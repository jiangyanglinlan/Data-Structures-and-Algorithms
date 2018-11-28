# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        length = self.get_length(head)
        k = k % length

        if k == 0:
            return head

        slow_point = head
        fast_point = head

        for i in range(0, k):
            fast_point = fast_point.next

        while fast_point.next is not None:
            slow_point = slow_point.next
            fast_point = fast_point.next

        fast_point.next = head
        head = slow_point.next
        slow_point.next = None

        return head

    @staticmethod
    def get_length(head):
        index = 0
        start = head
        while start is not None:
            index += 1
            start = start.next
        return index