# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, node):
        # write code here
        self.s1.append(node)
        if len(self.s2) == 0 or node < self.s2[-1]:
            self.s2.append(node)

    def pop(self):
        # write code here
        num = self.s1.pop()
        if len(self.s2) > 0 and self.s2[-1] == num:
            self.s2.pop()
        return num

    def top(self):
        # write code here
        if len(self.s1) > 0:
            return self.s1[-1]
        else:
            return None

    def min(self):
        # write code here
        return self.s2[-1]