# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        result = []
        start = 1
        end = 2
        while start < end and start > 0 and end < tsum:
            num = ((start + end) * (end - start + 1))/2
            if num == tsum:
                l = [i for i in range(start, end + 1)]
                result.append(l)
                start += 1
            if num > tsum:
                start += 1
            else:
                end += 1
        return result