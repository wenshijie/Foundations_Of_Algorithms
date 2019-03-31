# -*- coding: utf-8 -*-
"""
Created on =2019-01-14

@author: wenshijie
"""
# work 7
from binary_tree import Node
# 7.16 使用分而治之编写非递归合并排序算法


def merger_sort(s):  # 待排序数组

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

    n = len(s)
    part = [[0, int((n-1)/2), n-1]]   # 最开始的分割
    for value in part:
        low = value[0]
        mid = value[1]
        high = value[2]
        if high - low > 2:
            part.append([low, int((low+mid)/2), mid])
            part.append([mid + 1, int((high+mid+1)/2), high])
        if high - low == 2:
            part.append([low, int((low+mid)/2), mid])
    while part:
        [l, m, h] = part.pop(-1)
        merges(l, m, h)
    return s
# 7.21 编写一个非递归快速排序算法


def quick_sort(s):

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
    n = len(s)
    part = [[0, n-1]]
    for value in part:
        point = _partition(value[0], value[1])
        if point-1 > value[0]:
            part.append([value[0], point - 1])
        if value[1] > point+1:
            part.append([point+1, value[1]])
    return s
# 7.25 冒泡排序


def bubbling_sort(s):
    n = len(s)
    i = n-2  # 最后一项为n-1
    while i >= 0:
        j = 0
        while j <= i:
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]  # 较大的放到后面
            j += 1
        i -= 1
    return s
# 7.26 编写一个算法检查一个准完全二叉树是不是堆
# 假设准完全二叉树binary_tree里的形式存在


def check_heap(p):  # 输入一个二叉树
    part = [p]
    switch = True
    while (len(part) > 0) & switch:
        item = part.pop(0)
        if item.left_children:
            part.append(item.left_children)
            if item.value < item.left_children.value:
                switch = False
        if item.right_children:
            part.append(item.right_children)
            if item.value < item.right_children.value:
                switch = False
    return switch
# 7.32 chanter7 中容易修改
# 7.37 将元素与指针相同，例如5放到S[5]
# 7.43


def sort43(s):
    n = len(s)

    def _sort(low, high):
        if high - low > 0:
            if s[low] > s[low+1]:
                max_point = low
                min_point = low+1
            else:
                max_point = low + 1
                min_point = low
            k = low + 2
            while k <= high:
                if s[k] < s[min_point]:
                    min_point = k
                elif s[k] > s[max_point]:
                    max_point = k
                k += 1
            s[low], s[min_point], s[high], s[max_point] = s[min_point], s[low], s[max_point], s[high]
            _sort(low+1, high-1)
    _sort(0, n-1)
    return s
# 7.46 用k个元素的堆













if __name__ == '__main__':
    s = [2, 4, 6, 3, 1, 5, 3, 7, 9, 8]
    # print(merger_sort(s))
    # print(quick_sort(s))
    # print(bubbling_sort(s))
    # p = Node(8)
    # p.left_children = Node(6)
    # p.right_children = Node(5)
    # p.left_children.left_children = Node(1)
    # p.left_children.right_children = Node(3)
    # p.right_children.left_children = Node(6)
    # p.right_children.right_children = Node(4)
    # print(check_heap(p))
    print(sort43(s))
