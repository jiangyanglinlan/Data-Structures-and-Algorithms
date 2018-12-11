class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        if x < 0:
            x = -x
            flag = True

        l = []
        while x > 9:
            l.append(x % 10)
            x = x // 10
        l.append(x)

        index = len(l) - 1

        while index >= 0:
            if l[index] != 0:
                break
            if l[index] == 0:
                l.pop()
            index -= 1

        l.reverse()
        num = 0
        for i in range(0, len(l)):
            num += l[i] * pow(10, i)

        if flag is True:
            num = -num
        if num < -pow(2, 31) or num > pow(2, 31) - 1:
            return 0
        return num
