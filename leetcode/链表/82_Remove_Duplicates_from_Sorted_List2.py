# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        dummy = ListNode(None)
        dummy.next = head
        head = dummy

        while head.next is not None and head.next.next is not None:
            if head.next.val == head.next.next.val:
                val = head.next.val
                while head.next is not None and head.next.val == val:
                    head.next = head.next.next
            else:
                head = head.next

        return dummy.next