class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        l = []
        self.helper(result, l, s, 0)
        return result

    def helper(self, result, l, s, pos):
        if pos == len(s):
            new_list = l.copy()
            result.append(new_list)
        for i in range(pos + 1, len(s)+1):
            prefix = s[pos:i]
            if not self.is_palindrome(prefix):
                continue
            l.append(prefix)
            self.helper(result, l, s, i);
            l.pop(len(l) - 1)

    def is_palindrome(self, s):
        if s is None:
            return False
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


s = Solution()
print(s.partition("aab"))