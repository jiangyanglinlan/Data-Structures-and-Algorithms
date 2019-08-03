# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        l = []
        for i in xrange(0, len(array)):
            if not self.isOdd(array[i]):
                l.append(array[i])
        for i in l:
            array.remove(i)
        array.extend(l)
        return array

    def isOdd(self, num):
        return not num % 2 == 0

    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]