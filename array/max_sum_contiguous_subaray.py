"""
Question:

https://leetcode.com/problems/maximum-subarray/description/
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Solution:
"""
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res,curr=None,None
        for i in range(len(nums)):
            if curr==None:
                curr=res=nums[i]
            else:
                curr=max(curr+nums[i], nums[i])
                res=max(curr, res)
        return res