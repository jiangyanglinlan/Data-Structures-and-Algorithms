class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if nums is None or len(nums) == 0:
            return result
        l = []
        nums.sort()
        self.subset_help(result, l, nums, 0)
        return result

    def subset_help(self, result, l, nums, pos):
        new_list = l.copy()
        result.append(new_list)
        print(new_list)
        for i in range(pos, len(nums)):
            if i != pos and nums[i] == nums[i-1]:
                continue
            l.append(nums[i])
            self.subset_help(result, l, nums, i+1)
            l.pop(len(l)-1)

s = Solution()
print(s.subsetsWithDup([1, 2, 2]))
print('-------------')
print(s.subsetsWithDup([4, 4, 4, 1, 4]))
