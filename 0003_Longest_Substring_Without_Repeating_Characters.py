"""
LeetCode Question: https://leetcode.com/problems/longest-substring-without-repeating-characters/

JavaScript Solution: https://replit.com/@ZhangMYihua/longest-substring-without-repeat-characters-optimal#index.js
"""

string = "agghj"

def lengthOfLongestSubstring(s):
    if len(s) <= 1: 
        return len(s)
    
    seen = {}
    left, longest, right = 0, 0, 0
    
    while right < len(s):
        currentChar = s[right]
        if currentChar in seen.keys():
            previouslySeenChar = seen[currentChar]
            
            if previouslySeenChar >= left:
                left = previouslySeenChar + 1
        
        seen[currentChar] = right
        
        longest = max(longest, (right - left + 1))
    
        right += 1
    return longest

print(lengthOfLongestSubstring(string))
