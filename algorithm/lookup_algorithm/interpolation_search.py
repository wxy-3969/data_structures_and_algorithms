'''
插值查找通过目标元素在目标序列的大小分布情况确定中间位置
'''
def insertSearch(nums, value):
    low, high = 0, len(nums) - 1    # 初始化最低索引和最高索引
    count = 1
    while low <= high:
        print(f"第{count}次查询")
        count += 1
        mid = low + int((value - nums[low]) / (nums[high] - nums[low]) * (high - low))
        if nums[mid] == value:    # 如果中间位置的元素等于目标值，则返回中间位置
            return mid
        elif nums[mid] > value:   # 如果中间位置的元素大于目标值，搜索左边
            high = mid - 1
        else:
            low = mid + 1    # 否则搜索右边
    return -1
# 测试
if __name__ == '__main__':
    nums = [0, 1, 12, 45, 66, 67, 69, 73, 79, 89, 92, 100]
    print(insertSearch(nums, 89))

 




