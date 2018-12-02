# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder is None and postorder is None:
            return None
        if len(inorder) == 0 and len(postorder) == 0:
            return None
        return self.helper(postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1)

    def helper(self, postorder, pstart, pend, inorder, istart, iend):
        if istart > iend:
            return None
        root = TreeNode(postorder[pend])
        pos = self.find(inorder, postorder[pend])
        root.right = self.helper(postorder, pend + pos - iend, pend - 1, inorder, pos + 1, iend)
        root.left = self.helper(postorder, pstart, pstart + pos - istart - 1, inorder, istart, pos - 1)
        return root

    @staticmethod
    def find(inorder, value):
        for i in range(0, len(inorder)):
            if inorder[i] == value:
                return i
        return -1

    def buildTree2(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if postorder is None and inorder is None or (len(postorder) == 0 or len(inorder) == 0):
            return None
        find_inorder = dict()
        for i in range(0, len(inorder)):
            find_inorder[inorder[i]] = i
        return self.helper2(postorder, 0, len(inorder) - 1, find_inorder)

    def helper2(self, postorder, start, end, find_inorder):
        if len(postorder) == 0:
            return None
        if start > end:
            return None

        root = TreeNode(postorder.pop())
        root.right = self.helper2(postorder, find_inorder[root.val] + 1, end, find_inorder)
        root.left = self.helper2(postorder, start, find_inorder[root.val] - 1, find_inorder)
        return root