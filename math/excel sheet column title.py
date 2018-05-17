"""
Question:
https://leetcode.com/problems/excel-sheet-column-title/description/
168. Excel Sheet Column Title
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

Solution:
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        """
        1. Q clarity:
            given: integer from 1 to valid number that can be reproduced to a column number
            return: string which contains only alphabets[A-Z]
        2. Intuitive approach:
            since alphabet has 26 letter we use modulo 26 to get each character to construct the result string
            we need to decrement n at each iteration as 26/26 yield 1 which is not the desired case
            at each iteration insert the string in the beginning
        3. Code:
        """
        res=[]
        
        while n>0:
            val= (n+25)%26
            res.insert(0,chr(ord("A")+val))
            n-=1
            n= n//26

        return "".join(res)
        """
        4. Test Cases:
            0 => "" (base case)
            1=> "A" (boundary case for single character)
            26 => "Z"(boundary case for single character)
            701 => "ZY" (multiple character)
        """