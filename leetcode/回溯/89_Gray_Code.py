'''
这题做了很久, WA 了 n 发。
起初的想法是用回溯法把一个二进制数字中某些位为 1 的所有情况标记出来, 然后算值,
但是这个方法做出的答案不符合 两个连续的数值仅有一个位数的差异 的要求。
随后看到题解, 发现格雷码可以直接由二进制转换, 但这是提前知晓格雷码的情况下才能想出来的做法, 所以没有采用。
最后看到别人博客发现规律, 格雷码的 n 位数可以由第 n - 1 位推出来。
n 位数 = ['0' + 第 n - 1 位数的所有位数] + ['1' + 第 n - 1 位数逆序的所有位数]
于是用递归写出来了, 代码如下: 
'''

class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        result = ['0', '1']
        self.helper(result, n-1)
        return self.process_result(result)

    def helper(self, result, n):
        if n == 0:
            return
        tmp = result.copy()
        for i in range(0, len(result)):
            result[i] = '0' + tmp[i]
        for i in range(len(result)-1, -1, -1):
            result.append("1" + tmp[i])
        self.helper(result, n-1)

    def process_result(self, result):
        for i in range(0, len(result)):
            result[i] = int(result[i], 2)
        return result


s = Solution()
print(s.grayCode(0))