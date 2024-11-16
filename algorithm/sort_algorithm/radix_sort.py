'''
基数排序算法是一种特殊的排序算法，不需要元素间比较大小，也不用元素交换位置，
只需将元素按规则进行分类即可完成排序
'''


def radixSort(nums):
    maxlen = len(str(max(nums)))    # 获取最大长度
    queues = [[] for _ in range(10)]    # 创建10个空列表
    for i in range(maxlen):    # 根据最大长度遍历轮数
        for num in nums:
            try:
                queueIndex = int(str(num)[i])
            except:    # 如果索引越界，则默认索引为0
                queueIndex = 0
            queues[queueIndex].append(num)
        nums.clear()
        for queue in queues:
            nums.extend(queue)    # 一次添加所有队列的元素到原列表中
            queue.clear()
# 测试
if __name__ == '__main__':
    import random
    nums = list(range(10))
    random.shuffle(nums)
    print('排序前:', nums)
    radixSort(nums)
    print('排序后:', nums)






