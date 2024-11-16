'''
归并排序的核心思想是使用递归方法将待排序序列分隔成两个只有1个元素的部分
然后分别按顺序对比两部分中的元素，将其归并为一个有序的序列
'''


def merge(left, right):
    r, l = 0, 0    # 记录下标
    temp  =[]
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            temp.append(left[l])    # 将左边列表的数存入新列表
            # 下标+1
            l += 1
        else:
            # 将右边列表的数存入新列表
            temp.append(right[r])
            # 下标+1
            r += 1
    temp += left[l:]    # 处理多余的数据
    temp += right[r:]
    return temp


def mergeSort(nums):
    if len(nums) <= 1:    # 结束递归条件，若只有一个数，不在循环
        return nums
    num = len(nums) // 2    # 将列表分为两个部分
    left = mergeSort(nums[:num])    # 左右部分
    right = mergeSort(nums[num:])
    return merge(left, right)    # 递归处理
# 测试
if __name__ == '__main__':
    print(f"排序前:{([3, 9, 11, 22, 1, 5, 10])}")
    print(f"排序后:{mergeSort([3, 9, 11, 22, 1, 5, 10])}")
