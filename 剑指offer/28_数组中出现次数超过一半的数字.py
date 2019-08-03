# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if numbers is None:
            return 0
        d = {}
        for i in numbers:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        length = len(numbers) / 2
        for k, v in d.items():
            if v > length:
                return k
        return 0