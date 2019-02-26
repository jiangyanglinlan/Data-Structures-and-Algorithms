# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        l = []
        l.append(root)
        if root is None:
            return None

        depth = 1
        while len(l) > 0:
            l2 = []
            while len(l) > 0:
                l2.append(l.pop(0))
            for node in l2:
                if node.left is None and node.right is None:
                    return depth

                if node.left is not None:
                    l.append(node.left)
                if node.right is not None:
                    l.append(node.right)
            depth += 1
        return depth