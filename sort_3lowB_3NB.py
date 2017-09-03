#
import random
import time

# 打乱列表

li1 = list(range(1000))
li2 = list(range(1000))
li3 = list(range(1000))
li4 = list(range(1000))
li5 = list(range(1000))
li6 = list(range(1000))
li8 = list(range(1000))
random.shuffle(li1)
random.shuffle(li2)
random.shuffle(li3)
random.shuffle(li4)
random.shuffle(li5)
random.shuffle(li6)
random.shuffle(li8)


# 装饰器

def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        x = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time %s secs." % (func.__name__, t2 - t1))
        return x

    return wrapper


# low B 三人组

# 冒泡排序 - 大的数到最后
@cal_time
def bubble_sort(data_set):
    for i in range(len(data_set) - 1):
        for j in range(len(data_set) - i - 1):
            if data_set[j] > data_set[j + 1]:
                data_set[j], data_set[j + 1] = data_set[j + 1], data_set[j]


# bubble_sort(li1)

# 冒泡排序 - 优化

@cal_time
def bubble_sort_v1(data_set):
    for i in range(len(data_set) - 1):
        exchange = True
        for j in range(len(data_set) - i - 1):
            if data_set[j] > data_set[j + 1]:
                data_set[j], data_set[j + 1] = data_set[j + 1], data_set[j]
                exchange = False
        if exchange:
            return


bubble_sort_v1(li1)


# 选择排序 - 每次把无序区里最小的数放到最前面
@cal_time
def select_sort(data_set):
    for i in range(len(data_set) - 1):
        min_loc = i
        for j in range(i, len(data_set)):
            if data_set[min_loc] > data_set[j]:
                min_loc = j
        if min_loc != i:
            data_set[i], data_set[min_loc] = data_set[min_loc], data_set[i]


select_sort(li2)


# 插入排序 - 每次把无序区中第一个数插入到有序区中

@cal_time
def insert_sort(data_set):
    for i in range(1, len(data_set)):
        tmp = data_set[i]
        j = i - 1
        while j >= 0 and tmp < data_set[j]:
            data_set[j + 1] = data_set[j]
            j = j - 1
        data_set[j + 1] = tmp


insert_sort(li3)


#  NB 三人组

# 快速排序 - 每次将列表第一个数放到中间，使得左面的都比他小，右面的都比他大，再对左右两个列表做次操作，递归下去...
@cal_time
def quick_sort(data_set):
    return _quick_sort(data_set, 0, len(data_set) - 1)


def _quick_sort(data_set, left, right):
    if left < right:
        mid = partition(data_set, left, right)
        _quick_sort(data_set, left, mid - 1)
        _quick_sort(data_set, mid + 1, right)


def partition(data_set, left, right):
    tmp = data_set[left]
    while left < right:
        while left < right and data_set[right] >= tmp:
            right -= 1
        data_set[left] = data_set[right]
        while left < right and data_set[left] <= tmp:
            left += 1
        data_set[right] = data_set[left]
    data_set[left] = tmp
    return left


quick_sort(li4)


# 堆排序

def sift(data, low, high):
    i = low
    j = 2 * i + 1
    tmp = data[i]
    while j <= high:
        if j < high and data[j] < data[j + 1]:
            j += 1
        if tmp < data[j]:
            data[i] = data[j]
            i = j
            j = 2 * i + 1
        else:
            break
    data[i] = tmp


@cal_time
def heap_sort(data):
    n = len(data)
    # 创建堆
    for i in range(n // 2 - 1, -1, -1):
        sift(data, i, n - 1)
    # 整理
    for i in range(n - 1, -1, -1):
        data[0], data[i] = data[i], data[0]
        sift(data, 0, i - 1)


heap_sort(li5)


# 归并排序

def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if li[i] <= li[j]:
            ltmp.append(li[i])
            i += 1
        else:  # li[i]>li[j]
            ltmp.append(li[j])
            j += 1
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high + 1] = ltmp


def _mergesort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        _mergesort(li, low, mid)
        _mergesort(li, mid + 1, high)
        merge(li, low, mid, high)


@cal_time
def mergesort(li):
    low = 0
    high = len(li) - 1
    return _mergesort(li, low, high)


mergesort(li6)


# 计数排序
@cal_time
def count_sort(li, max_num):
    count = [0 for i in range(max_num + 1)]
    print(count)
    for num in li:
        count[num] += 1
    i = 0
    for num, m in enumerate(count):
        for j in range(m):
            li[i] = num
            i += 1


li7 = [1, 2, 3, 4, 4, 5, 5, 6, 2, 3, 2, 3, 4, 2, 3, 2, 2, 3, 4, 3, 2, 4, 2, 4, 6, 2, 4]
count_sort(li7, 6)


# 希尔排序 - 每次进行len(list)//2分组进行插入排序
@cal_time
def shell_sort(data_set):
    gap = len(data_set)//2
    while gap > 0:
        for i in range(gap, len(data_set)):
            tmp = data_set[i]
            j = i - gap
            while j >= 0 and tmp < data_set[j]:
                data_set[j + gap] = data_set[j]
                j = j - gap
            data_set[j + gap] = tmp
        gap //= 2

shell_sort(li8)

