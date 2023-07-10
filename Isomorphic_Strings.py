'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true

'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) <= 1:
            return True
        a = {}
        b = {}
        for i in range(len(s)):
            if s[i] in a and a[s[i]] != t[i] or t[i] in b and b[t[i]] != s[i]:
                return False
            a[s[i]] = t[i]
            b[t[i]] = s[i]
        return True