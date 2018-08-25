'''
这道题就是两数之和的简化版(数组是有序的)，我用的两根指针的方法, 时间复杂度为 O(n):
'''
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        start = 0
        end = len(numbers) - 1
        while start < end:
            if numbers[start] + numbers[end] == target:
                result.append(start + 1)
                result.append(end + 1)
                return result
            if numbers[start] + numbers[end] < target:
                start += 1
            if numbers[start] + numbers[end] > target:
                end -= 1
        return result


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))

