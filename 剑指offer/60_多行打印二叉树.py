# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        result = []
        l = []
        l2 = []
        s = []
        if pRoot is None:
            return []
        l.append(pRoot)
        while len(l) > 0:
            current_node = l.pop(0)
            s.append(current_node.val)
            if current_node.left is not None:
                l2.append(current_node.left)
            if current_node.right is not None:
                l2.append(current_node.right)
            if len(l) == 0:
                if len(l2) > 0:
                    l.extend(l2)
                result.append(s)
                l2 = []
                s = []
        return result

