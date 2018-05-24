"""
Question:
https://leetcode.com/problems/valid-perfect-square/description/

367. Valid Perfect Square
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Returns: True

Example 2:
Input: 14
Returns: False

Solution:
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return True
        low,high=2,num//2
        while(low<=high):
            mid=low+(high-low)//2
            temp=mid*mid
            if(temp==num):
                return True
            elif temp>num:
                high=mid-1
            else:
                low=mid+1
        return False
