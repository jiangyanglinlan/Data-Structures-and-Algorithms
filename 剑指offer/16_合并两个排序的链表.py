# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1

        dummy = ListNode(None)
        current_node = dummy
        while pHead1 is not None and pHead2 is not None:
            if pHead1.val < pHead2.val:
                current_node.next = pHead1
                pHead1 = pHead1.next
                current_node = current_node.next
            else:
                current_node.next = pHead2
                pHead2 = pHead2.next
                current_node = current_node.next
        if pHead1 is None:
            current_node.next = pHead2
        if pHead2 is None:
            current_node.next = pHead1
        return dummy.next