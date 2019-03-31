# -*- coding: utf-8 -*-
"""
Created on =2019-01-10

@author: wenshijie
"""
# chapter5
import numpy as np
import random
# 算法 5.1 n皇后问题


def queens(n):
    result = [0]*n

    def _promising(ii):
        k = 0
        switch = True
        while (k < ii) & switch:
            if (result[k] == result[ii]) | (abs(result[k] - result[ii]) == ii - k):
                switch = False
            k += 1
        return switch

    def _queens(i):
        if _promising(i):
            if i == n-1:
                print(result)
            else:
                for j in range(n):
                    result[i+1] = j
                    _queens(i+1)
    _queens(-1)
# 算法 5.1 蒙特卡洛估计


def estimate():
    print()
# 算法 5.3 蒙特卡洛估计（n皇后回溯算法）


def estimate_n_queens(n):
    result = [0]*n

    def _promising(ii):
        k = 0
        switch = True
        while (k < ii) & switch:
            if (result[k] == result[ii]) | (abs(result[k] - result[ii]) == ii - k):
                switch = False
            k += 1
        return switch

    i = -1
    number = 1
    m = 1
    m_prod = 1
    while (m != 0) & (i != n-1):
        m_prod = m_prod * m
        number = number + m_prod * n
        i += 1
        m = 0
        prom_children = []
        for j in range(n):
            result[i] = j
            if _promising(i):
                m += 1
                prom_children.append(j)
        if m != 0:
            j = random.choice(prom_children)
            result[i] = j
    return number
# 算法 5.4 子集之和问题的回溯算法


def sum_of_subsets(w, W):  # a输入数组w，以及最大值W
    w.sort()  # w非递减顺序
    include = ['no']*len(w)
    sum_w = sum(w)

    def _sum_of_subsets(i, weight, total):
        def _promising(k):
            if k < len(w)-1:
                return (weight + total >= W) & ((weight == W) | (weight + w[k + 1] <= W))
            else:
                # 当k等于最后一项是w[k+1]没有值
                return (weight + total >= W) & ((weight == W) | (weight + 0 <= W))
        if _promising(i):
            if weight == W:
                print(include)
            else:
                include[i+1] = 'yes'
                _sum_of_subsets(i+1, weight + w[i+1], total - w[i+1])
                include[i+1] = 'no'
                _sum_of_subsets(i+1, weight, total - w[i+1])
    _sum_of_subsets(-1, 0, sum_w)
# 算法 5.5 m着色问题的回溯算法


def n_color(w, m):  # w为邻近矩阵，m为颜色数量
    n = np.shape(w)[0]  # 顶点个数
    result = [-1]*n  # 顶点处所放的颜色
    all_result = []

    def _promising(i):  # 检查i是否是有希望的
        switch = True
        k = 0
        while (k < i) & switch:
            if w[k][i] & (result[k] == result[i]):
                switch = False
            k += 1
        return switch

    def n_coloring(i):
        if _promising(i):
            if i == n-1:
                all_result.append(result.copy())
            else:
                for color in range(1, m+1):  # m中颜色
                    result[i+1] = color
                    n_coloring(i+1)
    n_coloring(-1)
    if all_result:
        return all_result
    else:
        print('{} 种颜色此图中无解'.format(m))
# 算法 5.6 哈密顿回路问题的回溯算法


def hamiltonian(w):  # 邻近矩阵和起开始顶点a 第i个顶点开始 i = 0,1,2...n-1 一共n个顶点
    n = np.shape(w)[0]
    result = [0]*n  # 默认起始顶点为0
    all_result = []

    def _promising(i):
        if (i == n-1) & (not w[result[i]][result[0]]):  # 第一个顶点必须与最后一个顶点相邻
            switch = False
        elif (i > 0) & (not w[result[i-1]][result[i]]):  # 第 i 个顶点必须与 i-1个顶点相邻
            switch = False
        else:
            switch = True
            j = 1
            while (j < i) & switch:  # 该顶点是否已经被占用
                if result[i] == result[j]:
                    switch = False
                j += 1
        return switch

    def _hamiltonian(i):
        if _promising(i):
            if i == n-1:
                all_result.append(result.copy())
            else:
                for j in range(1, n):  # 0是起点，以后的顶点选取不在0中
                    result[i+1] = j
                    _hamiltonian(i+1)
    _hamiltonian(0)
    if all_result:
        return all_result
    else:
        print('此邻近矩阵代表的无向图没有回路')
# 算法 5.7 0-1背包问题的回溯算法


def knapsack(w, p, W):  # w和p 假设已经按照p[i]/w[i]非递减顺序排列
    n = len(w)
    max_profit = [0]
    best_set = [[]]
    include = ['0']*n

    def _promising(i, profit, weight):
        if weight >= W:
            return False
        else:
            total_weight = weight
            bound = profit
            j = i + 1

            while j < n:
                if total_weight + w[j] <= W:
                    total_weight = total_weight + w[j]
                    bound = bound + p[j]
                else:
                    break
                j += 1
            if j < n:
                bound = bound + (W - total_weight)*p[j]/w[j]
            return bound > max_profit[0]

    def _knapsack(i, profit, weight):
        if(weight <= W) & (profit > max_profit[0]):
            max_profit[0] = profit
            best_set[0] = include[:i+1]
        if _promising(i, profit, weight):
            include[i+1] = 'yes'
            _knapsack(i+1, profit + p[i+1], weight + w[i+1])
            include[i+1] = 'no'
            _knapsack(i + 1, profit, weight)
    _knapsack(-1, 0, 0)
    return max_profit[0], best_set[0]


if __name__ == '__main__':
    # print(queens(6))
    # print(estimate_n_queens(4))
    w = [5, 6, 10, 11, 16]
    print(sum_of_subsets(w, 21))
    # w1 = np.array([[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]])
    # print(n_color(w1, 3))
    # print(hamiltonian(w1))
    # print(knapsack([2, 5, 10, 5], [40, 30, 50, 10], 16))
