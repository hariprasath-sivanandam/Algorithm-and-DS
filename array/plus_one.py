"""
Question:

https://leetcode.com/problems/plus-one/description/
66. Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Solution:
"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        carry=1
        
        for i in range(len(digits)):
            carry, digits[~i] = divmod(digits[~i]+carry, 10)
        
        if carry==1: digits.insert(0,carry)

        while digits[0]==0: del digits[0]
        
        return digits
    
        # if inpur array suppose to be immutable
        # carry=1
        # res=[]
        # for i in digits[::-1]:
        #     res.insert(0, (i+carry)%10)
        #     carry=(i+carry)//10
        # print(res)
        # if(carry==1): res.insert(0,1)
        # return res