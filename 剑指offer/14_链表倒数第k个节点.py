# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        dummy = ListNode(None)
        dummy.next = head
        quick_node = dummy
        slow_node = dummy
        while k > 0 and quick_node.next is not None:
            quick_node = quick_node.next
            k -= 1
        if k > 0:
            return None
        while quick_node is not None:
            quick_node = quick_node.next
            slow_node = slow_node.next
        return slow_node