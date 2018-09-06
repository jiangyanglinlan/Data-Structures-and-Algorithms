class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if nums is None or len(nums) == 0:
            return result
        l = []
        l.sort()
        self.subset_help(result, l, nums, 0)
        return result

    def subset_help(self, result, l, nums, pos):
        new_list = l.copy()
        result.append(new_list)
        for i in range(pos, len(nums)):
            l.append(nums[i])
            self.subset_help(result, l, nums, i+1)
            l.pop(len(l)-1)

s = Solution()
print(s.subsets([1, 2, 3]))