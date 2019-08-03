# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        d = {}
        result = []
        for i in array:
            if tsum - i in d:
                if len(result) > 0:
                    if (tsum - i) * i < result[0] * result[1]:
                        result[0], result[1] = tsum - i, i
                else:
                    result.append(tsum - i)
                    result.append(i)
            else:
                d[i] = True
        return result