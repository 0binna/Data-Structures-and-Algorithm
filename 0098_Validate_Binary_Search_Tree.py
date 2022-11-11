"""
LeetCode Question: https://leetcode.com/problems/validate-binary-search-tree/

JavaScript Solution: https://replit.com/@ZhangMYihua/Validate-Binary-Search-Tree#index.js
"""

import math

def isValidBST(root):
    if not root:
        return True
    return dfs(root, -math.inf, math.inf)

def dfs(node, min, max):
    if node.val <= min or node.val >= max:
        return False
    
    if node.left:
        if not dfs(node.left, min, node.val):
            return False
    
    if node.right:
        if not dfs(node.right, node.val, max):
            return False
        
    return True