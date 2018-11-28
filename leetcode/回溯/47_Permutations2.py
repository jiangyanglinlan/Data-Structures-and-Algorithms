class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if nums is None or len(nums) == 0:
            return []
        l = []
        used = {}
        nums.sort()
        self.permute_helper(result, l, nums, used)
        return result

    def permute_helper(self, result, l, nums, used):
        print(l)
        if len(l) == len(nums):
            new_list = l.copy()
            result.append(new_list)
            return

        for i in range(0, len(nums)):
            if i in used.keys() and used[i] == 1:
                continue
            if i > 0 and nums[i-1] == nums[i] and used[i-1] == 0:
                continue
            l.append(nums[i])
            used[i] = 1
            self.permute_helper(result, l, nums, used)
            used[i] = 0
            l.pop(len(l) - 1)


s = Solution()
print(s.permute([1, 1, 2]))