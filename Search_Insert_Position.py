'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, curr_value in enumerate(nums):
            if curr_value >= target:
                return index 
        else:
            return len(nums)