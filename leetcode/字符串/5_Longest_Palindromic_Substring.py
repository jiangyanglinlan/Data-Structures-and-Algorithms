class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len_str = ''
        for i in range(0, len(s)):
            left = i
            right = i
            while left > 0 and right < len(s) - 1 and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1

            if right - left + 1 > len(max_len_str):
                max_len_str = s[left: right + 1]

        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                left = i
                right = i + 1
            while left > 0 and right < len(s) - 1 and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1

            if right - left + 1 > len(max_len_str):
                max_len_str = s[left: right + 1]

        return max_len_str


s = Solution()
test_str = "babaabad"
print(s.longestPalindrome(test_str))