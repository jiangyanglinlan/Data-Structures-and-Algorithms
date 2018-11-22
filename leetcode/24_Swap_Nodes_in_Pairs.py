# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        current_node = dummy
        while current_node.next is not None and current_node.next.next is not None:
            first_node = current_node.next
            second_node = current_node.next.next

            first_node.next = second_node.next
            second_node.next = first_node
            current_node.next = second_node
            current_node = first_node

        return dummy.next