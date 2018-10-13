class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x < 0:
            return -1
        start = 1
        end = x

        while start + 1 < end:
            mid = start + int((end - start) / 2)
            if mid < x / mid:
                start = mid
            elif mid > x / mid:
                end = mid
            else:
                return mid

        if end <= x / end:
            return end
        return start