'''
这道题目不需要返回值, 检测的 nums1 的值, 所以需要新建一个数组保存原来的 nums1。代码如下, 时间复杂度为 O(n+m)。
'''
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        new_nums1 = [i for i in nums1]
        index = 0
        index1 = 0
        index2 = 0
        while index1 < m and index2 < n:
            if new_nums1[index1] < nums2[index2]:
                nums1[index] = new_nums1[index1]
                index += 1
                index1 += 1
            else:
                nums1[index] = nums2[index2]
                index += 1
                index2 += 1
        i = index1
        while i < m:
            nums1[index] = new_nums1[i]
            index += 1
            i += 1
        i = index2
        while i < n:
            nums1[index] = nums2[i]
            index += 1
            i += 1
        return nums1

s = Solution()
a = s.merge([4,5,6,0,0,0], 3, [1, 2, 3], 3)
print(a)
