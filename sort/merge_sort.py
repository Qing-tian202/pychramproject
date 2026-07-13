"""
归并排序（Merge sort）

分解（Divide）：将待排序的数组分成两个子数组，每个子数组包含大约一半的元素。

解决（Conquer）：递归地对每个子数组进行排序。

合并（Combine）：将两个已排序的子数组合并成一个有序的数组。
"""
def merge_sort(arr):
    """
    :param arr: list
    :return: sorted list from small to big
    """
    if len(arr) <= 1:
        return arr

    # 分解：将列表分成两半
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # 递归排序左半部分
    right_half = merge_sort(arr[mid:])  # 递归排序右半部分

    # 合并：将两个有序子列表合并
    return merge(left_half, right_half)

def merge(left, right):
    """
    :param arr: list
    :return: sorted list from small to big
    """
    sorted_arr = []
    i = j = 0

    # 比较两个子列表的元素，按顺序合并
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # 将剩余的元素添加到结果中
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr