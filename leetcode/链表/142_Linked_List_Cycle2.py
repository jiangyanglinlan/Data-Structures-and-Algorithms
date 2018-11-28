# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
这一题是环形链表, 判断有没有环其实就是一个相遇问题, 定义两个指针, 一个走得快, 一个走得慢,
若两个指针重合则有环。
'''

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow_node = head
        fast_node = head
        while slow_node is not None and fast_node is not None:
            slow_node = slow_node.next
            if fast_node.next is not None:
                fast_node = fast_node.next.next
            else:
                return None
            if slow_node == fast_node:
                # 找到了环
                cycle_head_node = head
                while cycle_head_node != slow_node:
                    cycle_head_node = cycle_head_node.next
                    slow_node = slow_node.next
                return cycle_head_node
        return None