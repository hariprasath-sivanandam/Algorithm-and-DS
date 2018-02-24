Question:

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

Find Minimum in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
You may assume no duplicate exists in the array.

Example:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.

Solution:

class Solution {
    public int findMin(int[] nums) {
        int mid,low=0, high=nums.length-1;
        
        while(nums[low]>nums[high]){
            mid = low+(high-low)/2;
            if(nums[mid]>nums[high])
                low=mid+1;
            else
                high=mid;
        }
        
        return nums[low];
    }  
}