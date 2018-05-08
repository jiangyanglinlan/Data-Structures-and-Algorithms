import random


'''
选择排序的思想是每次找出列表元素中最小(大)的那一个, 存放到列表的起始位置,
然后, 再从剩余未排序元素中继续寻找最小(大)元素, 然后放到列表中已排序序列的末尾。
每次遍历找出列表中元素最小(大)的元素, 需要的时间为 O(n),
对于这种时间为 O(n), 的操作, 需要执行 n 次, 所以选择排序的时间复杂度为 O(n²)
'''


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


def find_smallest(arr):
    smallest = arr[0] # 存储最小的值
    smallest_index = 0 # 存储最小元素的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


if __name__ == '__main__':
    l = random_int_list(1,10000, 20)
    print(selection_sort(l))
