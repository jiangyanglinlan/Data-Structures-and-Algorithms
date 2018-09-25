class Solution:
    def permute(self, nums):
        result = []
        if nums is None or len(nums) == 0:
            return []
        l = []
        self.permute_helper(result, l, nums)
        return result


    def permute_helper(self, result, l, nums):
        if len(l) == len(nums):
            new_list = l.copy()
            result.append(new_list)
        for i in range(0, len(nums)):
            if nums[i] in l:
                continue
            l.append(nums[i])
            self.permute_helper(result, l, nums)
            l.pop(len(l) - 1)


s = Solution()
print(s.permute([1, 2, 3]))