# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        first_step = 1
        second_step = 2

        if number == 1:
            return first_step

        if number == 2:
            return second_step

        while number > 3:
            temp = second_step
            second_step += first_step
            first_step = temp
            number -= 1
        result = first_step + second_step
        return result
