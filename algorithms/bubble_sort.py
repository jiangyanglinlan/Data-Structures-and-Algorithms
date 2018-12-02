def bubble_sort(nums):
    length = len(nums)

    for i in range(0, length):
        for j in range(1, length - i):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]


if __name__ == '__main__':
    nums = [3, 4, 2, 3, 6, 8, 14, 31]
    bubble_sort(nums)
    print(nums)