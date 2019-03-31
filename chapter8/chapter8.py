# -*- coding: utf-8 -*-
"""
Created on =2019-01-15

@author: wenshijie
"""
# chapter8
import math
import random
# 算法 8.1


def interpolation_search(s, x):  # s 有序数组 x 要查找的值
    n = len(s)
    low, high, i = 0, n, -1
    if (x >= s[low]) & (x <= s[high]):
        while (low <= high) & (i == -1):
            denominator = s[high] - s[low]
            if denominator == 0 :
                mid = low
            else:
                mid = low + int((x - s[low])*(high - low)/denominator)
            if x == s[mid]:
                i = mid
            elif x < s[mid]:
                high = mid - 1
            else:
                low = mid + 1
    if i == -1:
        return 0
    else:
        return i
# 算法 8.2


def find_largest(s):
    n = len(s)
    large = s[0]
    for i in range(1, n):
        if s[i] > large:
            large = s[i]
    return large
# 算法 8.3


def find_both(s):
    n = len(s)
    large = s[0]
    small = s[0]
    for i in range(1, n):
        if s[i] < small:
            small = s[i]
        elif s[i] > large:
            large = s[i]
    return small, large
# 算法8.4 通过键的配对找出最大最小值


def find_both2(s):
    n = len(s)
    last_value = None
    if n % 2 == 1:
        last_value = s.pop(-1)
        n = n - 1
    if s[0] < s[1]:
        small = s[0]
        large = s[1]
    else:
        small = s[1]
        large = s[0]
    k = 2
    while k <= n-2:
        if s[k] < s[k+1]:
            if s[k] < small:
                small = s[k]
            if s[k+1] > large:
                large = s[k+1]
        else:
            if s[k+1] < small:
                small = s[k+1]
            if s[k] > large:
                large = s[k]
        k += 2
    if last_value:
        if last_value < small:
            small = last_value
        if last_value > large:
            large = last_value
    return small, large
# 算法 8.5 查找第k小键


def selection(s, k):
    n = len(s)
    k = k - 1  # 数值指针从0开始
    def _partition(low, high):
        tmp = s[low]
        j = low
        i = low + 1
        while i <= high:
            if s[i] < tmp:
                j += 1
                s[i], s[j] = s[j], s[i]
            i += 1
        s[low], s[j] = s[j], s[low]
        return j

    def _selection(low, high):
        if low == high:
            return s[low]
        else:
            point = _partition(low, high)
            if k == point:
                return s[point]
            elif k < point:
                return _selection(low, point - 1)
            else:
                return _selection(point+1, high)
    return _selection(0, n-1)
# 算法8.6 使用中值选择


def selection2(s, k):
    n = len(s)
    k = k - 1

    def _get_mid_value(low, high):
        s_tmp = s[low:high+1]
        s_tmp.sort()
        m = len(s_tmp)
        return s_tmp[int((m-1)/2)]

    def _select(low, high):
        if low == high:
            return s[low]
        else:
            point = partition(low, high)
            if k == point:
                return s[point]
            elif k < point:
                return _select(low, point - 1)
            else:
                return _select(point+1, high)

    def partition(low, high):
        global mark
        array_size = high - low + 1
        r = int(math.ceil(array_size/5))
        mid_value = []
        for i in range(r):
            first = low + 5*i
            last = min(low+5*(i+1)-1, array_size)
            mid_value.append(_get_mid_value(first, last))
        pivot_item = selection2(mid_value, int((r+1)/2))
        j = low
        i = low
        while i <= high:
            if s[i] == pivot_item:
                s[i], s[j] = s[j], s[i]
                mark = j  # 把中值的中值的位子标记出来·
                j += 1
            elif s[i] < pivot_item:
                s[i], s[j] = s[j], s[i]
                j += 1
            i += 1
        pivot_point = j - 1
        s[mark], s[pivot_point] = s[pivot_point], s[mark]
        return pivot_point
    return _select(0, n-1)
# 算法 8.7 概率选择


def selection3(s, k):
    n = len(s)
    k = k - 1

    def _select(low, high):
        if low == high:
            return s[low]
        else:
            point = partition(low, high)
            if k == point:
                return s[point]
            elif k < point:
                return _select(low, point-1)
            else:
                return _select(point+1, high)

    def partition(low, high):
        random_spot = random.randint(low, high)
        pivot_item = s[random_spot]
        j = low
        i = low
        while i <= high:
            if s[i] < pivot_item:
                s[i], s[j] = s[j], s[i]
                j += 1
            i += 1
        pivot_point = j
        s[pivot_point] = pivot_item
        return pivot_point
    return _select(0, n-1)





if __name__ == '__main__':
    s = [1, 2, 5, 4, 9, 8, 24, 23, 35]
    # print(find_largest(s))
    # print(find_both2(s))
    print(selection3(s, 7))