'''
这道题我用的 K-Sum 方法做的，时间复杂度是 O(n^3)
'''

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) == 4:
            if nums[0] + nums[1] + nums[2] + nums[3] == target:
                return [nums, ]
            else:
                return []
        end_result = []
        nums = sorted(nums)
        nums_len = len(nums)
        for i in range(nums_len - 3):
            for j in range(i + 1, nums_len - 2):
                first = j + 1
                second = nums_len - 1
                new_target = target - nums[i] - nums[j]
                while first < second:
                    if nums[first] + nums[second] == new_target:
                        result = []
                        result.append(nums[i])
                        result.append(nums[j])
                        result.append(nums[first])
                        result.append(nums[second])
                        if result not in end_result:
                            end_result.append(result)
                        first += 1
                        second -= 1
                    if nums[first] + nums[second] < new_target:
                        first += 1
                    if nums[first] + nums[second] > new_target:
                        second -= 1
        return end_result


s = Solution()
a = s.fourSum([-3,-2,-1,0,0,1,2,3], 0)
print(a)
