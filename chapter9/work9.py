# -*- coding: utf-8 -*-
"""
Created on =2019-01-17

@author: wenshijie
"""
# work9
import numpy as np
# 9.9 为分团判定问题编写一个多项式时间验证算法


def check_clique(w, s):
    """
    :param w: 邻近矩阵从0开始0代表第一个顶点.0代表没有路径，1带表有路径
    :param s: 分团的顶点顶点1,2..列表最大容量是邻近矩阵的行数
    :return: bool 是否是分团
    """
    result = True
    n = len(s)
    i = 0
    while (i < n) and result:
        for j in range(i+1, n):
            if w[s[i]-1][s[j]-1] == 0:  # 小于无穷
                result = False
        i += 1
    return result
# 9.12 检查哈密顿回路多项式时间


def check_hamiltonian(w, s):
    """

    :param w: 邻近矩阵
    :param s: 路劲
    :return: bool
    """
    n = len(s)
    result = True
    i = 0
    while (i < n-1) & result:
        if w[s[i]-1][s[i+1]-1] == 0:
            result = False
    return result
# 9.19 装箱问题近似算法的详细版本


def packing(weight, capacity):
    """

    :param weight: 物品的重量按照非递增排列,最大的要小于箱子的容量
    :param capacity: 箱子的容量
    :return: 每个箱子的装箱情况
    """
    result = [[]]
    for w in weight:
        if w + sum(result[-1]) < capacity:
            for pack in result:
                if sum(pack) + w < capacity:
                    pack.append(w)
                    break
        else:
            result.append([w])
    return result
# 9.24 编写一个多项式时间算法，检查一个无向图是否存在哈密顿回路
# 如果存在度为1的顶点则一定不会是哈密顿回路
# 如果顶点度都为2，则顺着一个顶点一直走下去如果最终走完所有顶点且回到起始点则为哈密顿回路


def check_path(w):  # 邻近矩阵
    """

    :param w: 邻近矩阵，如果有路劲为1没有路劲为0
    :return: bool
    """
    n = np.shape(w)[0]
    i = 0
    result = True
    if n < 3:
        result = False
    while (i < n) & result:
        if sum(w[i]) != 2:
            result = False
        i += 1
    if result:  # 如果顶点的度都为2
        result_j = [0]  # 路过的顶点
        for j in result_j:
            for k in range(n):
                if (w[j][k] != 0) & (k not in result_j):
                    result_j.append(k)
        if len(result_j) != n:
            result = False
    return result







if __name__ == '__main__':
    # w = [[0, 1, 0, 1, 1], [1, 0, 1, 1, 1], [0, 1, 0, 1, 0], [1, 1, 1, 0, 1], [1, 1, 0, 1, 0]]
    # print(check_clique(w, [1, 2, 3, 4]))
    # wei = [0.85, 0.5, 0.4, 0.4, 0.3, 0.2, 0.2, 0.1]
    # print(packing(wei, 1))
    w = np.array([[0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1],
                  [0, 0, 0, 1, 0, 1], [0, 0, 0, 1, 1, 0]])
    print(check_path(w))


