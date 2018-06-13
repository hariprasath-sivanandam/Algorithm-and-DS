"""
Question:
https://leetcode.com/problems/validate-binary-search-tree/description/
98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.

Solution:
"""

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root, l,r):
            if root==None: return True
            return (l<root.val and root.val<r) and check(root.left, l, root.val) and check(root.right, root.val, r)
        
        return check(root,-sys.maxsize-1, sys.maxsize)