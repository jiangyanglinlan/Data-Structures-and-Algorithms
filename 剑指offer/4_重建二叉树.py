# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if pre is None or tin is None or len(pre) == 0 or len(tin) == 0:
            return None
        find_inorder = dict()
        for i in xrange(0, len(tin)):
            find_inorder[tin[i]] = i
        return self.helper(pre, 0, len(tin) - 1, find_inorder)

    def helper(self, pre, start, end, find_inorder):
        if len(pre) == 0:
            return None
        if start > end:
            return None
        root = TreeNode(pre.pop(0))
        if start == end:
            return root
        root.left = self.helper(pre, start, find_inorder[root.val] - 1, find_inorder)
        root.right = self.helper(pre, find_inorder[root.val] + 1, end, find_inorder)
        return root