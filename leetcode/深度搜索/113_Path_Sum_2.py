# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        if root is None:
            return None
        result = []
        l = []
        self.helper(root, l, sum, result)
        return result

    def helper(self, root, l, target, result):
        if root.left is None and root.right is None:
            if target == root.val:
                l.append(root.val)
                new_list = l.copy()
                l.pop()
                result.append(new_list)
            return

        if root.left is not None:
            l.append(root.val)
            self.helper(root.left, l, target - root.val, result)
            l.pop()

        if root.right is not None:
            l.append(root.val)
            self.helper(root.right, l, target - root.val, result)
            l.pop()
