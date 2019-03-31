# -*- coding: utf-8 -*-
"""
Created on =2019-01-18

@author: wenshijie
"""
# work 11
# 编写算法11.1 的迭代版本


def gcd2(n, m):
    r = m
    while r != 0:
        r = n % m
        n = m
        m = r
    return n
#  11.18 略


if __name__ == '__main__':
    print(gcd2(30, 16))
