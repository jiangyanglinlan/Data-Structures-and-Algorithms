# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        x_len = len(array) - 1
        y_len = len(array[0]) - 1
        start_x = x_len
        start_y = 0

        end_x = 0
        end_y = y_len

        while start_x >= end_x and end_y >= start_y:
            if target == array[start_x][start_y]:
                return True
            if target == array[end_x][end_y]:
                return True

            if target > array[start_x][start_y]:
                start_y += 1
            else:
                start_x -= 1

            if target > array[end_x][end_y]:
                end_x += 1
            else:
                end_y -= 1
        return False