# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot is None or (pRoot.left is None and pRoot.right is None):
            return True
        if abs(self.get_depth(pRoot.left) - self.get_depth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def get_depth(self, root):
        if root is None:
            return 0
        return max(self.get_depth(root.left), self.get_depth(root.right)) + 1