'''
二分查找也称折半查找，要求被查找序列有序，先对比目标序列中间值和目标值的大小
若中间元素等于目标值，则查找成功；若中间元素大于目标值，则在左半部分继续查找；若中间元素小于目标值，则在右半部分继续查找。
'''

def binarySearch(nums, value):
    low, mid, high = 0, len(nums) // 2, len(nums) - 1    #初始化最低索引，中间索引，最高索引
    while low < high:
        if nums[mid] == value:    # 如果中间元素等于目标值，则返回True
            print(f"要查找值的索引为：{mid}")
            return True
        elif nums[mid] > value:    # 如果中间元素大于目标值，则在左半部分继续查找
            high = mid - 1
        else:
            low = mid + 1    # 如果中间元素小于目标值，则在右半部分继续查找
    return False
# 测试
if __name__ == '__main__':
    print(binarySearch([1, 3, 5, 7, 12, 20, 15, 6], 12))
