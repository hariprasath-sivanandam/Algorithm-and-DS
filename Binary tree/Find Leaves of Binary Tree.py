"""
Question:
https://leetcode.com/problems/find-leaves-of-binary-tree/description/
366. Find Leaves of Binary Tree
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example:
Given binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Returns [4, 5, 3], [2], [1].

Explanation:
1. Removing the leaves [4, 5, 3] would result in this tree:

          1
         / 
        2          
2. Now removing the leaf [2] would result in this tree:

          1          
3. Now removing the leaf [1] would result in the empty tree:

          []         
Returns [4, 5, 3], [2], [1].

Solution:
"""
class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        mp={}
        def traversal(root):
            if root==None: return 0
            
            l= traversal(root.left)
            r= traversal(root.right)
            level = max(l,r)+1
            if level not in mp: mp[level]=[]
            mp[level].append(root.val)
            return level
        traversal(root)
        res=[]
        for i in range(1,len(mp)+1):
            res.append(mp[i])
        return res