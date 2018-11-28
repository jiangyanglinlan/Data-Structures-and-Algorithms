# 这道字符串匹配的题目有两种方法:

# 暴力(常规方法, 较慢):
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        haystack_len = len(haystack)
        needle_len = len(needle)
        for i in range(haystack_len):
            if haystack[i: i+needle_len] == needle:
                return i
        return -1


# KMP
# 时间复杂度为 O(n+m)		
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        lps = self.compute_temporary_array(needle)
        i = 0
        j = 0
        haystack_len = len(haystack)
        needle_len = len(needle)
        while i < haystack_len and j < needle_len:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
            if j == needle_len:
                return i - needle_len
        return -1
    
    
    def compute_temporary_array(self, pattern):
        '''
        :param pattern: str 
        :return: str
        '''
        pattern_len = len(pattern)
        lps = [i for i in range(0, pattern_len)]
        index = 0
        i = 1
        while i < pattern_len:
            if pattern[i] == pattern[index]:
                lps[i] = index + 1
                index += 1
                i += 1
            else:
                if index != 0:
                    index = lps[index-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

s = Solution()
print(s.strStr('hello', 'll'))