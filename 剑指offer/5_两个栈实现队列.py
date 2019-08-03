# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack.append(node)

    def pop(self):
        # return xx
        if len(self.stack) == 0:
            return None
        while len(self.stack) > 0:
            self.stack2.append(self.stack.pop())
        result = self.stack2.pop()
        while len(self.stack2) > 0:
            self.stack.append(self.stack2.pop())
        return result