class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + int((end - start) / 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[end]:
                if nums[mid] <= target and target <= nums[end]:
                    start = mid
                else:
                    end = mid
            else:
                if nums[mid] >= target and target >= nums[start]:
                    end = mid
                else:
                    start = mid

        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        return -1


s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))
print(s.search([4,5,6,7,0,1,2], 3))