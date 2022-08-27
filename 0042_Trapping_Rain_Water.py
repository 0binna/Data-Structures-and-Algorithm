"""
LeetCode Question: https://leetcode.com/problems/trapping-rain-water/

JavaScript Solution: https://replit.com/@ZhangMYihua/trapping-rainwater-optimal-solution#index.js
"""

elevationArray = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]

"""
1. Identify the pointer with the lesser value
2. Is this pointer value greater than or equal to max on that side?
  yes -> update max on that side
  no -> get water for pointer, add to total
3. move pointer inwards
4. repeat for other pointer
"""

def getTrappedRainwater(heights):
    left, right, totalWater, maxLeft, maxRight = 0, len(heights) - 1, 0, 0, 0
    
    while left < right:
        if heights[left] <= heights[right]:
            if heights[left] >= maxLeft:
                maxLeft = heights[left]
            else:
                totalWater += maxLeft - heights[left]
            left += 1
        else:
            if heights[right] >= maxRight:
                maxRight = heights[right]
            else:
                totalWater += maxRight - heights[right]
            right -= 1
    return totalWater


print(getTrappedRainwater(elevationArray))