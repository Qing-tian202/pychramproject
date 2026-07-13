"""
快速排序（Quick sort）

选择基准元素：从列表中选择一个元素作为基准（pivot）。选择方式可以是第一个元素、最后一个元素、中间元素或随机元素。

分区：将列表重新排列，使得所有小于基准元素的元素都在基准的左侧，所有大于基准元素的元素都在基准的右侧。基准元素的位置在分区完成后确定。

递归排序：对基准元素左侧和右侧的子列表分别递归地进行快速排序。

合并：由于分区操作是原地进行的，递归结束后整个列表已经有序。
"""

def quick_sort(arr):
    """
    :param arr: list
    :return: sorted list from small to big
    """
    if len(arr) <= 1:
        return arr

    # 选择基准元素（这里选择最后一个元素）
    pivot = arr[-1]
    # 分区：小于基准的元素放在左侧，大于基准的元素放在右侧
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    # 递归排序并合并
    return quick_sort(left) + [pivot] + quick_sort(right)