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
        slow_point = head
        fast_point = head
        while n > 0:
            fast_point = fast_point.next
            n -= 1

        if fast_point is None:
            return head.next

        while fast_point.next is not None:
            fast_point = fast_point.next
            slow_point = slow_point.next

        slow_point.next = slow_point.next.next

        return head