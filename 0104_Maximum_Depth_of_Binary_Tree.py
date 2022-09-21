"""
LeetCode Question: https://leetcode.com/problems/maximum-depth-of-binary-tree/

JavaScript Solution: https://replit.com/@ZhangMYihua/Maximum-depth#index.js
"""

def maxDepth(node, currentDepth=0):
    if not node:
        return currentDepth
    currentDepth += 1
    
    return max(maxDepth(node.right, currentDepth), maxDepth(node.left, currentDepth))