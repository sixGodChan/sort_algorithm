# 二分查找：方式一

def bin_search(data_set, value):
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low + high) // 2
        if data_set[mid] == value:
            return mid
        elif data_set[mid] > value:
            high = mid - 1
        else:
            low = mid + 1


# p = bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 8)
# print(p)


# 二分查找 递归

def bin_search2(data_set, value, low, high):
    while low <= high:
        mid = (low + high) // 2
        if data_set[mid] == value:
            return mid
        elif data_set[mid] < value:
            return bin_search2(data_set, value, mid + 1, high)
        else:
            return bin_search2(data_set, value, low, mid - 1)


# list = [i for i in range(88, 999)]
# p = bin_search2(list, 767, 0, len(list))
# print(p)

# 二分查找 练习

li = [
    {'id': 1008, 'name': "张三", 'age': 20},
    {'id': 1006, 'name': "李四", 'age': 25},
    {'id': 1004, 'name': "王五", 'age': 23},
    {'id': 1007, 'name': "赵六", 'age': 33}
]


def bin_search_p(data_set, value):
    low = 0
    high = len(data_set)
    while low <= high:
        mid = (low + high) // 2
        if data_set[mid]['id'] == value:
            return data_set[mid]
        elif data_set[mid]['id'] > value:
            high = mid - 1
        else:
            low = mid + 1


c = bin_search_p(li, 1002)
print(c)


# 冒泡排序 练习

def bubble_sort_p(data_set):
    for i in range(len(data_set) - 1):
        for j in range(len(data_set) - i - 1):
            if data_set[j]['id'] > data_set[j + 1]['id']:
                data_set[j], data_set[j + 1] = data_set[j + 1], data_set[j]

bubble_sort_p(li)
print(li)
