"""
LeetCode Question: https://leetcode.com/problems/valid-palindrome-ii/

JavaScript Solution: https://replit.com/@ZhangMYihua/Almost-palindrome-solution#index.js
"""

input = "abca"

def validPalindrome(s):
    start, end = 0, len(s) -1
    while start < end:
        if s[start] != s[end]:
            return validSubPalindrome(s, start + 1, end) or validSubPalindrome(s, start, end - 1)
        start += 1
        end -= 1
    return True

def validSubPalindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

print(validPalindrome(input))