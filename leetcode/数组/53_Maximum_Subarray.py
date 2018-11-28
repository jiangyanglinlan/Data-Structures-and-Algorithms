'''
这是一道 dp,
转移方程为 nums[i] = nums[i-1] > 0 ? nums[i] + nums[i-1]:nums[i]
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = nums[0]
        sum = nums[0]
        for i in range(1, len(nums)):
            sum = sum + nums[i] if sum + nums[i] > nums[i] else nums[i]
            if sum > max:
               max = sum
        return max

        
