# -*- coding: utf-8 -*-
"""
Created on =2019-01-09

@author: wenshijie
"""


class Node:
    def __init__(self, value):
        self.symbol = None
        self.frequency = value
        self.left = None
        self.right = None


if __name__ == '__main__':
    a = [(1,2),(3,4),(5,6)]
    s = [0,0]
    s[0] = Node(5)
    s[0].symbol = 'a'
    print(s)




