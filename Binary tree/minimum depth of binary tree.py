"""
Question:
https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

Solution:
"""
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def minlen(root):
            if root==None: return sys.maxsize 
            if not root.left and not root.right: return 1
            return min(minlen(root.left),minlen(root.right))+1
            
        
        res= minlen(root) if root else 0
        return res
            