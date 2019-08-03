# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        abs_exponent = abs(exponent)
        result = self.power_with_unsigned_Exponent(base, abs_exponent)
        if exponent < 0:
            result = 1.0 / result
        return result

    def power_with_unsigned_Exponent(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        result = self.Power(base, exponent >> 1)
        result *= result
        if exponent & 0b1 == 1:
            # 奇数
            result *= base
        return result