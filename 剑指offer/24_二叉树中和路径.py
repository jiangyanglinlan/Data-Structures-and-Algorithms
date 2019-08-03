# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return []
        result = []
        l = []
        self.helper(root, expectNumber, l, result)
        return result

    def helper(self, root, target, l, result):
        if root.left is None and root.right is None:
            if target == root.val:
                l.append(root.val)
                new_list = l[:]
                result.append(new_list)
                l.pop()
        if root.left is not None:
            l.append(root.val)
            self.helper(root.left, target - root.val, l, result)
            l.pop()
        if root.right is not None:
            l.append(root.val)
            self.helper(root.right, target - root.val, l, result)
            l.pop()