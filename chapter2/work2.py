# -*- coding: utf-8 -*-
"""
Created on =2019-01-03

@author: wenshijie
"""
from typing import List

import numpy as np

# work2
# 2.6 有序数组分为三个子列表查找,时间复杂度2log（3底）（n）


def find_three(s, x):
    if len(s) >= 1:
        def _find_three(low, high):
            if low <= high:
                mid1 = int((low+high)/3)
                mid2 = int(2*(low+high)/3)
                if x == s[mid1]:
                    return mid1
                elif x == s[mid2]:
                    return mid2
                else:
                    if x < s[mid1]:
                        return _find_three(low, mid1-1)
                    elif (x > s[mid1]) & (x < s[mid2]):
                        return _find_three(mid1+1, mid2-1)
                    else:
                        return _find_three(mid2+1, high)
            else:
                return -1
        return _find_three(0, len(s)-1)
    else:
        return -1
# 2.7 分而治之找最大值


def binary_find_max(s):
    if (isinstance(s, list))&(len(s) >= 1):
        def _bin_max(low, high):
            if high > low:
                mid = int((low+high)/2)
                return max(_bin_max(low, mid), _bin_max(mid+1, high))
            else:
                return s[low]
        return _bin_max(0, len(s)-1)
    else:
        print('no max value,please input a list and at least has a item')
# 2.10 给定一个由n个不同正整数的列表，分为两个大小各位n/2的列表使得两个列表的整数和之差最大


def sum_diff_max(s):  # 只能使最后一步n/2与n/2找出前n/2项最小的，后面的不需要排序，所以略小于合并排序

        def _mergepartsort2(low, high):  # 部分排序，只把最小的n/2项依次放到前n项
            if low < high:
                mid = int((low + high) / 2)
                _mergepartsort2(low, mid)
                _mergepartsort2(mid + 1, high)
                return _merge2(low, mid, high)

        def _merge2(low, mid, high):
            '''合并'''
            n = high - low + 1
            u = [0] * n
            i, j, k = low, mid + 1, 0
            while (i <= mid) and (j <= high) and (k < int(len(s)/2)):
                # 只有len(s)/2两个数组合并时以及len(s)/4两个数组合并时最后一个判断才有作用，对于后者来说如果最后的
                # 判定为否 则前面的两个一定也为否，也就是说对于len(s)/4合并此循环的排序已经完成
                if s[i] < s[j]:
                    u[k] = s[i]
                    i += 1
                else:
                    u[k] = s[j]
                    j += 1
                k += 1
            if (k == int(len(s)/2)) & (mid == int(len(s)/2)-1):  # 避免len(s)/4 合并时k也为该值
                return u[:int(len(s)/2)], s[i:mid+1]+s[j:], sum(s[i:mid+1]+s[j:])-sum(u[:])   # 和最小，和最大，差最大
            else:
                if i > mid:
                    while k < n:
                        u[k] = s[j]
                        k += 1
                        j += 1
                else:
                    while k < n:
                        u[k] = s[i]
                        k += 1
                        i += 1
                s[low:high + 1] = u[:]
        return _mergepartsort2(0, len(s)-1)

# 2.11 为合并排序编写一个非递归算法


def sortmerge(s):
    n = len(s)
    long = 2

    def _merge2(low, mid, high):
        # 合并两个相邻的列表
        m = high - low + 1
        u = [0] * m
        h, j, k = low, mid + 1, 0
        while (h <= mid) and (j <= high):
            if s[h] < s[j]:
                u[k] = s[h]
                h += 1
            else:
                u[k] = s[j]
                j += 1
            k += 1
        if h > mid:
            while k < m:
                u[k] = s[j]
                k += 1
                j += 1
        else:
            while k < m:
                u[k] = s[h]
                k += 1
                h += 1
        s[low:high + 1] = u[:]

    while long <= n:
        i = 0
        while i+long-1 <= n-1:
            _merge2(i, int((2*i+long-1)/2), i+long-1)
            i = i+long
        if i <= n-1:
            _merge2(i, int((i+n-1)/2), n-1)
        long = 2*long
    _merge2(0, i-1, n-1)
    return s
