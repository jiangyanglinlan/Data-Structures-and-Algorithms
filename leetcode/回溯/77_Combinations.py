class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        l = []
        s = [i for i in range(1, n + 1)]
        self.helper(result, l, s, k, 0)
        return result

    def helper(self, result, l, s, k, pos):
        if len(l) == k:
            result.append(l.copy())
            return
        for i in range(pos, len(s)):
            l.append(s[i])
            self.helper(result, l, s, k, i + 1)
            l.pop(len(l) - 1)


s = Solution()
print(s.combine(4, 2))

