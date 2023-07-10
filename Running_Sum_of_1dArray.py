'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
'''

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runsum=nums
        for i in range(len(nums)): 
            if i==0:
                continue
            runsum[i]=runsum[i-1] + runsum[i]
        return runsum