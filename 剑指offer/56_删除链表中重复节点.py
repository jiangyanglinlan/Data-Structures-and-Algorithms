# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        dummy = ListNode(None)
        dummy.next = pHead
        slow_point = dummy.next
        fast_point = dummy.next
        new_point = dummy.next
        while fast_point.next is not None and fast_point.next.next is not None:
            fast_point = fast_point.next.next
            slow_point = slow_point.next
            if slow_point == fast_point:
                # 存在环
                while new_point != slow_point:
                    new_point = new_point.next
                    slow_point = slow_point.next
                return new_point
        return None