"""
LeetCode Question: https://leetcode.com/problems/two-sum/

JavaScript Solution: https://replit.com/@ZhangMYihua/two-sum-optimal-solution#index.js
"""

numsArray = [1, 3, 7, 9, 2]
targetToFind = 11


def findTwoSum(nums, target):
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


print(findTwoSum(numsArray, targetToFind))
