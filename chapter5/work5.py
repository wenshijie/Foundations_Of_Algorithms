# -*- coding: utf-8 -*-
"""
Created on =2019-01-11

@author: wenshijie
"""
import numpy as np
# work5
# 5.3.1 第一种使用过程的expand的写法，为n皇后问题编写回溯算法


def queens(n):
    result = [0]*n
    all_result = []

    def _queens(i):  # 这种写法把_promising()函数写到里面，每调用一次就会有一个新的i作为该次调用的全局变量
        def _promising(jj):
            switch = True
            k = 0
            while (k < i) & switch:
                if (result[k] == jj) | (abs(result[k] - jj) == i - k):
                    switch = False
                k += 1
            return switch
        for j in range(n):  # 对所有子节点准备执行放入操作
            if _promising(j):  # 如果j可以放入
                result[i] = j
                if i == n-1:
                    all_result.append(result.copy())
                else:
                    _queens(i+1)
    _queens(0)
    return all_result
# 5.3.2 第二种写法


def queens1(n):
    result = [0]*n
    all_result = []

    def _promising(i, j):  # 这种写法把_promising()函数写到外面，每次调用吧节点i参数传进去
        switch = True
        k = 0
        while (k < i) & switch:
            if (result[k] == j) | (abs(result[k]-j) == i-k):
                switch = False
            k += 1
        return switch

    def _queens(i):
        for j in range(n):  # 对所有子节点准备执行放入操作
            if _promising(i, j):  # 如果j可以放入
                result[i] = j
                if i == n-1:
                    all_result.append(result.copy())
                else:
                    _queens(i+1)
    _queens(0)
    return all_result
# 5.4 把满足条件加到列表里改成加1 即可最后输出多少种解
# 5.7 跟踪已经受控制的列集和左对角线右对角线集（不知道对角线该怎么表示(-->__-->）

'''
def queens_set(n):
    result = [0]*n
    columns = []
    left_diagonals = []
    right_diagonals = []

    def _promising(ii):
        k = 0
        switch = True
        while (k < ii) & switch:
            if (result[k] == result[ii]) | (abs(result[k] - result[ii]) == ii - k):
                switch = False
            k += 1
        if (ii >= 0) & switch:
            columns.append(result[ii])  # 列放入
            if ii == result[ii]:  # 这里用对角线的第一个元素位置来表示对角线
                left_diagonals.append((1, 1))
            
        return switch

    def _queens(i):
        if _promising(i):
            if i == n-1:
                print(result)
            else:
                for j in range(n):
                    result[i+1] = j
                    # print(result)
                    _queens(i+1)
    _queens(-1)
'''
#  5.8 修改n皇后问题使之仅给出一个解


def queens_one_result(n):
    result = [0]*n
    all_result = []

    def _promising(ii):
        k = 0
        switch = True
        while (k < ii) & switch:
            if (result[k] == result[ii]) | (abs(result[k] - result[ii]) == ii - k):
                switch = False
            k += 1
        return switch

    def _queens(i):
        if not all_result:  # 还没有答案就接着找，有的话就不再找了
            if _promising(i):
                if i == n-1:
                    all_result.append(result.copy())
                    # print(result)
                else:
                    for j in range(n):
                        result[i+1] = j
                        _queens(i+1)
    _queens(-1)
    return all_result
# 5.15 对事先没有对重量排序的“自己之和”问题编写一种回溯算法
# 没有排序的话只能有现在的重量是否小于等于W和现在重量加上余下的重量是否大于等于W


def sum_set(w, value):  # 未排序的w
    n = len(w)
    include = ['no']*n
    all_result = []

    def _promising(weight, total_weight):
        switch = True
        if (weight > value) | (weight + total_weight < value):
            switch = False
        return switch

    def _sum_set(i, weight, total_weight):
        if _promising(weight, total_weight):
            if weight == value:
                all_result.append(include.copy())
                # print(include)
            else:
                if i < n-1:
                    include[i+1] = 'yes'
                    _sum_set(i+1, weight + w[i+1], total_weight - w[i+1])
                    include[i+1] = 'no'
                    _sum_set(i+1, weight, total_weight)
    _sum_set(-1, 0, sum(w))
    return all_result
# 5.16 修改子集之和算法使其只输出一个满足条件的解


