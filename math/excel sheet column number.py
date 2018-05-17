"""
Question:
https://leetcode.com/problems/excel-sheet-column-number/description/
171. Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:
Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

Solution:
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        1. Q clarity:
            given: always alphabets[A-Z]
            return: number
        2. Intuitive Approach:
            string is traversed from right to left and each character is assessed 
            as we move through the string form right end , have the multiplier that grows geometricallly by a constant 26
            and add the result as we iterate thru each character in the string
        3. Code
        """
        mul,res=1,0
        
        for i in range(-1,-(len(s)+1),-1): # traverse the array from last
            res+= mul*(ord(s[i])-ord("A")+1)
            mul*=26
            
        return res
        """
        4.Test Cases:
            "" => 0 (empty string)
            "A" => 1 (single character)
            "Z" => 26 (boundary case)
            "ZAYX" => 458326 (multiple characters)
            
        """