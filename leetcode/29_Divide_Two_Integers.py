class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0

        flag = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            flag = -1

        dividend = abs(dividend)
        divisor = abs(divisor)
        max_sum = pow(2, 31)

        result = self.help(dividend, divisor) * flag
        if (result < 0 and result < -max_sum) or (result > 0 and result > max_sum - 1):
            return max_sum -1
        return result

    def help(self, dividend, divisor):
        '''
        计算 除数 
        '''
        if dividend < divisor:
            return 0
        sum = divisor
        multiple = 1
        while (sum + sum) <= dividend:
            sum += sum
            multiple += multiple
        return multiple + self.help(dividend - sum, divisor)