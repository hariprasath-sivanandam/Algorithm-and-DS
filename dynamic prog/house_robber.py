"""
Question:

https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent 
houses have security system connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.


Solution:
"""

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        1. understand Q better:
            try to get maximum points,
            no adjacent house, no negative integer inside array
        2. Intuition Approach:
            have 4 pointers prev1, prev2, curr1, and curr2
            initailise all of them to zero
            and at final step return max(curr1, curr2)
        3.code
        """
        
        prevMax, currMax = 0, 0;
        for x in nums:
            temp = currMax
            currMax = max(prevMax + x, currMax)
            prevMax = temp
            print(prevMax, currMax)
            
        return currMax;
        
        """
        4.testcases:
        [] => 0
        [10] => 10
        [40,1,1000] => 1040
        [1,2,3,1] => 4
        [2,7,9,3,1] => 12
        """