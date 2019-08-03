# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return None
        new_list_node = RandomListNode(pHead.label)
        new_list_node.next = self.Clone(pHead.next)
        new_list_node.random = pHead.random
        return new_list_node