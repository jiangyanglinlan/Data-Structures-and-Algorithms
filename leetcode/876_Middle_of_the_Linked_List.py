# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next is None:
            return head
        slow_point = head
        fast_point = head
        while True:
            if fast_point.next is None:
                return slow_point
            if fast_point.next.next is None:
                return slow_point.next
            fast_point = fast_point.next.next
            slow_point = slow_point.next