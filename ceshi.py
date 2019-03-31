# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 22:47:27 2019

@author: lenovo
"""
'''
def wen(a,b):
    c=1
    def shi(d,e):
        jie = c
        print(jie)
        c+=1
        print(jie)
    shi(4,4)
wen(3,3)
'''
import itertools
import numpy as np
# 算法 3.11
# 1 生成不包含v1的集合


def make_set(v):  # 输入不包含v1的矩阵
    long_v = len(v)
    subset = []
    for i in range(1, long_v+1):
        subset.extend(itertools.combinations(v, i))
    return [list(i) for i in subset]


def k_subset(k, n, s):  # 包含k个顶点的所有子集
    return s[bin2(n,k-1):bin2(n, k)]


def edge(w):  # 给一个无向连通矩阵,返回非递减的边信息
    n = np.shape(w)[0]
    edge_list = []
    for i in range(n-1):
        for j in range(1, n-1):
            if i+j < n:
                edge_list.append((w[i][i+j], i+1, i+j+1))
    edge_list.sort()
    return edge_list

s = [1, 3, 2, 4]


def merges(low, mid, high):
    q = [0]*(high - low + 1)
    i, j, k = low, mid+1, 0
    while (i <= mid) & (j <= high):
        if s[i] < s[j]:
            q[k] = s[i]
            i += 1
        else:
            q[k] = s[j]
            j += 1
        k += 1
    if i == mid+1:
        q[k:] = s[j:high+1]
    else:
        q[k:] = s[i:mid+1]
    s[low:high+1] = q
    return s


if __name__ == '__main__':
    v = [2, 3, 4, 5]
    # print(make_set(v))
    # w = np.array([[0, 1, 3, 20, 20], [1, 0, 3, 6, 20], [3, 3, 0, 4, 2], [20, 6, 4, 0, 5], [20, 20, 2, 5, 0]])
    # print(edge(w))
    print(merges(0,1,3))
