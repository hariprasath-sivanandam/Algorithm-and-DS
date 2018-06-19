"""
Question:
https://leetcode.com/problems/binary-tree-inorder-traversal/description/
94. Binary Tree Inorder Traversal
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

Solution:
"""

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        s,res=[],[]
        
        while s or root:
            if root:
                s.append(root)
                root=root.left
            else:
                temp=s.pop()
                res.append(temp.val)
                root=temp.right
                
        return res