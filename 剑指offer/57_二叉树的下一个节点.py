# -*- coding:utf-8 -*-

'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''

# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode is None:
            return None

        next_node = None
        if pNode.right is not None:
            next_node = pNode.right
            if pNode.right.left is not None:
                next_node = next_node.left
        elif pNode.next is not None:
            current_node = pNode
            parent_node = current_node.next
            while parent_node is not None and current_node == parent_node.right:
                current_node = parent_node
                parent_node = parent_node.next
            next_node = parent_node
        return next_node
