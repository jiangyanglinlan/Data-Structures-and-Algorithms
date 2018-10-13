class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for nums in matrix:
            if nums is None or len(nums) == 0:
                continue
            start = 0
            end = len(nums) - 1

            while start + 1 < end:
                mid = start + (int)((end - start) / 2)

                if target > nums[mid]:
                    start = mid
                elif target < nums[mid]:
                    end = mid
                else:
                    return True

            if nums[start] == target:
                return True
            if nums[end] == target:
                return True

        return False

    def searchMatrix2(self, matrix, target):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        row = len(matrix)
        col = len(matrix[0])
        start = 0
        end = row * col - 1

        while start + 1 < end:
            mid = start + (int)((end - start) / 2)
            x = (int)(mid / col)
            y = mid % col

            if matrix[x][y] > target:
                end = mid
            elif matrix[x][y] < target:
                start = mid
            else:
                return True

        if matrix[int(start / col)][start % col] == target:
                return True

        if matrix[int(end / col)][end % col] == target:
                return True

        return False