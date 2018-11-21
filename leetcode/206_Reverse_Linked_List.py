# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
这一题的思路是:
假定一个当前链表头结点的前一个节点(prev), 然后用循环进行链表反转
需要注意反转时的逻辑
'''

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        prev = None
        while head is not None:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev  # while 循环后, head 指向了原链表最后一个元素的 next, 也就是 None, 所以要返回 prev
