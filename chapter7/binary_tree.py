# -*- coding: utf-8 -*-
"""
Created on =2019-01-15

@author: wenshijie
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left_children = None
        self.right_children = None


if __name__ == '__main__':
    p = Node(9)
    print(p.value)
