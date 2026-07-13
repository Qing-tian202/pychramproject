import copy

global_list = [1, 2, 3]
global_dict = {'a': 10, 'b': 20}

def find_largest_palindrome_in_range(start, end):
    """
    数字转字符串，双指针法
    :param start:  起始
    :param end:  结束
    :return: 若有最大的回文数则返回该值，否则返回None
    """
    if start > end:
        return None

    for i in range(end, start-1, -1):
        i = str(i)
        n = len(i)
        flag = 1
        l, r = 0, n - 1
        if n == 1:
            return i
        else:
            if n % 2 == 1: #奇数
                while l <= r:
                    if i[l] != i[r]:
                        flag = 0
                        break
                    l += 1
                    r -= 1
            else:  #偶数
                while l < r:
                    if i[l] != i[r]:
                        flag = 0
                        break
                    l += 1
                    r -= 1

        if flag:
            return i

    return None


def find_largest_palindrome_in_range1(start, end):
    """
    反转数字法
    :param start:  起始
    :param end:  结束
    :return: 若有最大的回文数则返回该值，否则返回None
    """
    if start > end:
        return None

    for i in range(end, start-1, -1):
        oringe_num, reversed_num = i, 0
        while i > 0:
            reversed_num = i % 10 + reversed_num * 10
            i //= 10

        if reversed_num == oringe_num:
            return oringe_num

    return None

def process_elements(func, *args, **kwargs):
    """
    :param func: 回调函数名
    :param args:
    :param kwargs:
    :return:
    """
    area_list, area_dict = [item * 2 for item in args], {k : v + 5 for k, v in kwargs.items()}

    func(area_list, area_dict)


def print_result(modified_list, modified_dict):
    print("Modified List:", modified_list)
    print("Modified Dict:", modified_dict)


if __name__ == "__main__":
    print(find_largest_palindrome_in_range1(100, 200))
    print(find_largest_palindrome_in_range1(1, 10))
    print(find_largest_palindrome_in_range1(121, 121))
    print(find_largest_palindrome_in_range1(10, 5))

    process_elements(print_result,*copy.deepcopy(global_list), **copy.deepcopy(global_dict))