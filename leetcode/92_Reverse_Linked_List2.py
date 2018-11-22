# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        if m == n:
            return head

        dummy = ListNode(None)
        dummy.next = head
        head = dummy

        for i in range(1, m):
            if head is None:
                return None
            head = head.next

        pre_m_node = head  # 翻转开始的节点的前一个节点
        m_node = head.next  # 翻转开始的节点
        n_node = head.next  # 翻转结束的节点
        post_n_node = m_node.next  # 翻转结束的节点的下一个节点

        for i in range(m, n):
            temp = post_n_node.next
            post_n_node.next = n_node
            n_node = post_n_node
            post_n_node = temp

        m_node.next = post_n_node  # "翻转开始的节点" 指向 "翻转结束的节点的下一个节点"
        pre_m_node.next = n_node  # "翻转开始的节点的前一个节点" 指向 "翻转结束的节点"

        return dummy.next



