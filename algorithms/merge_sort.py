def merge_sort(nums):
    temp = [None for i in range(0, len(nums))]
    helper(nums, 0, len(nums) - 1, temp)


def helper(nums, start, end, temp):
    if start >= end:
        return

    left = start
    right = end
    mid = start + int((end - start) / 2)

    helper(nums, start, mid, temp)
    helper(nums, mid + 1, end, temp)
    merge(nums, start, mid, end, temp)


def merge(nums, start, mid, end, temp):
    left = start
    right = mid + 1
    index = start

    while left <= mid and right <= end:
        if nums[left] < nums[right]:
            temp[index] = nums[left]
            index += 1
            left += 1
        else:
            temp[index] = nums[right]
            index += 1
            right += 1

    while left <= mid:
        temp[index] = nums[left]
        index += 1
        left += 1

    while right <= end:
        temp[index] = nums[right]
        index += 1
        right += 1

    for i in range(start, end + 1):
        nums[i] = temp[i]


if __name__ == '__main__':
    nums = [3, 4, 2, 3, 6, 8, 14, 31]
    merge_sort(nums)
    print(nums)