# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or k == 0:
            return []
        return self.quick_select(tinput, k, 0, len(tinput) - 1)

    def quick_select(self, nums, k, start, end):
        if start == end:
            return sorted(nums[:start+1])

        index = self.partition(nums, start, end)
        num = index - start + 1

        if k == num:
            return sorted(nums[:index + 1])
        elif k > num:
            return self.quick_select(nums, k - num, index + 1, end)
        else:
            return self.quick_select(nums, k, start, index - 1)

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

