'''
直接选择排序的思想是将要排序的序列分成两部分，前面部分是排好序的，后半部分是未排序的
每轮从未排序的部分中选出一个数然后通过比较大小将它插入指定位置
每插入一个数，排好序的部分增加一个数，未排序的半部分减少一个数，直到所有序列排序完成
可以认为第0个数是排好序的，只需要从第一个数开始，把每一个数往前面的序列中插入，所以，如果元素个数为n，那么需要进行n-1次插入
'''


def insertSort(nums):
    for i in range(1, len(nums)):    # 从第二个数开始，往前面的序列中插入
        temp = nums[i]    # 将第i个数存入临时变量中
        j = i - 1    # 变量j用于记录和临时变量交换的位置，从i的前一个位置开始比较
        while j >= 0 and nums[j] > temp:    # 若未超出范围且第j个元素大于临时变量中的数
            nums[j + 1] = nums[j]    # 将第j个元素往后移
            j -= 1
        nums[j + 1] = temp    # 将临时变量存入最后一个未移动的位置的后一个位置
# 测试
list = [10, 20, 15, 18, 16, 17, 19, 11, 13, 12, 14]
insertSort(list)
print(list)