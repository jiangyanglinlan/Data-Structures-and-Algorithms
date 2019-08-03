# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if data is None or len(data) == 0:
            return 0
        start = self.binary_search(data, k, flag=True)
        end = self.binary_search(data, k, flag=False)
        if start is None or end is None:
            return 0
        return end - start + 1

    def binary_search(self, nums, target, flag=True):
        # flag 为 True 时取第一次出现, False 取第二次出现
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            if nums[start: end + 1] == [3, 3, 3]:
                debug = True
            mid = start + (end - start) / 2
            if target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                start = mid
            else:
                if flag is True:
                    end = mid
                else:
                    start = mid

        if flag is True:
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
        else:
            if nums[end] == target:
                return end
            if nums[start] == target:
                return start
        return None

