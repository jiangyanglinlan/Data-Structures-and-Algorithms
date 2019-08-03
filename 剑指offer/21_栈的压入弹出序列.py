# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        s = []
        while len(popV) > 0:
            pop_num = popV.pop(0)
            if pop_num not in pushV and pop_num not in s:
                return False
            elif pop_num not in s:
                x = 0
                for i in pushV:
                    x += 1
                    s.append(i)
                    if i == pop_num:
                        s.pop()
                        break
                for i in xrange(0, x):
                    pushV.pop(0)
            elif pop_num in s:
                pn = s.pop()
                if pn != pop_num:
                    return False
        return True