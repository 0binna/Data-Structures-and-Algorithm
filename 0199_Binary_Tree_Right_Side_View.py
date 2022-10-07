"""
LeetCode Question: https://leetcode.com/problems/binary-tree-right-side-view/

JavaScript Solution: https://replit.com/@ZhangMYihua/Binary-tree-right-side-view-DFS#index.js
"""

def rightSideViewDFS(root):
    result = []
    depthFirstSearch(root, 0, result)
    return result

def depthFirstSearch(node, currentLevel, result):
    if not node:
        return
    if currentLevel == len(result):
        result.append(node.val)

    if node.right:
        depthFirstSearch(node.right, currentLevel + 1, result)
  
    if node.left:
        depthFirstSearch(node.left, currentLevel + 1, result)