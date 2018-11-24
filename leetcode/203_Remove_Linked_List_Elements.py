# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        head = dummy

        while head is not None:
            if head.next is not None and head.next.val == val:
                current_node = head.next.next
                while current_node is not None and current_node.val == val:
                    current_node = current_node.next
                head.next = current_node
            head = head.next

        return dummy.next
