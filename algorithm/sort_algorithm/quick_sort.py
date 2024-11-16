'''
快速排序的核心思想是找一个数作标准数，将比标准数大的数放在后面，比标准数小的数放在前面
然后将大的部分和小的部分都按相同的方法处理，如此递归下去就可以完成排序
'''


def quickSort(nums, start, end):
    if start < end:    # 如果起始位置小于终止位置
        standard = nums[start]
        low = start    # 记录左右下标
        high = end
        while low < high:
            while low < high and nums[high] >= standard:
                high -= 1
            nums[low] = nums[high]    # 将右下标的数存入左下标的位置
            while low < high and nums[low] <= standard:    # 从左向右找比标准数小的数   
                low += 1
            nums[high] = nums[low]    # 将左下标的数存入右下标的位置
        nums[low] = standard    # 将标准数存入最终位置  
        quickSort(nums, start, low-1)
        quickSort(nums, low+1, end)
# 测试
if __name__ == '__main__':
    nums = [30, 24, 5, 18, 36, 9, 17, 28, 45, 6, 49, 25, 2, 12]
    print('排序前：', nums)
    quickSort(nums, 0, len(nums)-1)
    print('排序后：', nums)


