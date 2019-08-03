# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        l = ''
        for i in s:
            if i == ' ':
                l += '%20'
            else:
                l += i
        return l