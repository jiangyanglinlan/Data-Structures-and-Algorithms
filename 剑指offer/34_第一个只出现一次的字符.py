# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        d = {}
        for i in xrange(0, len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1

        for i in xrange(0, len(s)):
            if d[s[i]] == 1:
                return i
        return -1