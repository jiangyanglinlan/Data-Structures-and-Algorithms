# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        fib = [0 for i in range(0, 40)]
        fib[0] = 0
        fib[1] = 1
        for i in range(2, len(fib)):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]