# 2.11 2合并非递归


def sortmerge_no_recurison(s):
    n = len(s)
    i = 1
    for i in range(1, n):
        j = 0
        while (j < i) & (s[i] > s[j]):
            j += 1
        if j < i:
            u = s[j:i]
            s[j] = s[i]
            s[j+1:i+1] = u[:]
    return s
# 2.13 排序分为三个子列表合并排序


def mergesort_three():
    print()

# 2.17 汉诺塔问题 假设圆盘从小到大为 1,2,3,...n,三个柱子为 a,b,c, 开始时 在a上从上到下依次是圆盘从小到大 挪到c上


def hanoi(n, x, y, z):
    if n == 1:
        print('1 from {}->{}'.format(x,z))
    else:
        hanoi(n-1,x,z,y)
        print('{} from {}->{}'.format(n,x,z))
        hanoi(n-1,y,x,z)


# 2.23 快速排序非递归算法
def quicksort_no_recursion(s):
    n = len(s)
    stack = [0, n-1]
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high <= low:
            continue
        tmp = s[low]
        i = low+1
        j = low
        while i <= high:
            if s[i] < tmp:
                j += 1
                s[j], s[i] = s[i], s[j]
            i += 1
        point = j
        s[low] = s[j]
        s[j] = tmp
        stack.extend([low, point-1, point+1, high])
        # 所以可能的区间，每个区间都排列好，而且前一个区间一定都小于后一个区间里面的值
    return s

# 2.33 修改大整数乘法


def three_intergeprod(x1, x2):  # n是3的K次幂
    max_value = max(abs(x1), abs(x2))
    n = len(str(max_value))
    if n <= 3:
        return x1*x2
    else:
        k = int(n/3)
        a, x = int(x1/10**(2*k)), int(x2/10**(2*k))
        b, y = int((int(x1/10**k)) % 10**k), int((int(x2/10**k)) % 10**k)
        c, z = int(x1 % 10**k), int(x2 % 10**k)
        ax = three_intergeprod(a, x)
        ay = three_intergeprod(a, y)
        bx = three_intergeprod(b, x)
        bz = three_intergeprod(b, z)
        cy = three_intergeprod(c, y)
        cz = three_intergeprod(c, z)
        r = three_intergeprod(a+b+c, x+y+z)
        return ax*10**(4*k)+(ay+bx)*10**(3*k)+(r-ax-ay-bx-bz-cy-cz)*10**(2*k)+(bz+cy)*10**k+cz


# 2.37 利用分而治之编写一个计算n！的递归算法

# 2.37 分而治之计算n!


def factorial(n):  # n正为整数
    if n < 1:
        print('please in a interge >0')
    else:
        low = 1
        high = n

        def _fac(l, h):
            if (h-l) == 0:
                return h
            else:
                mid=int((l+h)/2)
                return _fac(l, mid)*_fac(mid+1, h)
        return _fac(low, high)


# 2.40 编写一个高效算法，在n*m中查找某一个值


