class Solution:
    @staticmethod
    def int_overflow(val):
        '''
        Python 中整型左移不会溢出, 需要额外处理一下
        :param val:
        :return:
        '''
        maxint = 2147483647
        if not -maxint-1 <= val <= maxint:
            val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
        return val

    def singleNumber(self, nums):
        bit_num = [0] * 32
        for i in range(0, len(nums)):
            current_num = nums[i]
            compare = 1
            for j in range(len(bit_num) - 1, -1, -1):
                if (current_num & compare) != 0:
                    bit_num[j] += 1
                compare <<= 1
        res = 0
        compare = 1
        for i in range(len(bit_num) - 1, -1, -1):
            if bit_num[i] % 3 != 0:
                res ^= compare
            compare = self.int_overflow(compare << 1)
        return res


def ensure_equal(a, b, message):
    if a != b:
        print('{}, ({}) 不等于 ({})'.format(message, a, b))
    else:
        print('测试成功')


if __name__ == '__main__':
    s = Solution()
    ensure_equal(s.singleNumber([2,2,3,2]), 3, 'test1 error')
    ensure_equal(s.singleNumber([0,1,0,1,0,1,99]), 99, 'test2 error')
    ensure_equal(s.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]), -4, 'test3 error')