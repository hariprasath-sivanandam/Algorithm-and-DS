"""
Question:
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

83. Remove Duplicates from Sorted List
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3

Solution:
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, A):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not A: return A
        first,second=A, A.next
        
        while second:
	        if first.val==second.val:
	            first.next=second=second.next
	        else:
	            first,second=second,second.next
        
        return A

# check if atleast two elements are there 
# make sure A.next not throws an error