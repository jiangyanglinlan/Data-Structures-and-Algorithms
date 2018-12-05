import random


def quick_sort(array):
    if len(array) < 2:
        return array # 为空或者只包含一个元素的数组是"有序"的
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def quick_sort2(array, begin, end):
    if begin >= end:
        return
    pivot_postion = partition(array, begin, end)
    quick_sort2(array, begin, pivot_postion - 1)
    quick_sort2(array, pivot_postion + 1, end)


def partition(nums, begin, end):
    pivot = nums[begin]
    while begin < end:
        while begin < end and nums[end] >= pivot:
            end -= 1
        nums[begin] = nums[end]
        while begin < end and nums[begin] <= pivot:
            begin += 1
        nums[end] = nums[begin]
    nums[begin] = pivot
    return begin


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

	
if __name__ == '__main__':
    l = random_int_list(1,10000, 20)
    print(quick_sort(l))
    quick_sort2(l, 0, len(l) - 1)
    print(l)