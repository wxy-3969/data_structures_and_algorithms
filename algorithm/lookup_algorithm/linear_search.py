'''
线性查找也称顺序查找，适用于顺序存储或链式存储的线性
'''

def lineSearch(nums, value):
    for i in range(0, len(nums)):    # 遍历列表
        if nums[i] == value:    # 如果找到元素，返回其位置
            return i
    else:    # 如果没有找到元素，返回-1
        return -1
if __name__ == '__main__':
    nums = [23, 45, 67, 89, 90, 100]
    print("元素的位置是：",lineSearch(nums, 89))
