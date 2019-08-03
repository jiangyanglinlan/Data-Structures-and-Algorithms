# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        visited = [[False for j in xrange(0, cols)] for i in xrange(0, rows)]

        count = self.helper(threshold, rows, cols, 0, 0, visited)

        return count

    def helper(self, k, rows, cols, row, col, visited):
        count = 0
        if row >= 0 and row < rows and col >= 0 and col < cols and self.check(k, row, col) and visited[row][
            col] is False:
            visited[row][col] = True
            count = 1 + self.helper(k, rows, cols, row + 1, col, visited) \
                    + self.helper(k, rows, cols, row - 1, col, visited) \
                    + self.helper(k, rows, cols, row, col + 1, visited) \
                    + self.helper(k, rows, cols, row, col - 1, visited)
        return count

    def check(self, k, row, col):
        return (self.get_sum(row) + self.get_sum(col)) <= k

    def get_sum(self, num):
        result = 0
        while num > 0:
            result += num % 10
            num = num // 10
        return result