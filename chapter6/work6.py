# -*- coding: utf-8 -*-
"""
Created on =2019-01-13

@author: wenshijie
"""
# work6
# 修改算法6.1 生成最优物品集合


def knapsack2(w, p, w_max):  # w为每个物品的重量，p为每个物品的价值。分别按照p/w非递减排列，w_max为最大容许重量
    n = len(w)
    queue = [[-1, 0, 0, []]]  # 创建一个队列,并初始化令，第一项为节点水平，第二，三项为当前节累积的价值和重量,最优集合
    max_profit = 0        # 由于w和p的下标是从零开始的故初始level用-1
    best_set = []

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
        best_set_tmp = queue[0][3]+[level]
        if (profit > max_profit) & (weight <= w_max):
            max_profit = profit
            best_set = best_set_tmp.copy()
        if bound(level, profit, weight) > max_profit:
            queue.append([level, profit, weight, best_set_tmp])
        profit = queue[0][1]
        weight = queue[0][2]
        if bound(level, profit, weight) > max_profit:
            queue.append([level, profit, weight, queue[0][3].copy()])
        del queue[0]
    return max_profit, best_set
# 6.9 见chapter6
# 6.18 为带有最终期限的调度安排编写分支定界算法


def schedule(d, p):  # d是最终期限,按非递减顺序排列,p为相应的价值顺序
    max_value = 0
    best_set = [[]]

    def bound(lev, pro):
        b = pro + sum(p[lev+1:])
        return b

    def insert(s):  # s = [level, path, profit, deadline, bound]
        m = len(queue)

        def _insert(low, high):
            if high >= low:
                mid = int((low+high)/2)
                if s[4] <= queue[mid][4]:
                    _insert(mid+1, high)
                else:
                    _insert(low, mid-1)
            else:
                queue.insert(low, s)
        _insert(0, m-1)
    queue = [[-1, [], 0, [], bound(-1, 0)]]  # [level, path, profit, deadline, bound]

    while queue:
        queue_tmp = queue.pop(0)
        if queue_tmp[4] > max_value:
            level = queue_tmp[0] + 1
            path_tmp = queue_tmp[1] + [level]
            profit = queue_tmp[2] + p[level]
            dead_line = queue_tmp[3] + [d[level]]
            if dead_line[-1] >= len(dead_line):  # 新加入的最终期限大于安排时间即可
                insert([level, path_tmp, profit, dead_line, bound(level, profit)])  # 选择level的点
                if profit > max_value:
                    max_value = profit
                    best_set[0] = path_tmp.copy()
            insert([level, queue_tmp[1], queue_tmp[2], queue_tmp[3], bound(level, queue_tmp[2])])  # 不选择level的点
    return max_value, best_set


if __name__ == '__main__':
    # print(knapsack2([2, 5, 10, 5], [40, 30, 50, 10], 16))
    d = [1, 1, 1, 2, 3, 3, 3, 3]
    p = [35, 30, 20, 10, 40, 25, 15]
    print(schedule(d, p))