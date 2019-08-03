# -*- coding:utf-8 -*-

'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
'''

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code hereclassify_many
        if matrix is None or rows < 1 or cols < 1 or path is None:
            return False

        new_matrix = []
        matrix = [i for i in matrix]
        for i in range(0, rows):
            l = []
            for j in range(0, cols):
                l.append(matrix.pop(0))
            new_matrix.append(l)
        visited = [[False for j in range(0, cols)] for i in range(0, rows)]

        path_length = 0

        for row in range(0, rows):
            for col in range(0, cols):
                if self.hasPathCore(new_matrix, rows, cols, row, col, path, path_length, visited):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, path_length, visited):
        if path_length == len(path):
            return True

        has_path = False
        if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row][col] == path[path_length] and \
                visited[row][col] is False:
            path_length += 1
            visited[row][col] = True

            has_path = self.hasPathCore(matrix, rows, cols, row, col - 1, path, path_length,
                                        visited) or self.hasPathCore(matrix, rows, cols, row, col + 1, path,
                                        path_length, visited) or self.hasPathCore(matrix, rows, cols, row + 1,
                                        col, path, path_length, visited) or self.hasPathCore(
                                        matrix, rows, cols, row - 1, col, path, path_length, visited)

            if has_path is False:
                path_length -= 1
                visited[row][col] = False

        return has_path