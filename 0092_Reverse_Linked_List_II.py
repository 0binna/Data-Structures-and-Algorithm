"""
LeetCode Question: https://leetcode.com/problems/reverse-linked-list-ii/

JavaScript Solution: https://replit.com/@ZhangMYihua/M-N-reversals#index.js
"""

def reverseBetween(head, left, right):
    currentPosition, currentNode = 1, head
    start = head
  
    while currentPosition < left:
        start = currentNode
        currentNode = currentNode.next
        currentPosition += 1
  
    newList, tail = None, currentNode
  
    while currentPosition >= left and currentPosition <= right:
        next = currentNode.next
        currentNode.next = newList
        newList = currentNode
        currentNode = next
        currentPosition += 1
  
    start.next = newList
    tail.next = currentNode
  
    if left > 1:
        return head
    else:
        return newList