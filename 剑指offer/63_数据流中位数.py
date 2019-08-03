# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.nums = []

    def Insert(self, num):
        # write code here
        self.nums.append(num)

    def GetMedian(self, n=None):
        # write code here
        nums_length = len(self.nums)
        if nums_length & 0b1 == 1:
            # 奇数
            return self.quick_select(self.nums, 0, nums_length - 1, nums_length / 2 + 1)
        else:
            num1 = self.quick_select(self.nums, 0, nums_length - 1, nums_length / 2)
            num2 = self.quick_select(self.nums, 0, nums_length - 1, nums_length / 2 + 1)
            return float(num1 + num2) / 2

    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]

        index = self.partition(nums, start, end)
        num = index - start + 1

        if k == num:
            return nums[index]
        elif k > num:
            return self.quick_select(nums, index + 1, end, k - num)
        else:
            return self.quick_select(nums, start, index - 1, k)

    def partition(self, nums, start, end):
        pivot = nums[start]
        while start < end:
            while start < end and nums[end] >= pivot:
                end -= 1
            nums[start] = nums[end]
            while start < end and nums[start] <= pivot:
                start += 1
            nums[end] = nums[start]
        nums[start] = pivot
        return start