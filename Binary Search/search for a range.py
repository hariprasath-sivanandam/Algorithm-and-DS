"""
Question:
https://leetcode.com/problems/search-for-a-range/description/

34. Search for a Range
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Solution:
"""
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def bs(l,h,findFirst):
            res=l
            while(l<=h):
                mid=l+(h-l)//2
                if(nums[mid]==target):
                    res=mid
                    if(findFirst):
                        h=mid-1
                    else:
                        l=mid+1
                elif nums[mid]>target:
                    h=mid-1
                else:
                    l=mid+1
            return res
        if(len(nums)>0):
            start = bs(0,len(nums)-1, True)
            end = bs(0,len(nums)-1,False)
            if (nums[start]==target):
                return [start,end]
        
        return [-1,-1] 