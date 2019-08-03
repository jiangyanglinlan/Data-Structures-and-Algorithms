# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        result = []
        if root is not None:
            r = [root,]
        else:
            r = []
        while len(r) > 0:
            node = r.pop(0)
            result.append(node.val)
            if node.left is not None:
                r.append(node.left)
            if node.right is not None:
                r.append(node.right)
        return result