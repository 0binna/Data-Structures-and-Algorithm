"""
LeetCode Question: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

JavaScript Solution: https://replit.com/@ZhangMYihua/remove-minimum-parentheses#index.js
"""

string1 = "(ab(cd)"

def minRemoveToMakeValid(s):
    res = [i for i in s]
    print(res)
    stack = []
    str1 = ""
    
    i = 0
    while i < len(res):
        if res[i] == '(':
            stack.append(i)
        elif res[i] == ')' and stack:
            stack.pop()
        elif res[i] == ')':
            res[i] = ""
        i += 1
    
    while stack:
        currentIndex = stack.pop()
        res[currentIndex] = ""
    
    return str1.join(res)


print(minRemoveToMakeValid(string1))