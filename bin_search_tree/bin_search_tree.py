# -*- coding: utf-8 -*-
"""
Created on =2019-01-16

@author: wenshijie
"""


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class BST(object):
    def __init__(self, value=None):
        self.root = Node(value)
        self.in_orders = []

    def find_item(self, value, node=None, parent=None, node_type=None):  # 默认从根节点开始搜索
        if (node is None) & (node_type is not None):  # 节点可能也是空，但有类型子节点或根节点
            return False, node, parent, node_type
        elif (node is None) & (node_type is None):  # 类型为空，节点为空，查找时不知道节点值
            node = self.root  # 如果开始搜索的节点没有给出，默认重根节点开始。用于查找时的判断，查找时可能不知道二叉树的根节点
            node_type = 'root'
            if node.value is None:  # 0根节点的值是空，直接返回结果或插入位子
                return False, node, parent, node_type
            else:
                if value == node.value:
                    return True, node, parent, node_type
                elif value < node.value:
                    return self.find_item(value, node.left_child, node, 'left_child')
                else:
                    return self.find_item(value, node.right_child, node, 'right_child')
        else:  # 节点不为空
            if value == node.value:
                return True, node, parent, node_type
            elif value < node.value:
                return self.find_item(value, node.left_child, node, 'left_child')
            else:
                return self.find_item(value, node.right_child, node, 'right_child')

    def insert(self, value):
        if self.root.value is None:
            self.root = Node(value)  # 如果跟节点没有值直接插入到跟节点
        else:
            # 默认从根节点开始查找插入
            result, node, parent, node_type = self.find_item(value, self.root, None, 'root')  # 插入相同的元素会被替换掉
            if node_type == 'left_child':
                parent.left_child = Node(value)
                parent.left_child.parent = parent
            else:
                parent.right_child = Node(value)
                parent.right_child.parent = parent

    def in_order(self, node=None):  # 中序遍历
        ss = []
        if node is None:  # 如果节点为空 默认从根节点开始
            node = self.root

        def _in_order(node):
            if node:
                _in_order(node.left_child)
                ss.append(node.value)
                _in_order(node.right_child)

        _in_order(node)
        return ss

    def find_max(self, node):  # 查找当前节点树的最大值
        if node.right_child is None:
            if node.value is None:
                print('root is nothing')
            else:
                return node
        else:
            return self.find_max(node.right_child)

    def delete(self, value):
        result, node, parent, node_type = self.find_item(value, self.root, None, 'root')
        if result:
            if (node.left_child is not None) & (node.right_child is not None):
                node_tmp = self.find_max(node.left_child)
                node.value = node_tmp.value
                self.delete(node_tmp.value)
            elif (node.left_child is None) & (node.right_child is None):
                if node_type == 'left_child':
                    parent.left_child = None
                else:
                    parent.right_child = None
                del node
            else:
                if (node.left_child is None) & (node.right_child is not None):
                    if node_type == 'left_child':
                        parent.left_child = node.right_child
                    else:
                        parent.right_child = node.right_child
                else:
                    if node_type == 'left_child':
                        parent.left_child = node.left_child
                    else:
                        parent.right_child = node.left_child
                print(parent.right_child.value)
                del node








if __name__ == '__main__':
    # node = Node()
    # print(node.value, node.left_child, node.right_child)
    b = BST()
    b.insert(5)
    b.insert(2)
    b.insert(3)
    b.insert(1)
    b.insert(6)
    b.insert(7)
    print(b.root.value , b.root.left_child.left_child.parent.value)
    print(b.in_order(b.root))
    b.delete(6)
    print(b.in_order(b.root))