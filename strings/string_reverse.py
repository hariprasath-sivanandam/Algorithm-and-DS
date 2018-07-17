"""
Question:
https://leetcode.com/problems/reverse-words-in-a-string/description/
151. Reverse Words in a String

Given an input string, reverse the string word by word.

Example:  

Input: "the sky is blue",
Output: "blue is sky the".

Note:

    A word is defined as a sequence of non-space characters.
    Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
    You need to reduce multiple spaces between two words to a single space in the reversed string.

Follow up: For C programmers, try to solve it in-place in O(1) space.

Solution:
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls=list(s.strip())
        def rev(start, end):
            while(start<end): ls[start], ls[end], start, end = ls[end], ls[start], start+1, end-1
                
        i=idx=0
        rev(i,len(ls)-1)
        while idx<(len(ls)-1):
            if ls[idx]==" " and i!=idx:
                rev(i,idx-1)
                i=idx+1
            elif ls[idx]==" ":
                del ls[idx]
                continue
            idx+=1
            
        if i<len(ls):
            rev(i, len(ls)-1)
        return "".join(ls)
        