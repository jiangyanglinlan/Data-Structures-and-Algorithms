# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder is None and inorder is None or (len(preorder) == 0 or len(inorder) == 0):
            return None
        return self.helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def helper(self, preorder, pstart, pend, inorder, istart, iend):
        '''
        :param preorder: 前序遍历序列
        :param pstart: preorder 中左(右)子树节点开始下标
        :param pend: preorder 中左(右)子树节点结束下标
        :param inorder: 中序遍历序列
        :param istart: inorder 中左(右)子树节点开始下标
        :param iend: inorder 中左(右)子树节点结束下标
        :return:
        '''
        if istart > iend:
            return None
        root = TreeNode(preorder[pstart])
        pos = self.find(inorder, preorder[pstart])
        root.left = self.helper(preorder, pstart + 1, pstart + pos - istart, inorder, istart, pos - 1)
        root.right = self.helper(preorder, pend - iend + pos + 1, pend, inorder, pos + 1, iend)
        return root

    @staticmethod
    def find(inorder, value):
        for i in range(0, len(inorder)):
            if inorder[i] == value:
                return i
        return -1
