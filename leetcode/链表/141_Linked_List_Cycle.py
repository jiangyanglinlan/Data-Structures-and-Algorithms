# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow_node = head
        fast_node = head
        while slow_node is not None and fast_node is not None:
            slow_node = slow_node.next
            if fast_node.next is not None:
                fast_node = fast_node.next.next
            else:
                return False
            if slow_node == fast_node:
                return True
        return False