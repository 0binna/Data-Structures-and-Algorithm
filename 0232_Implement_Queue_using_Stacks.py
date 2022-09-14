"""
LeetCode Question: https://leetcode.com/problems/implement-queue-using-stacks/

JavaScript Solution: https://replit.com/@ZhangMYihua/Create-Queue-using-stacks#index.js
"""

class QueueWithStacks:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def enqueue(self, val):
        self.inStack.append(val)

    def dequeue(self):
        if not self.outStack:
            while len(self.inStack) > 0:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()

    def peek(self):
        if not self.outStack:
            while len(self.inStack) > 0:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    def empty(self):
        return not self.inStack and not self.outStack