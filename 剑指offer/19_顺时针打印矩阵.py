# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if matrix is None:
            return []

        cols = len(matrix[0])
        rows = len(matrix)
        start = 0
        result = []

        while cols > start * 2 and rows > start * 2:
            self.print_matrix_in_circle(matrix, cols, rows, start, result)
            start += 1

        return result

    def print_matrix_in_circle(self, matrix, cols, rows, start, result):
        end_x = cols - 1 - start
        end_y = rows - 1 - start

        # 从左到右打印一行
        for i in xrange(start, end_x + 1):
            number = matrix[start][i]
            result.append(number)

        # 从上到下打印一列
        if start < end_y:
            for i in xrange(start + 1, end_y + 1):
                number = matrix[i][end_x]
                result.append(number)

        # 从右到左打印一行
        if start < end_x and start < end_y:
            for i in xrange(end_x - 1, start - 1, -1):
                number = matrix[end_y][i]
                result.append(number)

        # 从下到上打印一列
        if start < end_x and start < end_y - 1:
            for i in xrange(end_y - 1, start, -1):
                number = matrix[i][start]
                result.append(number)