def sum_of_subsets_one(w, W):  # a输入数组w，以及最大值W
    w.sort()
    n = len(w)
    include = ['no']*n
    all_result = []

    def _promising(i, weight, total_weight):
        if i < n-1:
            return (weight + total_weight >= W) & ((weight == W) | (weight + w[i + 1] <= W))
        if i == n-1:
            return (weight + total_weight >= W) & ((weight == W) | (weight + 0 <= W))

    def _sum_of_subsets_one(i, weight, total_weight):
        if not all_result:
            if _promising(i, weight, total_weight):
                if weight == W:
                    all_result.append(include.copy())  # 如果变长列表把include.copy()换成include[:i+1]
                else:
                    include[i+1] = 'yes'
                    _sum_of_subsets_one(i+1, weight + w[i+1], total_weight - w[i+1])
                    include[i+1] = 'no'
                    _sum_of_subsets_one(i+1, weight, total_weight-w[i+1])
    _sum_of_subsets_one(-1, 0, sum(w))
    return all_result
# 5.19 使用贪婪算法每次用一种颜色为尽可能多的为着色顶点进行着色


def colors(w, m):  # w为邻近矩阵，m为颜色的种类
    n = np.shape(w)[0]
    color = [-1]*n  # 第i个点的颜色种类
    point_list = list(range(n))

    def _promising(kj, s):  # 判断某个点kj是否可以放入颜色ki
        switch = True
        for v in s:
            if w[v][kj]:
                switch = False
        return switch

    for i in range(m):  # 依次选取颜色
        if not point_list:
            print('{}个点着色完成共使用{}种颜色，还剩余{}种颜色'.format(n, i, m-i))
            break
        else:
            have_i_color = []  # 当前第i种色的顶点的索引
            for j in point_list:  # 依次查看顶点j是否可以着第i种色
                if (color[j] < 0) & _promising(j, have_i_color):
                    color[j] = i
                    have_i_color.append(j)
            for vv in have_i_color:
                point_list.remove(vv)
            if i == m-1:
                if point_list:  # 未着色的顶点不为空,为空时是False
                    print('用完{}种颜色为{}个顶点着色,还有{}个点未着色'.format(m, n-len(point_list), len(point_list)))
                else:
                    print('恰好用完{}种颜色为{}个顶点着色'.format(m, n))
    return color
# 5.21 贪婪算法的图着色问题不能给出最优解
# 5.29 chapter5中改一下即可
# 5.36 应该是只有向有移动时才需要计算界限bound，向左移动时是不需要计算界限的。但是都要判断是否大于W，
# 所以应该只有计算bound可以减少计算量


def knapsack(w, p, W):  # w和p 假设已经按照p[i]/w[i]非递减顺序排列
    n = len(w)
    max_profit = [0]
    best_set = [[]]
    include = ['no']*n
    bound = [0]

    def _promising(i, profit, weight):
        if weight >= W:
            return False
        else:
            if (include[i] == 'no') | (i < 0):
                total_weight = weight
                bound[0] = profit
                j = i + 1
                while j < n:
                    if total_weight + w[j] <= W:
                        total_weight = total_weight + w[j]
                        bound[0] = bound[0] + p[j]
                    else:
                        break
                    j += 1
                if j < n:
                    bound[0] = bound[0] + (W - total_weight)*p[j]/w[j]
                return bound[0] > max_profit[0]
            else:
                return bound[0] > max_profit[0]  # 向右移动时最大界限不改变

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
# 5.40 n的三次方


def queens3(n):
    result = [0]*n
    result1 = [0]*n
    result2 = [0]*n
    all_result = []

    def _promising(ii):
        k = 0
        switch = True
        while k < ii:
            if (abs(result[k]-result[ii])== abs(result1[k]-result1[ii])) |\
                (abs(result[k] - result[ii]) == abs(result2[k]-result2[ii])) | \
                    (abs(result1[k] - result1[ii]) == abs(result2[k] - result2[ii])):
                switch = False
            k += 1
        return switch

    def _queens(i):
        if _promising(i):
            if i == n-1:
                last_result = [(result[i], result1[i], result2[i]) for i in range(n)]
                all_result.append(last_result)
            else:
                for j in range(n):
                    for j1 in range(n):
                        for j2 in range(n):
                            result[i+1] = j
                            result1[i+1] = j1
                            result2[i+1] = j2
                            _queens(i+1)
    _queens(-1)
    return len(all_result), all_result
# 5.41 见5.16


if __name__ == '__main__':
    # print(queens(5))
    # w = [5, 6, 10, 11, 16]
    # print(sum_of_subsets_one(w, 21))
    # w1 = np.array([[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]])
    # print(colors(w1, 4))
    # print(knapsack([2, 5, 10, 5], [40, 30, 50, 10], 16))
    print(queens3(4))