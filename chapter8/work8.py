# -*- coding: utf-8 -*-
"""
Created on =2019-01-15

@author: wenshijie
"""
# work8
import random
from bin_search_tree.bin_search_tree import Node
from bin_search_tree.bin_search_tree import BST
# preparations


def make_bin_search_tree(s: list, p: BST= None)->'return tree':  # 可以给一个二叉查找树，也可以直接生成
    # 最好列表的第一项不要偏离中值太远，要不然树会严重倾斜，也可以给一个合适的值令p = BST（value）
    if p:
        for i in s:
            p.insert(i)
    else:
        p = BST()
        for i in s:
            p.insert(i)
    return p
# 8.10 找出二叉查找树的最大键


def find_max(p):  # p是一个二叉查找树的根节点
    # 二叉查找树大于根节点的在右子节点小于根节点的在左子节点
    if p.right_child is None:
        if p.value is None:
            return 'root is nothing'
        else:
            return p.value
    else:
        return find_max(p.right_child)
# 8.12 见bin_search_tree.bin_search_tree
# 8.13 见bin_search_tree.B_tree
# 8.14 见bin_search_tree.B_tree
# 8.34 编写一个概率算法，判断是否为质数，或为合数


def prime(x):
    part = [[2, int(x/2)]]
    switch = True
    while part and switch:
        value = part.pop(0)
        if value[1] - value[0] >= 0:
            r = random.randint(value[0], value[1])
            if x % r == 0:
                switch = False
            if value[1] - value[0] > 0:
                part.append([value[0], int((value[0]+value[1])/2)])
                part.append([int((value[0]+value[1])/2)+1, value[1]])
    if not switch:
        return switch, r
    else:
        return switch





if __name__ == '__main__':
    # print(a.value)
    # s = [9, 4, 3, 7, 5, 10, 14, 18, 8]
    # r = make_bin_search_tree(s)  # 最好列表的第一项不要偏离中值太远，要不然树会严重倾斜，也可以给一个合适的值令p = BST（value）
    # print(find_max(r.root))
    # a = Node(8)
    # a.right_child = Node(5)
    # b = a.right_child.value
    # del a.right_child
    # print(b)
    # print(a.left_child)
    print(prime(11))

