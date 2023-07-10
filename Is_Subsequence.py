'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        queue = []
        for i in range(len(s)):
            queue.append(s[i])
        for i in range(len(t)):
            if t[i] in queue:
                if t[i] == queue[0]:
                    queue.pop(0)
        return len(queue) == 0