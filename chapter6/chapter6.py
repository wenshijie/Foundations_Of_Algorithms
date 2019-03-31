# -*- coding: utf-8 -*-
"""
Created on =2019-01-13

@author: wenshijie
"""
# chapter6
import numpy as np
# 算法 6.1 0-1背包问题的宽度优先查找


def knapsack2(w, p, w_max):  # w为每个物品的重量，p为每个物品的价值。分别按照p/w非递减排列，w_max为最大容许重量
    n = len(w)
    queue = [[-1, 0, 0]]  # 创建一个队列,并初始化令，第一项为节点水平，第二，三项为当前节累积的价值和重量,
    max_profit = 0        # 由于w和p的下标是从零开始的故初始level用-1

    def bound(lev, pro, wei):
        if wei >= w_max:
            return 0
        else:
            expect_profit = pro
            j = lev + 1
            total_weight = wei
            while j < n:
                if total_weight + w[j] <= w_max:
                    total_weight = total_weight + w[j]
                    expect_profit = expect_profit + p[j]
                    j += 1
                else:
                    break
            if j < n:
                expect_profit = expect_profit + (w_max - total_weight)*p[j]/w[j]
            return expect_profit
    while queue:
        level = queue[0][0] + 1  # 设定下一个节点的水平
        profit = queue[0][1] + p[level]
        weight = queue[0][2] + w[level]
        if (profit > max_profit) & (weight <= w_max):
            max_profit = profit
        if bound(level, profit, weight) > max_profit:
            queue.append([level, profit, weight])
        profit = queue[0][1]
        weight = queue[0][2]
        if bound(level, profit, weight) > max_profit:
            queue.append([level, profit, weight])
        del queue[0]
    return max_profit
# 算法 6.2 0-1背包问题带有分支定界修剪算法的最佳优先查找


def knapsack3(w, p, w_max):  # w为每个物品的重量，p为每个物品的价值。分别按照p/w非递减排列，w_max为最大容许重量
    n = len(w)
    max_profit = 0

    def insert(s):  # s = [level, profit, weight, bound_value]
        m = len(queue)

        def _insert(low, high):
            if high >= low:
                mid = int((low+high)/2)
                if s[3] <= queue[mid][3]:
                    _insert(mid+1, high)
                else:
                    _insert(low, mid-1)
            else:
                queue.insert(low, s)
        _insert(0, m-1)

    def bound(lev, pro, wei):
        if wei >= w_max:
            return 0
        else:
            expect_profit = pro
            j = lev + 1
            total_weight = wei
            while j < n:
                if total_weight + w[j] <= w_max:
                    total_weight = total_weight + w[j]
                    expect_profit = expect_profit + p[j]
                    j += 1
                else:
                    break
            if j < n:
                expect_profit = expect_profit + (w_max - total_weight)*p[j]/w[j]
            return expect_profit

    queue = [[-1, 0, 0, bound(-1, 0, 0)]]  # 创建一个队列,并初始化令，第一项为节点水平，第二，三项为当前节累积的价值和重量,
    # 由于w和p的下标是从零开始的故初始level用-1,增加界限
    while queue:
        if queue[0][3] > max_profit:
            level1 = queue[0][0] + 1  # 设定下一个节点的水平
            profit1 = queue[0][1] + p[level1]
            weight1 = queue[0][2] + w[level1]
            bound_value1 = bound(level1, profit1, weight1)
            if (profit1 > max_profit) & (weight1 <= w_max):
                max_profit = profit1
            profit2 = queue[0][1]
            weight2 = queue[0][2]
            bound_value2 = bound(level1, profit2, weight2)
            del queue[0]
            if bound_value1 > max_profit:
                insert([level1, profit1, weight1, bound_value1])
            if bound_value2 > max_profit:
                insert([level1, profit2, weight2, bound_value2])
        else:
            del queue[0]
    return max_profit
# 算法 6.3 旅行推销员问题带分支定界的修剪的最佳优先查找算法


def get_item(s1, s2):  # 得到在s1中但不在s2中的值
    s = []
    for item in s1:
        if item not in s2:
            s.append(item)
    return s


def travel2(w):  # w 邻近矩阵
    n = np.shape(w)[0]
    point = list(range(n))  # 第一个顶点是0
    min_length = 1000  # 初始最短路劲无穷大
    opt_tour = [[]]

    def length(s):
        m = len(s)
        all_length = 0
        for j in range(m-1):
            all_length = all_length + w[s[j]][s[j+1]]
        return all_length

    def bound(path):
        b1 = length(path)
        others_point = get_item(point, path)
        b2 = min([w[path[-1]][j] for j in others_point])
        b3 = 0
        for ii in others_point:
            s = []
            for jj in others_point:
                if ii != jj:
                    s.append(w[ii][jj])
            b3 = b3 + min(min(s), w[ii][0])
        return b1 + b2 + b3

    def insert(s):  # s = [path ,level, bound_value]
        m = len(queue)

        def _insert(low, high):
            if high >= low:
                mid = int((low+high)/2)
                if s[2] >= queue[mid][2]:
                    _insert(mid+1, high)
                else:
                    _insert(low, mid-1)
            else:
                queue.insert(low, s)
        _insert(0, m-1)

    queue = [[[0], 0, bound([0])]]  # 路径起始0 level 和界限,
    while queue:
        queue_tmp = queue.pop(0)
        if queue_tmp[2] < min_length:  # 界限（下界）小于某一条最小路径是展开，才有可能找到更小的，
            level = queue_tmp[1] + 1   # 下界大于当前最小的话，肯定不会更小了
            for item in point[1:]:  # 去除第一个起始顶点
                if item not in queue_tmp[0]:
                    path = queue_tmp[0] + [item]  # .append 会改变原列表
                    if level == n-2:
                        path.append(get_item(point, path)[0])
                        path.append(0)  # 把起始顶点加上去
                        if length(path) < min_length:
                            min_length = length(path)
                            opt_tour[0] = path.copy()
                    else:
                        bound_value = bound(path)
                        if bound_value < min_length:
                            insert([path, level, bound_value])
    return min_length, opt_tour[0]
# 算法 6.4


if __name__ == '__main__':
    # print(knapsack3([2, 5, 10, 5], [40, 30, 50, 10], 16))
    # get_item([1, 3, 2], [1, 2])
    w = np.array([[0, 14, 4, 10, 20], [14, 0, 7, 8, 7], [4, 5, 0, 7, 16], [11, 7, 9, 0, 2], [18, 7, 17, 4, 0]])
    print(travel2(w))