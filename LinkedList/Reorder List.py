"""
Question:
https://leetcode.com/problems/reorder-list/description/

143. Reorder List
Given a sorted linked list, delete all duplicates such that each element appear only once.

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

Solution:
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, A):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not A: return
        slow=fast=A
        
        while(fast.next and fast.next.next):
	        slow,fast=slow.next,fast.next.next
        first,second,slow.next=A,slow.next,None #3rd initialization is important
        
        prev=nxt=None
        
        while(second):
	        nxt=second.next
	        second.next=prev
	        prev=second
	        second=nxt
        
        second=prev
        
        while first and second:
	        temp1=first.next
	        first.next=second
	        temp2=second.next
	        second.next=temp1
	        first=second.next
	        second=temp2