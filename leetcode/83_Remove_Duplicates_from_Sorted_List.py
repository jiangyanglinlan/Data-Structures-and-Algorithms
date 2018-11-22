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
        dummy = ListNode(None)
        dummy.next = head

        while head is not None:
            while head.next is not None and head.next.val == head.val:
                head.next = head.next.next
            head = head.next
        return dummy.next