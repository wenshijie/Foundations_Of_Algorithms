# -*- coding: utf-8 -*-
"""
Created on =2019-01-04

@author: wenshijie
"""
import numpy as np
import itertools
# work3

# 3.4 修改求二次项系数


def bin3(n, k):
    if k > n/2:
        k = n-k
    b = [0]*(k+1)
    for i in range(n+1):
        u = b[:]
        print(u)
        for j in range(min(i+1, k+1)):
            if (j == 0) | (j == i):
                b[j] = 1
            else:
                b[j] = u[j-1]+u[j]
    return b[k]
# 3.16 n个矩阵相乘有多少顺序


def measure(n):  #
    if (n == 2) | (n == 1):
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return 5
    else:
        value = 0
        for i in range(3, n):
            value = value + 2*measure(i)

        return value  # 可以把n个分为，第一个乘以n-1，和最后一个乘以n-1，两种情况
# 3.20 最优相乘顺序，因为只有1*1， 1*d ，d*d，d*1 所以d*d一定在1d和d1中间，或者在两边易知，最优是吧1d和dd相乘而不是吧dd和dd相乘，
# 又如果有dd出现则一定是由1d开始，又1d*dd=1d 所以只要先把所有1d和d1之间的从左往右相乘即可


def matrix_prod(s):  # n个行列列表
    n = len(s)-1  # 矩阵的个数
    result = []
    list_1 = []  # 1 所在的位置
    for i in range(len(s)):
        if s[i] == 1:
            list_1.append(i)
    for i in range(list_1[0]-1):
        result.append('(A'+str(i+1))
    if list_1[0] > 0:
        result.append('A'+str(list_1[0])+')'*(list_1[0]-1))
    result.append('(A'+str(list_1[0]+1))
    for j in list_1[1:-1]:  # 不包括开头和结尾
        result.append('...A'+str(j)+')(A'+str(j+1)+'...')
    result.append('A'+str(list_1[-1])+')')
    if list_1[-1] < n:
        result.append('('*(n-list_1[-1]-1)+'A'+str(list_1[-1]+1))
        for j in range(list_1[-1]+2, n+1):
            result.append('A'+str(j)+')')
    return ''.join(result)
# 3.29 推销员问题相信动态规划解决


def make_set(v):  # 输入不包含v1的矩阵,生成不包含v1的集合
    long_v = len(v)
    subset = [[]]  # 在里面加一项作为空集的标志
    for i in range(1, long_v+1):
        subset.extend(itertools.combinations(v, i))
    return [list(i) for i in subset]  # 所以D的长度应该是2的n-1次幂，不包括V1，且包括空集


def k_subset(k, n, s):  # 包含k个顶点的所有子集
    start = sum([bin3(n,i) for i in range(0, k)])  # 从Cn、0开始应为集合中有空集
    end = sum([bin3(n, i) for i in range(0, k+1)])
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
# 3.32 序列对准动态规划


def opt(s1, s2):  # 两个需要对准的序列
    n = len(s1)-1  # 序列1的长度,当做行标,输入时已经在末尾加了一个符号和下面的列表加的不同
    m = len(s2)-1  # 序列2的长度，当列标
    d = np.zeros((n+1, m+1))
    for i in range(m+1):
        d[n][i] = 2*(m-i)
    for j in range(n+1):
        d[j][m] = 2*(n-j)
    sum_ij = m + n - 2
    while sum_ij >= 0:
        for i in range(n):
            if (0 <= sum_ij - i) & (sum_ij - i <= m - 1):
                print(sum_ij - i)
                if s1[i] == s2[sum_ij - i]:
                    penalty = 0
                else:
                    penalty = 1
                d[i][sum_ij - i] = min(d[i + 1][sum_ij - i + 1] + penalty,
                                       d[i + 1][sum_ij - i] + 2, d[i][sum_ij - i + 1] + 2)
        sum_ij = sum_ij - 1
    return d
# 3.38 使用动态规划法给定n个实数列表，求出任意连续子列表的最大和值


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
# 3.39 返回最长公共子序列
# 首先生成n+1行m+1列的矩阵，第一行第一列为0，后面如果两个列表的第i和第j个值s1[i]=s[j]则为1完毕后，
# 从第二行第二列开始，每个位置的值等于它自身加上前一行到0到该列与前一列0-该行的最大值
# 如果某个位置变化后大于等于自身且自身原来等于1，输出其改变后的值和位置


def find_sublist(s1, s2):
    n = len(s1)
    m = len(s2)
    d = np.zeros((n+1, m+1), int)
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                d[i][j] = 1
            else:
                d[i][j] = 0
    result_list = []
    for i in range(1, n+1):
        for j in range(1, m+1):
            tmp = d[i][j]
            d[i][j] = tmp + max(max(d[i-1, :j]), max(d[:i, j-1]))
            if (tmp == 1) & (d[i][j] >= tmp):
                result_list.append((d[i][j], i-1, j-1))
    return d, result_list
# result_list=[(1, 0, 0), (1, 0, 5), (2, 2, 3), (2, 3, 2), (1, 4, 0), (3, 4, 5), (2, 6, 2), (4, 7, 6)]
# 最长公共序列为4个 [[7,6],[4,5][3,2][0,0]] 或[[7,6],[4,5][3,2][0,0]]
# 先找第一个值最大的 让后次大且满足i和j都小于上一个。


if __name__ == '__main__':
    # print(bin3(5, 2))
    # print(measure(5))
    s = [4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 1, 4, 4, 1, 4, 4, 1, 4, 4, 4, 1, 4, 4, 4]
    s1 = [1, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 1, 4, 4, 1, 4, 4, 1, 4, 4, 4, 1, 4, 4, 4]
    s2 = [4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 1, 4, 4, 1, 4, 4, 1, 4, 4, 4, 1, 4, 4, 4, 1]
    x1 = ['A', 'A', 'C', 'A', 'G', 'T', 'T', 'A', 'C', 'C', '@']
    y1 = ['T', 'A', 'A', 'G', 'G', 'T', 'C', 'A', '*']
    x2 = ['A', '$', 'C', 'M', 'A', '*', 'M', 'N']
    y2 = ['A', 'X', 'M', 'C', '4', 'A', 'N', 'B']
    # print(matrix_prod(s2))
    # print(opt(x1, y1))
    print(find_sublist(x2, y2))
