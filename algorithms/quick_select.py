import random


def quick_select(start, end, k, nums):
    if start == end:
        return nums[start]

    index = partition(nums, start, end)
    num = index - start + 1

    if k == num:
        return nums[index]
    elif k > num:
        return quick_select(index + 1, end, k - num, nums)
    else:
        return quick_select(start, index - 1, k, nums)


def partition(nums, start, end):
    pivot = nums[start]
    while start < end:
        while start < end and nums[end] >= pivot:
            end -= 1
        nums[start] = nums[end]
        while start < end and nums[start] <= pivot:
            start += 1
        nums[end] = nums[start]
    nums[start] = pivot
    return start


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(nums)
    result = quick_select(0, len(nums) - 1, 5, nums)
    print(result)