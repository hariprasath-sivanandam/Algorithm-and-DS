"""
Question:
https://leetcode.com/problems/balanced-binary-tree/description/
110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7

Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

Return false.

Solution:
"""

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def traverse(root):
            if root:
                l = traverse(root.left)
                r = traverse(root.right)
                if l !=-1 and r!=-1 and abs(l-r)<2:
                    return max(l,r)+1
                return -1
            return 0
        return False if traverse(root)==-1 else True