# -*- coding: utf-8 -*-
"""
Created on =2019-01-08

@author: wenshijie
"""
import numpy as np

# chapter4
# 算法 4.1 prim 算法


def prim(w):  # 输入距离矩阵
    global v_near
    n = np.shape(w)[0]
    w = np.insert(w, 0, [0]*n, 0)  # 给行插入一行0在第一行
    w = np.insert(w, 0, [0]*(n+1), 1)  # 插入一列0在第一列 仅仅为了使的索引的点相对应
    # print(w)
    m = np.shape(w)[0]  # m = n+1  比顶点数多1
    nearest = [0]*m  # 默认第一个点为初始顶点，所以从第二个点开始索引为2
    distance = [-1]*m  #
    f = []  # 边的集合
    k = n-1
    for i in range(2, m):
        nearest[i] = 1  # 当前的distance都是距离V1的距离
        distance[i] = w[1][i]  # 此时各点离顶点集合最近的距离就是各顶点距离点1的距离
    while k > 0:
        min_value = 1000  # 没有路径，代表无穷大
        for i in range(2, m):
            if (distance[i] >= 1) & (distance[i] < min_value):  # 下限可以是0，可以是1，因为当i=v_near时distance[v_near]=-1
                min_value = distance[i]
                v_near = i
        f.append((nearest[v_near], v_near))
        distance[v_near] = -1  # 将v_near为索引的点加入Y中，即令该点距离小雨0，则上述判断就不会成立
        for j in range(2, m):
            if w[j][v_near] < distance[j]:
                distance[j] = w[j][v_near]
                nearest[j] = v_near  # 此时距离如果j 是距离Y最近的点，那么该点是距离v_near最近。
        k -= 1
    return f
# 算法 4.2 kruskal


def edge(w):  # 给一个无向连通矩阵,返回非递减的边信息
    n = np.shape(w)[0]
    edge_list = []
    for i in range(n-1):
        for j in range(1, n-1):
            if i+j < n:
                edge_list.append((w[i][i+j], i+1, i+j+1))
    edge_list.sort()
    return edge_list


def kruskal(w):
    n = np.shape(w)[0]
    u = list(range(n+1))  # 第一项索引为零所以生成n+1个
    edge_list = edge(w)
    result = []

    def find(i):  # 找出i所在的集合（最小的i值）
        while u[i] != i:
            i = u[i]
        return i

    def merge(p, q):
        if p < q:  # p指向合并后的集合，q不在指向一个集合
            u[q] = p
        else:  # q指向合并后的集合，p不在指向一个集合
            u[p] = q

    j = 0  # 从权重最小的边开始
    while len(result) < n-1:
        (long, v_little, v_large) = edge_list[j]
        q = find(v_little)
        p = find(v_large)
        if q != p:
            merge(p, q)
            result.append(edge_list[j])
        j = j + 1
    return result
# 4.3 Dijkstra 算法


def dijkstra(w):
    global v_near
    n = np.shape(w)[0]
    touch = list(range(n+1))
    length = list(range(n+1))
    result = []
    for i in range(2, n+1):
        touch[i] = 1  # 开始时距离都是各点到点1的距离
        length[i] = w[0][i-1]
    k = n-1
    while k > 0:
        min_value = 1000
        for i in range(2, n+1):
            if ((length[i]) > 0) & (length[i] < min_value):
                min_value = length[i]
                v_near = i
        result.append((min_value, touch[v_near], v_near))
        for i in range(2, n+1):
            if length[v_near] + w[v_near-1][i-1] < length[i]:
                length[i] = length[v_near] + w[v_near-1][i-1]
                touch[i] = v_near
        length[v_near] = -1  # 因为它的值前面更新距离需要故最后才除去
        k = k - 1
    return result
# 4.4 带有最终期限的调度安排


def schedule(s):  # s已经更具收益非递减排序
    n = len(s)  # 总的任务数量
    s = [0] + s  # 在s前面加上0项，适任务和索引相同
    list_j = [1]  # 把第一项添加进数组
    deadline_work = [(s[1], 1)]
    for i in range(2, n+1):
        sort_list = deadline_work+[(s[i], i)]
        sort_list.sort()
        deadline = [item[0] for item in sort_list]
        tmp = True
        for ii in range(len(deadline)):
            if deadline[ii] < ii+1:
                tmp = False
        if tmp:
            deadline_work[:] = sort_list.copy()
            list_j[:] = [item[1] for item in sort_list]
    return list_j
# 0-1背包问题的动态规划算法


def bag01(w, p, W):  # w为物品的重量，p为对应物品的价值，W为背包的最大容量 W 为整数
    p = [0] + p  # 将下标与物品对应i指代第i个物品的价值
    w = [0] + w  # 将下标与物品对应i指代第i个物品的重量
    m = len(p)  # m = n + 1 n为物品的个数
    max_p = np.zeros((len(p), W+1))
    for i in range(1, m):
        for j in range(1, W + 1):
            if w[i] > j :
                max_p[i][j] = max_p[i-1][j]
            else:
                max_p[i][j] = max(max_p[i-1][j], p[i] + max_p[i-1][j-w[i]])
    return max_p[m-1][W]


if __name__ == '__main__':
    w = np.array([[0, 1, 3, 20, 20], [1, 0, 3, 6, 20], [3, 3, 0, 4, 2], [20, 6, 4, 0, 5], [20, 20, 2, 5, 0]])
    w1 = np.array([[0, 7, 4, 6, 1], [20, 0, 20, 20, 20], [20, 2, 20, 20, 20], [20, 3, 20, 0, 20], [20, 20, 20, 1, 0]])
    deadline = [3, 1, 1, 3, 1, 3, 2]
    w3 = [2, 1, 4, 3]
    p = [9, 8, 7, 6]
    W = 10
    # print(prim(w))
    # print(kruskal(w))
    # print(dijkstra(w1))
    # print(schedule(deadline))
    print(bag01(w3, p, W))