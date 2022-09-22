"""
LeetCode Question: https://leetcode.com/problems/binary-tree-level-order-traversal/

JavaScript Solution: https://replit.com/@ZhangMYihua/Level-Order#index.js
"""

from queue import Queue

def levelOrder(root):
    if not root:
        return []
    result = []
    queue = Queue(maxsize = 0)
    queue.put(root)
  
    while not queue.empty():
        currentLevelValues = []
        length = queue.qsize()
        count = 0

        while count < length:
            currentNode = queue.get()
            currentLevelValues.append(currentNode.val)
            if currentNode.left:
                queue.put(currentNode.left)
            if currentNode.right:
                queue.put(currentNode.right)
            count += 1
        result.append(currentLevelValues)
    return result