# -*- coding: utf-8 -*-
"""
Created on =2019-01-17

@author: wenshijie
"""
# chapter11
# 算法 11.1 欧式算法


def gcd(n, m):
    """

    :param n: int
    :param m: int
    :return: int
    """
    if m == 0:
        return n
    else:
        return gcd(m, n % m)
# 算法 11.2 欧式算法2


def euclid(n, m):
    """

    :param n: int
    :param m: int
    :return: gcd, i, j
    """
    if m == 0:
        gcd, i, j = n, 1, 0
        return gcd, i, j
    else:
        gcd1, i1, j1 = euclid(m, n%m)
        gcd = gcd1
        i = j1
        j = i1 - int(n/m)*j1
        return gcd, i, j
# 算法 11.3 求解模线性方程


def solve_liners(n, m, k):
    gcd, i, j = euclid(n, m)
    result = []
    if k % gcd == 0:
        for l in range(gcd):
            result.append([j*k/gcd+l*n/gcd])
    return result
# 算法 11.4 计算模的幂


def compute_power(n, m, k):
    a = 1
    b = list(bin(k))[2:]
    for v in b:
        a = a**2
        if v == '1':
            a = a*m
            while a >= n:
                a = a - n
            # print(a)
        else:
            while a >= n:
                a = a - n
            # print(a)
    return a




if __name__ == '__main__':
    # print(gcd(30, 18))
    # print(euclid(30, 18))
    print(compute_power(257, 5, 45))