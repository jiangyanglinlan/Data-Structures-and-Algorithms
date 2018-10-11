class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n

        while start + 1 < end:
            mid = start + (int)(end - start)/2
            if isBadVersion(mid) is True:
                end = mid
            else:
                start = mid

        if isBadVersion(start) is True:
            return start

        if isBadVersion(end) is True:
            return end

        return -1