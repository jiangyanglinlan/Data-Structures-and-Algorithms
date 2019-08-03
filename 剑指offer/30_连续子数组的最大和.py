# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        dp = [0 for i in xrange(0, len(array))]
        dp[0] = array[0]
        max_num = -1
        for i in xrange(0, len(array)):
            if dp[i - 1] > 0:
                dp[i] = dp[i - 1] + array[i]
            else:
                dp[i] = array[i]
            if max_num < dp[i]:
                max_num = dp[i]
        return max_num