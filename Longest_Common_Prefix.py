'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            if len(strs) == 0:
                return ""
            a = strs[0]
            for i in range(1, len(strs)):
                prefix = ""
                if len(a) == 0:
                    break
                for j in range(len(strs[i])):
                    if j < len(a) and a[j] == strs[i][j]:
                        prefix += a[j]
                    else:
                        break
                a = prefix
            return a 
            