'''
堆排序是选择排序的一种，核心思想是将待排序序列放入大顶堆或小顶堆中，再将堆顶元素放到整个序列最后的已经排好序部分的最前面
然后重新调整待排序部分为大顶堆，直到排序完成
'''


def maxHeap(nums, size, parent):
    lefNode = parent * 2 + 1    # 获取parent的左右子节点
    right =  parent * 2 + 2
    max = parent    # 默认父节点最大
    if lefNode < size and nums[lefNode] > nums[max]:    # 依次判断左右节点，找到最大数的索引
        max = lefNode
    if right < size and nums[right] > nums[max]:
        max = right
    if max != parent:    # 若最大的节点在判断完以后不是父节点，说明最大的节点是左节点或右节点
        nums[parent], nums[max] = nums[max], nums[parent]
        maxHeap(nums, size, max)    # 递归处理交换后的子树
    else:
        return
        
        
def heapSort(nums):
    last = len(nums) - 1
    parent = len(nums) // 2 - 1    # 最后一个父节点的索引
    while parent >= 0:    # 从最后一个父节点开始，依次向前
        maxHeap(nums, len(nums), parent)
        parent -= 1
    i = last    # 从最后一个元素开始
    while i > 0:
        nums[i], nums[0] = nums[0], nums[i]    # 将第0个元素与最后一个元素交换，即把最大的元素放到最后面
        maxHeap(nums, i, 0)    # 重新调整堆
        i -= 1
    return nums
# 测试
if __name__ == '__main__':
    nums = [3, 5, 4, 6, 8, 7, 9, 1, 2]
    print(f"排序前:{nums}")
    print(f"排序后:{heapSort(nums)}")


