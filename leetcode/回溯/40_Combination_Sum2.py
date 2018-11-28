class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        l = []
        candidates.sort()
        self.helper(result, l, candidates, target, 0)
        return result

    def helper(self, result, l, candidates, target, pos):
        if target == 0:
            result.append(l.copy())
        elif target < 0:
            return
        for i in range(pos, len(candidates)):
            if i != pos and candidates[i] == candidates[i-1]:
                continue
            l.append(candidates[i])
            self.helper(result, l, candidates, target - candidates[i], i + 1)
            l.pop(len(l)-1)


s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))
