"""
LeetCode Question: https://leetcode.com/problems/linked-list-cycle-ii/

JavaScript Solution: https://replit.com/@ZhangMYihua/cycle-detection-Flyods-tortoise-and-hare#index.js
"""

def findCycle(head):
    if not head:
        return None
  
    tortoise, hare = head, head
  
    while True:
        tortoise = tortoise.next
        hare = hare.next
    
        if hare == None or hare.next == None:
            return None
        else:
            hare = hare.next
    
        if tortoise == hare:
            break
  
    p1 = head
    p2 = tortoise
  
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
  
    return p2