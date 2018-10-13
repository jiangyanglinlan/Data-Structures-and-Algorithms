class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1

        if nums[0] > target:
            return 0

        if nums[end] < target:
            return end + 1

        while start + 1 < end:
            mid = start + (int)((end - start) / 2)
            if target > nums[mid]:
                start = mid
            elif target < nums[mid]:
                end = mid
            else:
                return mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return start + 1