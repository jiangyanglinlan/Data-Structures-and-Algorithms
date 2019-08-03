'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return None
        l = []
        self.helper(pRootOfTree, l)
        for i in xrange(0, len(l)):
            if i == 0:
                l[i].left = None
                if i + 1 < len(l):
                    l[i].right = l[i + 1]
                else:
                    l[i].right = None
            elif i == len(l) - 1:
                l[i].right = None
                if i - 1 >= 0:
                    l[i].left = l[i - 1]
                else:
                    l[i].left = None
            else:
                l[i].right = l[i + 1]
                l[i].left = l[i - 1]
        return l[0]

    def helper(self, root, l):
        if root is None:
            return
        self.helper(root.left, l)
        l.append(root)
        self.helper(root.right, l)