"""
Question:
https://leetcode.com/problems/find-bottom-left-tree-value/description/
 Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:

Input:

    2
   / \
  1   3

Output:
1

Example 2:

Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

Note: You may assume the tree (i.e., the given root node) is not NULL. 

Solution:
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def leftmost(root,level):
            if root:
                if level> leftmost.max_level:
                    leftmost.max_level = level
                    leftmost.res=root.val
                leftmost(root.left, level+1)
                leftmost(root.right, level+1)        
        
        leftmost.max_level=0
        leftmost.res=None
        leftmost(root,1)
        return leftmost.res