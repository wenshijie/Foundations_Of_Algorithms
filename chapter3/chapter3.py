# -*- coding: utf-8 -*-
"""
Created on =2019-01-04

@author: wenshijie
"""
# chapter3
import numpy as np
import itertools

# 算法3.1 分而治之计算多项式系数


def bin1(n, k):  # k<=n
    if (k == 0) | (n == k):
        return 1
    else:
        return bin1(n-1, k-1)+bin1(n-1, k)

# 算法3.2 动态规划法计算二次项系数


def bin2(n, k):
    b = np.zeros((n+1, k+1), int)
    for i in range(n+1):
        for j in range(min(i+1, k+1)):
            if (j == 0) | (j == i):
                b[i][j] = 1
            else:
                b[i][j] = b[i-1][j-1]+b[i-1][j]
    return b[n][k]
# 算法3.3 floyd


def floyd(w):  # 0...n-1代表节点1...n
    d = w.copy()
    n = np.shape(w)[0]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d
# 算法 3.4


def floyd2(w, q, r):
    d = w.copy()
    n = np.shape(w)[0]
    p = np.zeros((n, n), int)-1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k]+d[k][j]:
                    p[i][j] = k  # 把 i-j的最短路径i-k-j的中间路径放到pij
                    d[i][j] = d[i][k]+d[k][j]
    print(p)
# 算法 3.5
    min_list = []

    def path(x, y):
        if p[x][y] != -1:
            path(x, p[x][y])
            min_list.append(p[x][y]+1)
            path(p[x][y], y)
    path(q-1, r-1)
    min_list = [q] + min_list + [r]
    return min_list, d[q-1, r-1]  # 最短路径，最短路线长度
# 算法 3.6


def minmult(d):  # 数组d，其索引范围为0-n，d[i-1][i]是第i个矩阵的维度
    long = len(d)-1  # 一共有多少个矩阵
    m = np.zeros((long, long), int)
    p = m.copy()-1
    for diagonal in range(1, long):
        for i in range(long-diagonal):
            j = i + diagonal
            list_value = [m[i][k] + m[k+1][j] + d[i]*d[k+1]*d[j+1] for k in range(i, j)]
            m[i][j] = min(list_value)
            p[i][j] = i + list_value.index(min(list_value))
    list_good = []
# 算法 3.7

    def order(x, y):
        if x == y:
            list_good.append('A'+str(x+1))
        else:
            k = p[x][y]
            list_good.append('(')
            order(x, k)
            order(k+1, y)
            list_good.append(')')
    order(0, long-1)
    return m[0][long-1], ''.join(list_good[1:-1])
# 3.9见binary_search_tree树不可见，下面是将一个树尽量可见话列表中第i个列表是第i层从左到右的各元素


def tree(v):  # 将一个列表变成二分查找树
    t = []
    for value in v:
        tmp = True
        i = 0
        j = 0
        while tmp:
            if len(t) == i:
                t.append([None] * 2 ** i)
                t[i][j] = value
                tmp = False
            elif t[i][j] is None:
                t[i][j] = value
                tmp = False
            else:
                if value <= t[i][j]:
                    j = 2*j
                    i = i+1
                else:
                    j = 2*j + 1
                    i = i + 1
    return t

# 算法 3.11


def make_set(v):  # 输入不包含v1的矩阵,生成不包含v1的集合
    long_v = len(v)
    subset = [[]]  # 在里面加一项作为空集的标志
    for i in range(1, long_v+1):
        subset.extend(itertools.combinations(v, i))
    return [list(i) for i in subset]  # 所以D的长度应该是2的n-1次幂，不包括V1，且包括空集


def k_subset(k, n, s):  # 包含k个顶点的所有子集
    start = sum([bin2(n,i) for i in range(0, k)])  # 从Cn、0开始应为集合中有空集
    end = sum([bin2(n, i) for i in range(0, k+1)])
    return s[start:end]


def travel(w):  # w为n+1 * n+1 第一行第一列为0 为了让索引与路径相同及1指代v1
    n = np.shape(w)[0] - 1
    v = list(range(2, n + 1))  # 这里v没有包括v1
    d = np.zeros((n+1, 2**(n-1)), int)
    p = np.zeros_like(d)
    all_subset = make_set(v)  # 包含空集
    for i in range(2, n+1):
        d[i][0] = w[i][1]
    for k in range(1, n-1):
        for item in k_subset(k, n-1, all_subset):
            for i in v:
                if i not in item:
                    tmp_d = []
                    for j in item:
                        f = item.copy()
                        f.remove(j)
                        tmp_d.append((w[i][j] + d[j][all_subset.index(f)], j))
                    min_tmp = min(tmp_d)  # 返回的是元组，第一项是结果值，第二项是j
                    d[i][all_subset.index(item)] = min_tmp[0]
                    p[i][all_subset.index(item)] = min_tmp[1]
    tmp_v = []
    for j in range(2, n+1):
        cv = v.copy()
        cv.remove(j)
        tmp_v.append((w[1][j] + d[j][all_subset.index(cv)], j))
    min_tmp_v = min(tmp_v)  # 返回元组
    d[1][2**(n-1)-1] = min_tmp_v[0]  # d的最后一列
    p[1][2**(n-1)-1] = min_tmp_v[1]
    return d[1][2**(n-1)-1], d, p
# 算法 3.12 使用分而治之的序列对准


def opt(x, y):
    m = len(x)
    n = len(y)

    def _opt(i, j):
        if i == m:
            opt_value = 2*(n-j)
        elif j == n:
            opt_value = 2*(m-j)
        else:
            if x[i] == y[j]:
                penalty = 0
            else:
                penalty = 1
            opt_value = min(_opt(i+1, j+1)+penalty, _opt(i+1, j)+2, _opt(i,j+1)+2)
        return opt_value
    return _opt(0, 0)


if __name__ == '__main__':
    w = np.array([[0, 1, 20, 1, 5], [9, 0, 3, 2, 20], [20, 20, 0, 4, 20], [20, 20, 2, 0, 3], [3, 20, 20, 20, 0]])
    d = [5, 2, 3, 4, 6, 7, 8]
    v = [12, 5, 2, 3, 4, 6, 7, 8, 1, 9, 10, 13, 15, 19, 20, 22]
    v1 = [2, 3, 4, 5]
    w = np.array([[0, 0, 0, 0, 0], [0, 0, 2, 9, 50], [0, 1, 0, 6, 4], [0, 50, 7, 0, 8], [0, 6, 3, 50, 0]])
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    x1 = ['A', 'A', 'C', 'A', 'G', 'T', 'T', 'A', 'C', 'C']
    y = [0, 2, 3, 4, 6, 7, 8, 1]
    y1 = ['T', 'A', 'A', 'G', 'G', 'T', 'C', 'A']
    # print(bin2(5, 2))
    # print(floyd2(w, 5, 3))
    # print(minmult(d))
    # print(tree(v))
    # print(k_subset(3, 4, make_set(v1)))
    # print(travel(w))
    print(opt(x1, y1))

