# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True

        if abs(self.get_depth(root.left) - self.get_depth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_depth(self, root):
        if root is None:
            return 0
        return max(self.get_depth(root.left), self.get_depth(root.right)) + 1
