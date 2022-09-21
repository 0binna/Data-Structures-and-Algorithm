"""
LeetCode Question: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

JavaScript Solution: https://replit.com/@ZhangMYihua/Find-start-and-end-of-target-OlogN#index.js
"""

array = [1,3,3,5,5,5,8,9]
targetToFind = 5

def searchRange(nums, target):
    if len(nums) < 1:
        return [-1, -1]
    firstPos = binarySearch(nums, 0, len(nums) - 1, target)

    if firstPos == -1:
        return [-1, -1]

    endPos, startPos = firstPos, firstPos
    temp1, temp2 = None, None

    while startPos != -1:
        temp1 = startPos
        startPos = binarySearch(nums, 0, startPos - 1, target)
    startPos = temp1

    while endPos != -1:
        temp2 = endPos
        endPos = binarySearch(nums, endPos + 1, len(nums) - 1, target)
    endPos = temp2

    return [startPos, endPos]

def binarySearch(nums, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        foundVal = nums[mid]
        if foundVal == target:
            return mid
        elif foundVal < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(searchRange(array, targetToFind))