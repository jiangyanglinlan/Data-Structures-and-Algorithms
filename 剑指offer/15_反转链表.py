# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None:
            return None
        pre_node = None
        while pHead is not None:
            temp = pHead.next
            pHead.next = pre_node
            pre_node = pHead
            pHead = temp
        return pre_node
