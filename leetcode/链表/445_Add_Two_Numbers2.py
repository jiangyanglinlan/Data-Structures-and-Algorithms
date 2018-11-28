# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 这题如果直接遍历链表运算的话, 有几个问题:
# 1. 两个数有可能位数不同, 不知道从哪个位置开始。
# 2. 模拟竖式运算应该从个位开始, 而个位在链表最后一个节点, 无法处理进位

# 我一开始的做法是翻转链表, 翻转之后就和 leetcode 第 2 题一样的运算了(代码 1)
# 后来注意到题目描述有不翻转链表。这样做法改成了将链表节点的值入栈, 然后出栈运算(代码 2)

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.reverse_linked_list(l1)
        l2 = self.reverse_linked_list(l2)

        dummy = ListNode(None)
        old_node = ListNode(None)
        dummy.next = old_node
        carry = 0
        while l1 is not None and l2 is not None:
            num1 = l1.val
            num2 = l2.val
            sum = num1 + num2 + carry
            remainder = sum % 10  # 余数
            carry = sum // 10  # 进位
            new_node = ListNode(remainder)
            old_node.next = new_node
            old_node = new_node
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            sum = l1.val + carry
            remainder = sum % 10  # 余数
            carry = sum // 10  # 进位
            new_node = ListNode(remainder)
            old_node.next = new_node
            old_node = new_node
            l1 = l1.next

        while l2 is not None:
            sum = l2.val + carry
            remainder = sum % 10  # 余数
            carry = sum // 10  # 进位
            new_node = ListNode(remainder)
            old_node.next = new_node
            old_node = new_node
            l2 = l2.next

        if carry != 0:
            old_node.next = ListNode(1)

        self.reverse_linked_list(dummy.next.next)
        return dummy.next.next

    @staticmethod
    def reverse_linked_list(head):
        if head is None or head.next is None:
            return head

        prev = None
        while head is not None:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []

        while l1 is not None:
            stack1.append(l1.val)
            l1 = l1.next

        while l2 is not None:
            stack2.append(l2.val)
            l2 = l2.next

        dummy = ListNode(None)
        old_node = ListNode(None)
        dummy.next = old_node
        carry = 0
        while len(stack1) != 0 and len(stack2) != 0:
            num1 = stack1.pop()
            num2 = stack2.pop()
            sum = num1 + num2 + carry

            remainder = sum % 10  # 余数
            carry = sum // 10  # 进位
            new_node = ListNode(remainder)
            old_node.next = new_node
            old_node = new_node

        while len(stack1) != 0:
            sum = stack1.pop() + carry
            remainder = sum % 10  # 余数
            carry = sum // 10  # 进位
            new_node = ListNode(remainder)
            old_node.next = new_node
            old_node = new_node

        while len(stack2) != 0:
            sum = stack2.pop() + carry
            remainder = sum % 10  # 余数
            carry = sum // 10  # 进位
            new_node = ListNode(remainder)
            old_node.next = new_node
            old_node = new_node

        if carry != 0:
            old_node.next = ListNode(1)

        result = self.reverse_linked_list(dummy.next.next)
        return result
