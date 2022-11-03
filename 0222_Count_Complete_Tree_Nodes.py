"""
LeetCode Question: https://leetcode.com/problems/count-complete-tree-nodes/

JavaScript Solution: https://replit.com/@ZhangMYihua/Number-of-Nodes-in-Complete-Binary-Tree#index.js
"""

import math

def countNodes(root):
    if not root:
        return 0
  
    height = getTreeHeight(root)
  
    if height == 0:
        return 1
  
    upperCount = (2**height) - 1
  
    left, right = 0, upperCount
  
    while left < right:
        idxToFind = Math.ceil((left + right) / 2)
    
        if nodeExists(idxToFind, height, root):
            left = idxToFind
        else:
            right = idxToFind - 1
 
    return upperCount + left + 1


def getTreeHeight(root):
    height = 0
    while root.left != None:
        height += 1
        root = root.left
    return height

def nodeExists(idxToFind, height, node):
    left, right, count = 0, (2**height) - 1, 0
  
    while count < height:
        midOfNode = Math.ceil((left + right) / 2)
    
        if idxToFind >= midOfNode:
            node = node.right
            left = midOfNode
        else:
            node = node.left
            right = midOfNode - 1
        count += 1
        
    return node != None
