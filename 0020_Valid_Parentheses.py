"""
LeetCode Question: https://leetcode.com/problems/valid-parentheses/

JavaScript Solution: https://replit.com/@ZhangMYihua/valid-parentheses#index.js
"""

string = "{()[]}"

parens = {'(': ')', '{' : '}', '[': ']'}

def isValid(s):
    if(len(s) == 0):
        return True
  
    stack = []
  
    i = 0
    while i < len(s):
        if s[i] in parens.keys():
            stack.append(s[i])
        else:
            if stack:
                leftBracket = stack.pop()
                correctBracket = parens[leftBracket]
                if(s[i] != correctBracket):
                    return False
            else:
                return False
        i += 1
  
    return len(stack) == 0


print(isValid(string))