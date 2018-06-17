"""
https://leetcode.com/problems/diameter-of-binary-tree/description/
543. Diameter of Binary Tree
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

Solution:

"""
class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dia=0
        def traverse(root):
            if root==None:
                return 0
            lheight = traverse(root.left)
            rheight = traverse(root.right)
            self.dia=max(self.dia, lheight+rheight+1)
            return max(lheight,rheight)+1
        
        traverse(root)
        return self.dia-1 if root else 0