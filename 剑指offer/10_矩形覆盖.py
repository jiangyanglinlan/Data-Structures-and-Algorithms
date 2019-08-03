# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        nums = [0, 1, 2]
        for i in xrange(0, 500):
            nums.append(nums[-1] + nums[-2])
        return nums[number]