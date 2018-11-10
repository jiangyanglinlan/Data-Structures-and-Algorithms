# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre_point = head  # 记录要删除的节点的前一个节点
        slow_point = head
        fast_point = head
        while n > 0:
            fast_point = fast_point.next
            n -= 1

        flag = False
        while fast_point is not None:
            slow_point = slow_point.next
            fast_point = fast_point.next
            if flag is True:
                pre_point = pre_point.next
            flag = True

        if pre_point == slow_point: # 出现此情况的输入举例: ([1], 1)、([1, 2], 2)
            return pre_point.next

        pre_point.next = slow_point.next
        slow_point.next = None
        return head