# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if s == '':
            return ''
        result = ''
        rol = n % len(s)
        for i in range(rol, len(s)):
            result += s[i]
        for i in range(0, rol):
            result += s[i]
        return result