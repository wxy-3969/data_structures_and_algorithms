'''
选择排序的基本思想是在未排序的序列中选择一个最小的数，将其放在已排好序的序列的末尾
假设待排序的序列长度为m,则需选m-1次,如n表示已经选择过的次数择第n+1次选择需比较m-n-1次
'''


def selectSort(nums):
    for i in range(0, len(nums)):    # 外层循环控制选择的次数
        minIndex = i    # 记录未排序中最小的数的下标，初始值为当前遍历的下标
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minIndex]:    # 如果找到一个比已经记录的最小数下标的数还小的
                minIndex = j    # 记录最小数的下标
        if minIndex != i:    # 如果最小数的下标不是当前遍历的下标
            temp = nums[i]    # 交换最小数和当前遍历的数
            nums[i] = nums[minIndex]
            nums[minIndex] = temp
# 测试
list = [1, 3, 2, 4, 5, 6, 7, 8, 9, 0]
selectSort(list)
print(list)




