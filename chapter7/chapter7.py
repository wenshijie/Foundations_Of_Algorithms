# -*- coding: utf-8 -*-
"""
Created on =2019-01-14

@author: wenshijie
"""
# chapter7
import math


# 算法 7.1 插入排序


def insert_sort(s):
    for i in range(1, len(s)):
        tmp = s[i]
        j = i - 1
        while (j >= 0) & (s[j] > tmp):
            s[j + 1] = s[j]
            j -= 1
        s[j + 1] = tmp
    return s


# 算法 7.2  选择排序


def selection_sort(s):
    n = len(s)
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if s[j] < s[smallest]:
                smallest = j
        tmp = s[smallest]
        s[smallest] = s[i]
        s[i] = tmp
    return s


# 合并排序 动态规划版本


def merge_sort(s):
    n = len(s)

    def merges(low, mid, high):
        q = [0] * (high - low + 1)
        i, j, k = low, mid + 1, 0
        while (i <= mid) & (j <= high):
            if s[i] < s[j]:
                q[k] = s[i]
                i += 1
            else:
                q[k] = s[j]
                j += 1
            k += 1
        if i == mid + 1:
            q[k:] = s[j:high + 1]
        else:
            q[k:] = s[i:mid + 1]
        s[low:high + 1] = q

    m = int(math.ceil(math.log2(n)))  # 向上取整
    m1 = 2 ** int(math.ceil(math.log2(n)))
    size = 1
    k = 1
    while k <= m:
        low = 0
        while low <= m1 - 2 * size + 1:
            mid = low + size - 1
            high = min(low + 2 * size - 1, n)
            merges(low, mid, high)
            low = low + 2 * size
        size = 2 * size
        k += 1
    return s


# 算法 7.5 堆排序


def siftdown(i, s):  # 恢复堆的性质, s是堆的一个列表形式
    n = len(s)
    if n > 0:
        parent = i
        sift_key = s[i]
        spot_found = True
        while (2 * parent <= n - 2) & spot_found:
            if 2 * parent < n - 2:
                if s[2 * parent + 1] < s[2 * parent + 2]:
                    larger_child = 2 * parent + 2
                else:
                    larger_child = 2 * parent + 1
            else:
                larger_child = 2 * parent + 1
            if sift_key < s[larger_child]:
                s[parent] = s[larger_child]
                parent = larger_child
            else:
                spot_found = False
        s[parent] = sift_key


def root(s):  # 删除根节点，并恢复堆,返回删除的根节点
    key_out = s[0]
    s[0] = s[-1]
    del s[-1]
    siftdown(0, s)
    return key_out


def remove_keys(s):
    n = len(s)
    result = []
    i = 1
    while i <= n:
        result.append(root(s))
        i += 1
    return result


def make_heap(h):
    n = len(h)
    m = int((n - 1) / 2)
    while m >= 0:
        siftdown(m, h)
        m -= 1


def heap_sort(s):
    make_heap(s)
    ss = remove_keys(s)
    return ss


# 基数排序


def radix_sort(s):  # 输入一个以10为基底的数组
    max_long = len(str(max(s)))
    s = [str(i) for i in s]  # 为了方便取位数 转化为字符
    list1_9 = [[]] * 10

    def distribute(s_list, i):
        for k in range(10):
            list1_9[k].clear()
        for value in s_list:
            # if no i get 0
            # noinspection PyBroadException
            try:
                tmp = value[-i]
            except Exception:
                tmp = 0
            list1_9[int(tmp)] = list1_9[int(tmp)].copy() + [value]

    def coalesce(ss):
        ss.clear()
        for j in range(10):
            ss.extend(list1_9[j])

    for j in range(1, max_long + 1):
        distribute(s, j)
        coalesce(s)
    return s


if __name__ == '__main__':
    s = [5, 4, 6, 3, 2, 1, 7, 8]
    # print(insert_sort(s))
    # print(selection_sort(s))
    # print(merge_sort(s))
    # print(heap_sort(s))
    # print(root([8, 7, 6, 5, 2, 1, 4, 3]))
    s1 = [45, 55, 65, 54, 34, 178, 234, 69, 95]
    print(radix_sort(s1))
