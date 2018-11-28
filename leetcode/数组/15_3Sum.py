'''
K-Sum
复杂度 O(n^3)
'''

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List
        """
        end_result = []

        if nums is None or len(nums) < 3:
            return []

        nums.sort()

        length = len(nums)

        for i in range(0, length-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            first = i + 1
            second = length - 1
            new_target = 0 - nums[i]
            while first < second:
                if nums[first] + nums[second] == new_target:
                    result = []
                    result.append(nums[i])
                    result.append(nums[first])
                    result.append(nums[second])
                    end_result.append(result)
                    while first < second and nums[first] == nums[first+1]:
                        first += 1
                    while first < second and nums[second] == nums[second - 1]:
                        second -= 1
                    first += 1
                    second -= 1
                elif nums[first] + nums[second] > new_target:
                    second -= 1
                elif nums[first] + nums[second] < new_target:
                    first += 1
        return end_result


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))