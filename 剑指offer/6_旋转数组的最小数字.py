# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray is None or len(rotateArray) == 0:
            return 0

        start = 0
        end = len(rotateArray) - 1

        while (start + 1 < end):
            mid = start + ((end - start) // 2)
            if rotateArray[mid] < rotateArray[end]:
                end = mid
            else:
                start = mid

        if rotateArray[start] < rotateArray[end]:
            return rotateArray[start]
        return rotateArray[end]