"""
LeetCode Question: https://leetcode.com/problems/two-sum/

JavaScript Solution: https://replit.com/@ZhangMYihua/two-sum-optimal-solution#index.js
"""
import argparse
import math
import pickle
import random as R
import time
from collections import defaultdict
from functools import partial, reduce, wraps
from itertools import combinations, starmap
from pathlib import Path
from statistics import mean, median, stdev
from uuid import uuid4

from numba import njit
from numba.typed import List

TEST_CASES_DIR = Path(__name__).parent / "test_cases" / "0001"
TEST_CASES_DIR.mkdir(exist_ok=True, parents=True)


def timeit(func):
    """Decorator to time function execution."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        return result, duration

    return wrapper


def start_dag(val, lo, hi):
    """The center coordinates in summation mattrix that sum to val."""
    if val % 2 == 0:
        lane = [lo, lo]
    else:
        lane = [lo + 1, lo]
    move = (val - sum(lane)) // 2
    return lane[0] + move, lane[1] + move


def sum_pairs(val, lo, hi):
    """All unique values in range [`lo`, `hi`] inclusize that sum to `val`."""
    start = start_dag(val, lo, hi)
    return [
        (start[0] + i, start[1] - i)
        for i in range(min(hi - start[0], start[1] - lo) + 1)
    ]


def gen_test_case(lo, hi):
    """Generate test case."""
    target = R.randint(lo + lo, hi + hi)
    answers = sum_pairs(target, lo, hi)
    answer = R.choice(answers)
    invalid_values = set(answer) | set(map(R.choice, answers))
    nums = list(answer) + list(set(range(lo, hi + 1)) - invalid_values)
    R.shuffle(nums)
    return target, nums


def all_sums(values):
    """All combinations summed up."""
    return set(starmap(sum, combinations(values)))


def print_addition_mattrix(lo=1, hi=10):
    """Helper function to print addition mattrix."""
    mat = "\n".join(
        [
            f"{x} \t"
            + "\t".join([str(x + y) if x <= y else "" for y in range(lo, hi + 1)])
            for x in range(lo, hi + 1)
        ]
    )
    print("\t" + "\t".join([str(x) for x in range(lo, hi + 1)]))
    print(mat)


def stats(data):
    """Get stats for `data`."""
    return {
        "mean": mean(data),
        "median": median(data),
        "stdev": stdev(data),
        "min": min(data),
        "max": max(data),
    }


def new_test_cases(lo, hi, count):
    """Wrapper to gen_test_case for cli use."""
    for i in range(count):
        target, nums = gen_test_case(lo, hi)
        filename = TEST_CASES_DIR / f"{lo}_{hi}_{uuid4()}.pickle"
        with open(filename, "wb+") as file:
            pickle.dump((target, nums), file)
        print(f"{i+1}: {filename}")


def load_test_cases():
    """Load existing test cases."""
    for test_case_file in TEST_CASES_DIR.glob("*.pickle"):
        with open(test_case_file, "rb") as file:
            yield test_case_file, pickle.load(file)


def _fixed_width(string, width):
    padding = (width - len(string)) / 2
    left_padding, right_padding = math.floor(padding), math.ceil(padding)
    return " " * left_padding + string + " " * right_padding


def _table_row(widths, data):
    data_line = list(starmap(_fixed_width, zip(map(str, data), widths)))
    return f"| {' | '.join(data_line)} |"


def print_results(results, sort_by=None):
    """Print results as a table."""
    header = ["name", *stats([1, 1]).keys()]
    rows = [
        [name, *map("{0:.6f}".format, stats(result).values())]
        for name, result in results.items()
    ]
    if (sort_by_i := header.index(sort_by)) >= 0:
        rows.sort(key=lambda x: x[sort_by_i])

    col_widths = [max(map(len, line)) for line in zip(*[header, *rows])]
    header_sep = "-" * (
        reduce(lambda a, b: a + b, col_widths) + 3 * len(col_widths) + 1
    )
    print(_table_row(col_widths, header))
    print(header_sep)
    print("\n".join(map(partial(_table_row, col_widths), rows)))


def findTwoSum(nums, target):
    """Original solution."""
    numsMap = {}

    p = 0
    while p < len(nums):
        if nums[p] in numsMap.keys():
            currentMapVal = numsMap[nums[p]]
            return [currentMapVal, p]
        else:
            numberToFind = target - nums[p]
            numsMap[numberToFind] = p
        p += 1

    return None


def findTwoSumRewrite(nums, target):
    """Clean up Original solution."""
    numsMap = {}
    for i, num in enumerate(nums):
        if num in numsMap:
            return [numsMap[num], i]
        else:
            numsMap[target - num] = i
    return None


@njit
def findTwoSumJit(nums, target):
    """Rewrite with jit."""
    numsMap = {}
    for i, num in enumerate(nums):
        if num in numsMap:
            return [numsMap[num], i]
        else:
            numsMap[target - num] = i
    return None


def run_tests():
    """Cli: Run tests with all functions."""
    results = defaultdict(list)
    for (name, func) in [
        (name[len("findTwoSum") :].strip() or "orig", timeit(func))
        for name, func in globals().items()
        if name.startswith("findTwoSum")
    ]:
        for i, (case_name, (target, nums)) in enumerate(load_test_cases()):
            nums = List(nums)
            func(nums, target)  # Warm-up
            result, duration = func(nums, target)
            assert result, f"no result: {name} - {case_name}"
            actual = nums[result[0]] + nums[result[1]]
            assert actual == target, f"{name}: {case_name} {target} != {actual}"
            results[name].append(duration)

    return dict(results)


def main():
    """Cli entrypoint."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--low", default=1, type=int)
    parser.add_argument("-u", "--upper", default=1000, type=int)
    parser.add_argument("-c", "--count", default=100, type=int)
    parser.add_argument(
        "-s", "--sort", default="mean", choices=list(stats([1, 1]).keys())
    )

    parser.add_argument("command", choices=["new-test-cases", "run-test"])
    args = parser.parse_args()

    if args.command == "new-test-cases":
        new_test_cases(args.low, args.upper, args.count)
    else:
        results = run_tests()
        print_results(results, sort_by=args.sort)


if __name__ == "__main__":
    main()
