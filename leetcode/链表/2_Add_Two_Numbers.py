# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        li1 = []
        li2 = []
        li1.append(l1.val)
        li2.append(l2.val)
        while l1.next != None:
            l1 = l1.next
            li1.append(l1.val)
            
        while l2.next != None:
            l2 = l2.next
            li2.append(l2.val)
            
        li1.reverse()
        li2.reverse()
       
        first_number = ''
        seconde_number = ''
        for s in li1:
            first_number += str(s)
        for s in li2:
            seconde_number += str(s)
        #print(l1)
        #print(l2)
        #for i in str(int(first_number) + int(seconde_number)):
         #   print(i)
        li = [int(i) for i in str(int(first_number)+int(seconde_number))]
        li.reverse()
        return li

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 模拟竖式运算
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

        return dummy.next.next