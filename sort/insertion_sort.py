"""
插入排序（Insertion Sort）

初始化：将列表分为已排序部分和未排序部分。初始时，已排序部分只包含第一个元素，未排序部分包含剩余元素。

选择元素：从未排序部分中取出第一个元素。

插入到已排序部分：将该元素与已排序部分的元素从后向前依次比较，找到合适的位置插入。

重复步骤：重复上述步骤，直到未排序部分为空，列表完全有序。
"""
def insertion_sort(arr):
    """
    :param arr: list
    :return: sorted list from small to big
    """
    n = len(arr)

    for i in range(1,n):
        temp = arr[i] #记录未排序序列的第一个元素
        j = i - 1 #已排序序列的结束位置

        while j >= 0 and temp < arr[j]: #寻找合适的位置
            arr[j + 1] = arr[j] #往后移动元素
            j -= 1

        arr[j + 1] = temp # 插入合适的位置

    return arr