def find_value(s, x):  # s是一个矩阵，x是否在矩阵中
    highi, highj = np.shape(s)[0]-1, np.shape(s)[1]-1
    lowi, lowj = 0, 0
    result = []

    def _find(li, hi, lj, hj):
        if (li <= hi) & (lj <= hj):
            midi = int((li + hi) / 2)
            midj = int((lj + hj) / 2)
            if x == s[midi][midj]:
                result.append((midi, midj))
                i1, i2 = midi, midi
                j1, j2 = midj, midj
                while (s[midi][j1-1] == x) & (j1-1 >= lj):
                    # 第midi行非递减，所以依次检查qmij前的项是否等于x，当有一项不等于再前面的也不等于
                    result.append((midi, j1-1))
                    j1 -= 1
                while (s[midi][j2+1] == x)&(j2+1 <= hj):  #midi行，midj后的项
                    result.append((midi, j2-1))
                    j2 += 1
                while (s[i1-1][midj] == x)&(i1-1 >= li):
                    result.append((i1-1, midj))
                    i1 -= 1
                while (s[i2+1][midj] == x)&(i2+1 <= hj):
                    result.append((i2+1, midj))
                    i2 += 1
                _find(li, midi-1, lj, midj-1)
                _find(li, midi-1, midj+1, hj)
                _find(midi+1, hi, lj, midj-1)
                _find(midj+1, hi, midj+1, hj)
            elif x < s[midi][midj]:
                for i in range(li, midi):
                    # 第midj列非递减，所以依次检查前mii-1行是否等于x，可以用二分查找
                    if s[i][midj] == x:
                        result.append((i, midj))
                for j in range(lj, midj):  # midi行，midj前的项
                    if s[midi][j] == x:
                        result.append((midi, j))
                _find(li, midi-1, lj, midj-1)
                _find(li, midi-1, midj+1, hj)
                _find(midi+1, hi, lj, midj-1)
            else:
                for i in range(midi+1, hi+1):
                    # 第midj列非递减，所以依次检查后mid-1行是否等于x，可以用二分查找
                    if s[i][midj] == x:
                        result.append((i, midj))
                for j in range(midj+1, hj+1):  # midi行，midj前的项
                    if s[midi][j] == x:
                        result.append((midi, j))
                _find(midi+1, hi, lj, midj-1)
                _find(midi+1, hi, midj+1, hj)
                _find(li, midi-1, midj+1, hj)
    _find(lowi, highi, lowj, highj)
    return result  # 所有满足目标值的索引
# 2.42 tromino


def tromino(s, x, y):  # s为空格，ti,tj 是缺失的空格
    n = np.shape(s)[0]-1
    k = [1]  # 第一块以后每铺一块列表递增一位可以把列表里只保留一个元素-下一次要铺的是第几块，不过数据少的时候没必要

    def _tromino(li, hi, lj, hj, ti, tj):
        if ((hi-li) >= 1) & ((hj-lj) >= 1):
            midi = int((li+hi)/2)  # 行的中点
            midj = int((lj+hj)/2)  # 列的中点
            if (ti > midi) & (tj > midj):
                s[midi][midj] = k[-1]
                s[midi][midj + 1] = k[-1]
                s[midi + 1][midj] = k[-1]
                k.append(k[-1]+1)
                _tromino(li, midi, lj, midj, midi, midj)
                _tromino(li, midi, midj+1, hj, midi, midj+1)
                _tromino(midi+1, hi, lj, midj, midi+1, midj)
                _tromino(midi+1, hi, midj+1, hj, ti, tj)
            if (ti > midi) & (tj <= midj):
                s[midi][midj] = k[-1]
                s[midi][midj + 1] = k[-1]
                s[midi + 1][midj + 1] = k[-1]
                k.append(k[-1]+1)
                _tromino(li, midi, lj, midj, midi, midj )
                _tromino(li, midi, midj + 1, hj, midi, midj + 1)
                _tromino(midi + 1, hi, midj + 1, hj, midi+1, midj+1)
                _tromino(midi + 1, hi, lj, midj, ti, tj)
            if (ti <= midi) & (tj > midj):
                s[midi][midj] = k[-1]
                s[midi + 1][midj] = k[-1]
                s[midi + 1][midj + 1] = k[-1]
                k.append(k[-1]+1)
                _tromino(li, midi, lj, midj, midi, midj)
                _tromino(midi + 1, hi, lj, midj, midi + 1, midj)
                _tromino(midi + 1, hi, midj + 1, hj, midi + 1, midj + 1)
                _tromino(li, midi, midj+1, hj, ti, tj)
            if (ti <= midi) & (tj <= midj):
                s[midi][midj + 1] = k[-1]
                s[midi + 1][midj] = k[-1]
                s[midi + 1][midj + 1] = k[-1]
                k.append(k[-1]+1)
                _tromino(li, midi, midj + 1, hj, midi, midj + 1)
                _tromino(midi + 1, hi, lj, midj, midi + 1, midj)
                _tromino(midi + 1, hi, midj + 1, hj, midi + 1, midj + 1)
                _tromino(li, midi, lj, midj, ti, tj)
    _tromino(0, n, 0, n, x, y)
    return s
