def insert_sort(nums):
    for j in range(1, len(nums)):
        key = nums[j]
        i = j - 1
        while i >= 0 and nums[i] > key:
            nums[i + 1] = nums[i]
            i -= 1

        nums[i + 1] = key


if __name__ == '__main__':
    nums = [3, 4, 2, 3, 6, 8, 14, 31]
    insert_sort(nums)
    print(nums)