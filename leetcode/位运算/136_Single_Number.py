class Solution:
    def singleNumber(self, nums):
        if nums is None or len(nums) == 0:
            return -1
        res = 0
        for i in nums:
            res ^= i
            print('res =', res)
        return res
