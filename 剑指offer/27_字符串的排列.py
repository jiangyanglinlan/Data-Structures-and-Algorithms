# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) == 0 or ss is None:
            return []
        l = ''
        result = []
        used = {}
        self.helper(ss, l, result, used)
        return result

    def helper(self, ss, l, result, used):
        if len(l) == len(ss):
            new_list = l[:]
            result.append(new_list)
            return
        for i in range(0, len(ss)):
            if i in used and used[i] == 1:
                continue
            if i > 0 and ss[i - 1] == ss[i] and used[i - 1] == 0:
                continue
            l += ss[i]
            used[i] = 1
            self.helper(ss, l, result, used)
            l = l[:-1]
            used[i] = 0