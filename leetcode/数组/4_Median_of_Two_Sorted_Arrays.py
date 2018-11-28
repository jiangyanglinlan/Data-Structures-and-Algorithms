'''
这道题目用二分查找的思想来做, 可以转换成求第 k 小(大)的数组,
如果 nums1[k/2-1] < nums2[k/2-1], 说明 nums1[k/2-1] 及其之前的元素肯定在 n所有元素的前 k-1 小元素中,
将 nums1 的从前 k/2 个元素开始切片后, 继续求 nums1 和 nums2 中的第 k-k/2 大的数, 直到一个序列长度为 0。
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)

        
        if (len1 + len2) % 2 == 1:
            k = (int)((len1 + len2) / 2 + 1)
            return self.find_k(nums1, nums2, k)
        else:
            k1 = (int)((len1 + len2) / 2)
            k2 = (int)((len1 + len2) / 2 + 1)
            return (self.find_k(nums1, nums2, k1)  + self.find_k(nums1, nums2, k2)) / 2
        
    def find_k(self, nums1, nums2, k):
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            return self.find_k(nums2, nums1, k)
        if len1 == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        p = (int)(min(k/2, len1))
        if nums1[p-1] <= nums2[k - p - 1]:
            return self.find_k(nums1[p:], nums2, k-p)
        else:
            return self.find_k(nums1, nums2[k-p:], p)


if __name__ == '__main__':
    s = Solution()
    l = s.findMedianSortedArrays([1, 3], [2])
    print(l)