# 2.43 称硬币


def find_false_coin(s):  # s为硬币组成的数组真的为1假的为2，s长度为3的幂,称重log3\n,时间复杂度2*log3\n(比较)

    def _find_false_coin(l, h):
        long = int((h-l+1)/3)
        if long >= 3:
            m1 = sum(s[l:long+l])
            m2 = sum(s[long+l:2*long+l])
            if m1 == m2:
                return _find_false_coin(2*long+l, h)
            elif m1 > m2:
                return _find_false_coin(l, long+l-1)
            else:
                return _find_false_coin(long+l, 2*long+l-1)
        else:
            if s[l] == s[l+1]:
                return h
            if s[l] > s[l+1]:
                return l
            else:
                return l+1
    return _find_false_coin(0, len(s)-1)
# 2.44 取余数 ！！！！！！不会


def get_mod(x, n, p):

    def _get_mod(m):
        if m >= 2:
            v = _get_mod(int(m / 2)) * _get_mod(int(m / 2))
            r = v - int(v / p) * p
            return r
        else:
            r = x - int(x / p) * p
            return r
    return _get_mod(n)


# 2.45-1(非递推) 连续子列表最大和值


def find_max_list(s):
    all_max = 0  # 全局最大值
    i = 0
    n = len(s)-1
    while i <= n:
        list_max = []  # 用来存放局部最大连续列表和的开始地址和结束位子，首项是开始处尾项是结束处
        last_max = 0  # 局部连续子列表和最大值
        last_sum = s[i]  # 连续子列表的和
        while (i <= n) & (last_sum > 0):
            if last_sum > last_max:
                list_max.append(i)
                last_max = last_sum
            if i == n:  # 如果i=n 则说明已经加到最后一项了
                i += 1
            else:
                last_sum = last_sum + s[i+1]
                i += 1
        if last_max > all_max:
            all_max = last_max
            start, end = list_max[0], list_max[-1]
        i += 1
    return all_max, start, end
# 2.45-2递推


def find_max_list2(s):
    list_value_max = [0, -1, -1]  # 初始令最大值为s的和，列表起止-1，-1

    def _find(l, h):
        if h - l > 0:  # 包含单项，不包含单项大于1
            if list_value_max[0] < sum(s[l:h]):
                list_value_max[0] = sum(s[l:h])  # 可以把求和命名一个变量避免重复求和
                list_value_max[1] = l
                list_value_max[2] = h-1
            if sum(s[l+1:h+1]) > list_value_max[0]:
                list_value_max[0] = sum(s[l+1:h+1])
                list_value_max[1] = l+1
                list_value_max[2] = h
            _find(l, h-1)
            _find(l+1,h)
    _find(0, len(s)-1)
    return list_value_max


if __name__ == '__main__':
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    s1 = [1, 9, 12, 4, 3, 4, 7, 5, 6, 8, 10, 11, 15, 18, 22, 19]
    a = 123456789
    b = 987654321123456789987654321
    c = 8
    s2 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 4, 5, 6, 7, 8, 9, 10, 11],
                   [4, 5, 6, 7, 8, 9, 10, 11, 12], [5, 6, 7, 8, 9, 10, 11, 12, 13], [6, 7, 8, 9, 10, 11, 12, 13, 14],
                   [7, 8, 9, 10, 11, 12, 13, 14, 15]])
    coin = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    s3 = [-1, 9, -12, -4, 3, 4, 7, 5, 6, 8, -10, -11, -15, -18, 22, -19]
    # print(find_three(s, 0))
    # print(binary_find_max(s1))
    # print(sum_diff_max(s1))
    # hanoi(4, 'a', 'b', 'c')
    # print(quicksort_no_recursion(s1))
    # print(three_intergeprod(a, b))
    # print(factorial(c))
    # print(find_value(s2, 5))
    # print(tromino(np.zeros((16, 16)), 4, 7))
    # print(find_false_coin(coin))
    # print(get_mod(4, 4, 3))
    print(find_max_list2(s3))