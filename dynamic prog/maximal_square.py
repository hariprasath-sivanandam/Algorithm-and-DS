"""
Question:

https://leetcode.com/problems/maximal-square/description/

221. Maximal Square

iven a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

Solution:
"""

class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(i>0 and j>0) and matrix[i][j]=="1":
                    curr = min(min(int(matrix[i-1][j-1]),int(matrix[i-1][j])), int(matrix[i][j-1]))+ int(matrix[i][j])
                    matrix[i][j]=str(curr)
                else:
                    curr=int(matrix[i][j])                     
                res= max(res,curr)
                
        return res*res