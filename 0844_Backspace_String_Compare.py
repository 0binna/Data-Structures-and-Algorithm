"""
LeetCode Question: https://leetcode.com/problems/backspace-string-compare/

JavaScript Solution:https://replit.com/@ZhangMYihua/backspace-string-compare-optimal#index.js
"""
string1 = "aaa###a"
string2 = "aaaa###a"

def backspaceCompare(S, T):
    p1, p2 = len(S) - 1, len(T) - 1

    while p1 >= 0 or p2 >= 0:
        if (p1 >= 0 and S[p1] == "#") or (p2 >= 0 and T[p2] == "#"):
            if S[p1] == "#" and p1 >= 0:
                backCount = 2
    
                while backCount > 0:
                    p1 -= 1
                    backCount -= 1
                    if S[p1] == "#" and p1 >= 0:
                        backCount += 2

            if T[p2] == "#" and p2 >= 0:
                backCount = 2

                while backCount > 0:
                    p2 -= 1
                    backCount -= 1
                    if T[p2] == "#" and p2 >= 0:
                        backCount += 2
        else:
            if (S[p1] != T[p2]) or p1 < 0 or p2 < 0:
                return False
            else:
                p1 -= 1
                p2 -= 1
        
    return True


print(backspaceCompare(string1, string2))