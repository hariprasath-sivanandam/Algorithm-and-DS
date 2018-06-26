"""
Question:
https://leetcode.com/problems/generate-parentheses/description/
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

Solution:
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def generate(path,l,r):
            print()
            if len(path)==2*n:
                return generate.res.append(path)
            if(l<n):
                generate(path+'(',l+1,r)
            if(l>r):
                generate(path+')',l,r+1)
                
        generate.res=[]
        generate('',0,0)
        return generate.res