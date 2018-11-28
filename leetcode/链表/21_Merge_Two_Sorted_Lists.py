# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        dummy = ListNode(None)
        current_node = dummy
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                current_node.next = l1
                l1 = l1.next
                current_node = current_node.next
            else:
                current_node.next = l2
                l2 = l2.next
                current_node = current_node.next

        if l1 is None:
            current_node.next = l2
        else:
            current_node.next = l1
        return dummy.next