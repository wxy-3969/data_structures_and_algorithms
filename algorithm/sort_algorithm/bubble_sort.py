import time
'''
冒泡排序是一种交换排序，即如果前面的数比后面的数大就交换位置
在冒泡排序过程中,每一轮比较出一个最大的数放在序列的最后,使用m表示元素的个数,那么需要进行m-1轮比较
用n表示已经进行过的轮数,则每一轮需要比较的次数为m-n-1
'''
def  bubbleSort(nums):
    for i in range(0,len(nums)-1):    # 外层for循环表示进行比较的轮数，为len(nums)-1
        for j in range(0,len(nums)-i-1):    # 内存for循环表示每一轮比较的次数，为len(nums)-已执行轮数-1
            print("第%d轮第%d次" % (i+1,j+1),end = "\t")    # 如果前面的数比后面的数大，就交换位置
            if nums[j] > nums[j+1]:
                print("%d和%d交换位置" % (nums[j],nums[j+1]),end = "\t")
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
            else:
                print("%d比%d小,不交换位置" % (nums[j],nums[j+1]),end = "\t")
            print(nums)
        print("第%d轮排序结果" % (i+1), nums)     
# 测试
if __name__ == '__main__':
    nums = [10, 12, 22, 30, 5, 60, 20, 66, 102, 33, 0, 6, 18]
    print("排序前：",nums)
    start_time = time.time()
    print("开始时间：",start_time)
    bubbleSort(nums)
    end_time = time.time()


'''
optimize1
如果某一轮未发生位置交换，说明排序已经完成，可以提前结束排序
'''
def bubbleSort(nums):
    for i in range(0,len(nums)-1):    # 外层for循环表示进行比较的轮数，为len(nums)-1
        sorted=True
        for j in range(0,len(nums)-i-1):    # 内存for循环表示每一轮比较的次数，为len(nums)-已执行轮数-1
            print("第%d轮第%d次" % (i+1,j+1),end = "\t")
            if nums[j]>nums[j+1]:    # 如果前面的数比后面的数大，就交换位置
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
                sorted=False    # 发生位置交换，说明排序未结束
            else:
                print("%d比%d小,不交换位置" % (nums[j],nums[j+1]),end = "\t")  
            print(nums)
        print("第%d轮排序结果" % (i+1), nums)
        if sorted:    # 判断本轮位置是否有交换
            return
# 测试
if __name__ == '__main__':
    nums = [10, 12, 22, 30, 5, 60, 20, 66, 102, 33, 0, 6, 18]
    print("排序前：",nums)
    start_time = time.time()
    print("开始时间：",start_time)
    bubbleSort(nums)
    end_time = time.time()


'''
optimize2
当某一轮中某一次位置交换后，下一次开始均为发生位置交换，说明后面排序已经完成，那么下一轮只需比较前面的元素即可
'''
def bubbleSort(nums):
    r = range(0, len(nums) - 1)
    for i in range(0, len(nums) - 1):    # 外层for循环表示进行比较的轮数，为len(nums)-1
        sorted = True    # 每一轮开始时，都认为排序未完成
        for j in r:    # 内存for循环表示每一轮比较的次数，为len(nums)-已执行轮数-1
            print("第%d轮第%d次" % (i + 1, j + 1), end="\t")
            if nums[j] > nums[j + 1]:    # 如果前面的数比后面的数大，就交换位置
                print("%d和%d交换位置" % (nums[j], nums[j + 1]), end="\t")
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
                sorted = False    # 发生位置交换，说明排序未结束
                lastChange = j    # 记录最后一次交换的位置
            else:
                print("%d比%d小,不交换位置" % (nums[j], nums[j + 1]), end="\t")
            print(nums)
        print("第%d轮排序结果" % (i + 1), nums)
        if sorted:    # 判断本轮位置是否有交换# 判断本轮位置是否有交换
            return
        print("最后一次交换的位置是：",lastChange)
        r = range(0, lastChange)    # 改变下一次比较的范围
# 测试
if __name__ == '__main__':
    nums = [10, 12, 22, 30, 5, 60, 20, 66, 102, 33, 0, 6, 18]
    print("排序前：",nums)
    start_time = time.time()
    print("开始时间：",start_time)
    bubbleSort(nums)
    end_time = time.time()




