class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1

        while(start + 1 < end):
            mid = start + int((end - start) / 2)
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid

        if nums[start] < nums[end]:
            return nums[start]

        return nums[end]


s = Solution()
# print(s.findMin([3,4,5,1,2]))
# print(s.findMin([4,5,6,7,0,1,2]))
print(s.findMin([5, 1, 2, 3, 4]))
print(s.findMin([4, 5, 1, 2, 3]))