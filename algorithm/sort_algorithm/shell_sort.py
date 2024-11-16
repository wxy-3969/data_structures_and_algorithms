# 希尔排序也称为最小增量排序，是插入排序的改进可以将后面的较小得数快速换到较靠前的位置
# 核心思想是将待排序序列按步长分为若干组，每轮分别排序组内的元素，一轮结束后各组内的元素已经排好序
# 然后缩小步长重新分组排序直到步长为1，排序完成


def shellSort(nums):
    step = len(nums) // 2
    while step > 0:
        for i in range(step, len(nums)):    # 从每一组的第二个元素开始遍历，所以初始值为第1组的第2个元素,即step值
            temp = nums[i]    # 临时变量用于存第i个数
            j = i - step
            while j >= 0 and nums[j] > temp:    # 遍历本组中前面的所有元素，若本组中前面的数更大
                nums[j + step] = nums[j]    # 前面的元素向后移动一个步长
                j -= step
            nums[j + step] = temp    # 循环结束后，说明有一个更小的，将临时变量存入j的组的后一个元素,即j+step
        step //= 2
# 测试
if __name__ == '__main__':
    nums = [44, 50, 77, 96, 32, 39, 82, 78, 90, 18, 34, 56, 71, 99, 12]
    print("原始数据：", nums)
    shellSort(nums)
    print("排序结果：", nums)

