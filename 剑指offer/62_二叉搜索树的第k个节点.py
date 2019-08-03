# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if pRoot is None:
            return None
        l = []
        self.helper(pRoot, l)
        if k - 1 >= 0 and k - 1 < len(l):
            return l[k - 1]
        return None

    def helper(self, root, l):
        if root is None:
            return
        self.helper(root.left, l)
        l.append(root)
        self.helper(root.right, l)