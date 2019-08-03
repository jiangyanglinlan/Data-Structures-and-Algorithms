# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence is None or len(sequence) == 0:
            return False

        root = sequence[-1]
        i = 0
        while i < len(sequence) - 1:
            if sequence[i] > root:
                break
            i += 1

        j = i
        while j < len(sequence) - 1:
            if sequence[j] < root:
                return False
            j += 1

        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[0: i])

        right = True
        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i + 1: len(sequence)])

        return left and right
