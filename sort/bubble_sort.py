"""
冒泡排序(Bubble sort)

比较相邻元素：从列表的第一个元素开始，比较相邻的两个元素。

交换位置：如果前一个元素比后一个元素大，则交换它们的位置。

重复遍历：对列表中的每一对相邻元素重复上述步骤，直到列表的末尾。这样，最大的元素会被"冒泡"到列表的最后。

缩小范围：忽略已经排序好的最后一个元素，重复上述步骤，直到整个列表排序完成。

"""

def bubble_sort(arr):
    """
    :param arr: list
    :return: sorted list from small to big
    """
    n = len(arr)

    for i in range(n):
        # 交换标志
        flag = False
        for j in range(n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] = arr[j + 1], arr[j] #交换
                flag = True  #有交换发生，标志为真
            else:
                flag = False #没有交换， 标志为假

        # 没有交换，提前结束算法
        if not flag:
            break

    return arr



