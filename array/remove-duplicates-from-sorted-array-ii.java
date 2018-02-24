Question:

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Remove Duplicates from Sorted Array II
For example,
Given sorted array nums = [1,1,1,2,2,3],
Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. 
It doesn't matter what you leave beyond the new length.

Solution:

class Solution {
    public int removeDuplicates(int[] nums) {
        int i=0, k=0;
        
        for(int j=1; j<nums.length; j++){
            if(nums[i] != nums[j] || (nums[i] == nums[j] && k==0)){
                k= nums[i] ==nums[j] ? 1 :0;
                nums[++i] =nums[j];
            }
        }
        return ++i;
    }
}