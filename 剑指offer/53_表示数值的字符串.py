# -*- coding:utf-8 -*-

'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''


class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        sign = False
        decimal = False
        has_e = False

        for i in xrange(0, len(s)):
            if s[i] == 'e' or s[i] == 'E':
                if has_e is True:
                    return False
                if i == len(s) - 1:
                    return False
                has_e = True

            elif s[i] == '+' or s[i] == '-':
                if sign is True and (s[i - 1] != 'e' and s[i - 1] != 'E'):
                    return False
                if sign is False:
                    if i != 0 and (s[i - 1] != 'e' and s[i - 1] != 'E'):
                        return False
                sign = True

            elif s[i] == '.':
                if has_e is True:
                    return False
                if decimal is True:
                    return False
                decimal = True
            elif not (s[i] >= '0' and s[i] <= '9'):
                return False
        return True
