"""
选择排序（Selection Sort）

初始化：将列表分为已排序部分和未排序部分。初始时，已排序部分为空，未排序部分为整个列表。

查找最小值：在未排序部分中查找最小的元素。

交换位置：将找到的最小元素与未排序部分的第一个元素交换位置。

更新范围：将未排序部分的起始位置向后移动一位，扩大已排序部分的范围。

重复步骤：重复上述步骤，直到未排序部分为空，列表完全有序。
"""
def selection_sort(arr):
    """
    :param arr: list
    :return: sorted list from small to big
    """
    n = len(arr)

    for i in range(n):
        min_index = i #最小值索引
        for j in range(i+1,n): #遍历剩余元素，寻找最小值
            if arr[j] < arr[min_index]:
                min_index = j #记录位置

        arr[i], arr[min_index] = arr[min_index], arr[i] #交换

    return arr