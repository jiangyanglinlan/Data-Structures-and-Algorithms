# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        d = {}
        result = []
        for num in array:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for num in array:
            if d[num] == 1:
                result.append(num)

        return result