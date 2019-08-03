# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
            result = (num1 ^ num2) & 0xffffffff
            carry = ((num1 & num2) << 1) & 0xffffffff
            num1 = result
            num2 = carry
        if num1 <= 0x7fffffff:
            result = num1
        else:
            result = ~(num1^0xffffffff)
        return result