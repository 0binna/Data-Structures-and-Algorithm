"""
LeetCode Question: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

JavaScript Solution: https://replit.com/@ZhangMYihua/merge-multi-level-doubly-linked-list#index.js
"""

def flatten(head):
    if not head:
        return head

    currentNode = head
    while currentNode != None:
        if currentNode.child == None:
            currentNode = currentNode.next
        else:
            tail = currentNode.child
            while tail.next != None:
                tail = tail.next

            tail.next = currentNode.next
            if tail.next != None:
                tail.next.prev = tail

            currentNode.next = currentNode.child
            currentNode.next.prev = currentNode
            currentNode.child = None

    return head