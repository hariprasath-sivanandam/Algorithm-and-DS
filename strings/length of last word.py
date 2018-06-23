"""
https://leetcode.com/problems/length-of-last-word/description/
Question:
58. Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.

Example:
Input: "Hello World"
Output: 5

Solution:
"""

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        for i in range(len(s)):
            if s[~i]==" " and count>0: return count
            if s[~i]!=" ": count+=1
        return count