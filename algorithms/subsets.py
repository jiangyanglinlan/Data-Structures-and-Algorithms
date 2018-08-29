'''
回溯法模板
'''
def subsets(nums):
    result = []
    if nums is None or len(nums) == 0:
        return result
    l = []
    l.sort()
    subset_help(result, l, nums, 0)
    return result


def subset_help(result, l, nums, pos):
    new_list = l.copy()
    result.append(new_list)
    for i in range(pos, len(nums)):
        l.append(nums[i])
        subset_help(result, l, nums, i+1)
        l.pop(len(l)-1)


print(subsets([1, 2, 3]))