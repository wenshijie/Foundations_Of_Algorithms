# -*- coding: utf-8 -*-
"""
Created on =2019-01-08

@author: wenshijie
"""
# work4
import numpy as np
from linklist import Node

# 4.6 修改prim算法无向加权图是否是连通图


def connected(w):  # w 为无向加权图的权重矩阵
    global v_near
    n = np.shape(w)[0]  # 顶点数
    w1 = np.insert(w, 0, [0] * n, 0)  # 首行加一行0
    w1 = np.insert(w1, 0, [0] * (n + 1), 1)  # 首列加一列0，使得索引与顶点相同
    distance = [0]*(n+1)  # 假
    m = 19  # 用来表示距离的最大值 大于该值说明，没有通道
    for i in range(2, n+1):
        if w1[1][i] < m:
            distance[i] = 1  # 说明i 可以到达1
    k = n-1
    while k > 0:  # 重复n-1 次
        for i in range(2, n+1):
            if distance[i] == 1:
                v_near = i
        distance[v_near] = -1
        for j in range(2, n+1):
            if (w1[v_near][j] < m) & (distance[j] == 0):
                distance[j] = 1
        k -= 1
    if sum(distance) == -(n-1):
        return 'True'
    else:
        return 'False'
# 4.15 见chapter4 已经加了最短路径的长度
# 4.16 不会，写一个其他的判断，从图中依次删去其它点都不能直接到达的顶点
# （有向图中A到B，B到A是一个环），然后删去与该顶点相关的边


def cycle(w):  # 有向图的邻近矩阵 第i行j列是从带点i+1到点j+1 ,为了方便吧对角线上的值和无穷大的值都设置为0，不能到达
    global result
    n = len(w)
    p = w.copy()
    m = np.shape(p)[0]
    delete_list = []
    k = 0
    while k <= n-1:
        for j in range(m):
            tmp = True
            for i in range(m):
                if p[i][j] == 0:
                    continue
                else:
                    if p[j][i] != 0:
                        continue
                    else:
                        tmp = False
                        break
            if tmp:
                delete_list.append(j)
        p = np.delete(p, delete_list, 0)
        p = np.delete(p, delete_list, 1)
        m = np.shape(p)[0]
        if m == 0:
            result = 'no cycle'
            break
        if (m != 0) & (len(delete_list) == 0):
            result = 'have cycle'
            break
        k += 1
    return result
# 4.21


def work(s, k):  # k个服务者，s为任务的集合
    n = len(s)
    i = 0
    m = 1
    while i < n:
        if m <= k:
            print('{} work to server {}'.format(i+1, k))
            k = k + 1
            i = i + 1
        else:
            k = 1
# 4.31 霍夫曼算法，编码 #####本例子不能输入某个频率和字符进行只得到某一个字符的编码，因为对于频率相同
# 如果是两个有可能在不同的高度例如频率 1,3,3... 或3,3,3....如果只想得到某些字符的编码，
# 可以在Node类(linklist.py)里面添加父节点从字符的叶节点向上查找知道跟节点


def huffman(s):  # s为列表列表里的元素是由频率以及对应的字符[(频率，字符)]
    s.sort()
    n = len(s)
    pq = []
    for i in range(n):
        a = Node(s[i][0])
        a.symbol = s[i][1]
        pq.append(a)

    def insert(ss, rr):  # 为rr找出插入位置使得ss是按里面元素的频率从小到大排序
        long = len(ss)

        def _insert(low, high):
            if low > high:
                ss.insert(low, rr)
            else:
                mid = int((low+high)/2)
                if rr.frequency <= ss[mid].frequency:
                    _insert(low, mid-1)
                else:
                    _insert(mid+1, high)
        _insert(0, long - 1)

    k = 1
    while k <= n-1:
        r = Node(pq[0].frequency+pq[1].frequency)
        r.left = pq[0]
        r.right = pq[1]
        del pq[0]
        del pq[0]
        insert(pq, r)
        k += 1
    r = pq[0]
    # return r  # 霍夫曼树根节点
    result_code = []

    def _get_huffman_code(node, code_value=[]):  # 得到各个字符的编码
        if node.symbol is not None:
            # print(''.join(code_value), node.symbol)  # 编码结果
            result_code.append((''.join(code_value), node.symbol))
        else:
            _get_huffman_code(node.left, code_value + ['0'])
            _get_huffman_code(node.right, code_value + ['1'])
    _get_huffman_code(r, [])
    return result_code
# 4.35 为0-1背包问题编写动态规划算法（见chapter4里面已经有了）



if __name__ == '__main__':
    # w connected
    # w = np.array([[0, 1, 3, 20, 20], [1, 0, 3, 6, 20], [3, 3, 0, 4, 2], [20, 6, 4, 0, 5], [20, 20, 2, 5, 0]])
    # w1 no-connected
    # w1 = np.array([[0, 1, 3, 20, 20], [1, 0, 3, 6, 20], [3, 3, 0, 4, 20], [20, 6, 4, 0, 20], [20, 20, 20, 20, 0]])
    # print(connected(w1))
    w2 = np.array([[0, 7, 4, 6, 1], [0, 0, 0, 0, 0], [0, 2, 0, 5, 0], [1, 3, 0, 0, 0], [0, 0, 0, 1, 0]])
    s = [(2, 'a'), (3, 'b'), (7, 'c'), (8, 'd'), (9, 'e')]
    s1 = [(5, 'b'), (5, 'e'), (5, 'c'), (16, 'a'), (17, 'd'), (25, 'f')]  # 频率相同的要看初始给他们的顺序决定编码长度
    print(huffman(s))
    # print(huffman(s1))
    # print(cycle(w2))
