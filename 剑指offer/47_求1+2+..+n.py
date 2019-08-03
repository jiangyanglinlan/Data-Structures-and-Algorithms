# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.sum = 0

    def Sum_Solution(self, n):
        # write code here
        self.sum = n
        ans = n > 0 and self.func(n)
        return self.sum

    def func(self, n):
        self.sum += self.Sum_Solution(n - 1)