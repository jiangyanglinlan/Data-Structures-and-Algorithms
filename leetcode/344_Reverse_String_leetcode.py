class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return s[::-1] 皮一下
        start = 0
        end = len(s) - 1
        l = list(s)
        while start < end:
            self.swap(l, start, end)
            start += 1
            end -= 1
        result_str = ''.join(i for i in l)
        return result_str

    def swap(self, s, start, end):
        s[start], s[end] = s[end], s[start]


s = Solution()
print(s.reverseString('A man, a plan, a canal: Panama'))



