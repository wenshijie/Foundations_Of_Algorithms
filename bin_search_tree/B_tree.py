# -*- coding: utf-8 -*-
"""
Created on =2019-01-19

@author: wenshijie
"""


class Node:
    def __init__(self, small=None, large=None):
        self.small = small
        self.large = large
        self.left_children = None
        self.middle_children = None
        self.right_children = None
        self.parent = None


class Tree23:
    def __init__(self):  # 这里我们使只有一个节点值时其值放在small
        self.root = Node()

    def find(self, value, node, parent, node_type):  # 查找应该插入的位置
        if (node.small is None) and (node.large is None):  # 节点中没有值,应该只有根节点才会执行此步
            return node, parent, node_type
        elif (node.small is not None) and (node.large is not None):  # 节点种有两个值
            if node.left_children is None:  # 如果有两个值而且叶节点为空，则当前为叶节点
                return node, parent, node_type
            else:  # 如果不为空则三个叶节点都不为空
                if value <= node.small:
                    return self.find(value, node.left_children, node, 'left_children')
                elif (value > node.small) and (value <= node.large):
                    return self.find(value, node.middle_children, node, 'middle_children')
                else:
                    return self.find(value, node.right_children, node, 'right_children')
        else:  # 当节点中只有一个值时
            if node.left_children is None:  # 如果没有有子节点那么就应该插入到该叶节点
                return node, parent, node_type
            else:  # 否则一定有两个叶节点
                if value <= node.small:
                    return self.find(value, node.left_children, node, 'left_children')
                else:
                    return self.find(value, node.right_children, node, 'right_children')

    def insert(self, value):
        node, parent, node_type = self.find(value, self.root, None, 'root')
        if node.small is None:  # 如果返回的节点node.small没有值，那么直接插入，根节点没有值时
            node.small = value
        elif (node.small is not None) and (node.large is None):  # 如果返回的节点有一个值，插入
            if value > node.small:
                node.large = value
            else:
                node.large = node.small
                node.small = value
        else:  # 如果返回的节点有两个值
            if value <= node.small:
                middle_value = node.small
                node.small = value
            elif value > node.large:
                middle_value = node.large
                node.large = value
            else:
                middle_value = value
            # 分裂成两个节点上传到父节点
            node_small = Node(small=node.small)
            node_large = Node(small=node.large)
            del node  # 已分类 删去
            self._insert(node_small, node_large, middle_value, parent)

    def _insert(self, node_small, node_large, value_mid, parent):  # 插入到非叶子节点
        if parent is None:  # 如果节点本身就是根节点，就再重新创造一个根节点
            parent = Node()
        if parent.small is None:  # 只有本身是根节点时创造的根节点small为空，这时候parent是跟节点
            parent.small = value_mid
            parent.left_children = node_small
            parent.left_children.parent = parent
            parent.right_children = node_large
            parent.right_children.parent = parent
            self.root = parent
        elif (parent.small is not None) and (parent.large is None):  # 插入父节点有一个元素
            if value_mid <= parent.small:  # 当插入小于节点的小值时,可以得知是从左子节点上移的点
                parent.large = parent.small
                parent.small = value_mid
                parent.left_children = node_small
                parent.left_children.parent = parent
                parent.middle_children = node_large
                parent.middle_children.parent = parent  # 并给增加的中间节点指定父节点
            else:  # value_mid > parent.large说明从右子节点上移的点
                parent.large = value_mid
                parent.right_children = node_large
                parent.right_children.parent = parent
                parent.middle_children = node_small
                parent.middle_children.parent = parent
        else:  # 插入的非叶子节点有两个节点
            if value_mid > parent.large:  # 从右子节点插入
                node_small_tmp = Node(small=parent.small)
                node_small_tmp.left_children = parent.left_children
                node_small_tmp.left_children.parent = node_small_tmp
                node_small_tmp.right_children = parent.middle_children
                node_small_tmp.right_children.parent = node_small_tmp
                node_large_tmp = Node(small=value_mid)
                node_large_tmp.left_children = node_small
                node_large_tmp.left_children.parent = node_small
                node_large_tmp.right_children = node_large
                node_large_tmp.right_children.parent = node_large_tmp
                self._insert(node_small_tmp, node_large_tmp, parent.large, parent.parent)
                del parent  # 已经分裂成两个子节点了所以可以删去了
            elif value_mid <= parent.small:  # 说明从左子节点上传的
                node_small_tmp = Node(small=value_mid)
                node_small_tmp.left_children = node_small
                node_small_tmp.left_children.parent = node_small_tmp
                node_small_tmp.right_children = node_large
                node_small_tmp.right_children.parent = node_small_tmp
                node_large_tmp = Node(small=parent.large)
                node_large_tmp.left_children = parent.middle_children
                node_large_tmp.left_children.parent = node_large_tmp
                node_large_tmp.right_children = parent.right_children
                node_large_tmp.right_children.parent = node_large_tmp
                self._insert(node_small_tmp, node_large_tmp, parent.small, parent.parent)
                del parent
            else:  # parent.small <= value_mid < parent.large
                node_small_tmp = Node(small=parent.small)
                node_small_tmp.left_children = parent.left_children
                node_small_tmp.left_children.parent = node_small_tmp
                node_small_tmp.right_children = node_small
                node_small_tmp.right_children.parent = node_small_tmp
                node_large_tmp = Node(small=parent.large)
                node_large_tmp.left_children = node_large
                node_large_tmp.left_children.parent = node_large_tmp
                node_large_tmp.right_children = parent.right_children
                node_large_tmp.right_children.parent = node_large_tmp
                self._insert(node_small_tmp, node_large_tmp, value_mid, parent.parent)
                del parent


if __name__ == '__main__':
    q = Tree23()
    for v in [6, 5, 3, 4, 7, 9, 1, 2, 8]:
        q.insert(v)
    # q.insert(6)
    # print(q.root.small)
    # q.insert(5)
    # print(q.root.small, q.root.large)
    # q.insert(3)
    # print(q.root.small, q.root.left_children.small, q.root.right_children.small)
    # q.insert(4)
    # print(q.root.small, q.root.left_children.small, q.root.left_children.large, q.root.right_children.small)
    # q.insert(7)
    # # print(q.root.small, q.root.left_children.small, q.root.left_children.large, q.root.right_children.small,
    # #       q.root.right_children.large)
    # q.insert(9)
    # print(q.root.small, q.root.large,q.root.left_children.small, q.root.left_children.large,
    #       q.root.middle_children.small,q.root.right_children.small, q.root.right_children.large)
    # q.insert(1)
    # print(q.root.small, q.root.left_children.small, q.root.left_children.left_children.small,
    #       q.root.left_children.left_children.large, q.root.left_children.right_children.small,
    #       q.root.left_children.right_children.large)
    print(q.root.small, q.root.right_children.small, q.root.right_children.left_children.small,
          q.root.right_children.left_children.large, q.root.right_children.right_children.small,
          q.root.right_children.right_children.large)
    # print(q.root.small, q.root.large)
    # print(q.root.left_children.small)
    # print(q.root.left_children.left_children.small )
    # print(q.root.middle_children_r.small)
    # print(q.root.right_children.small,q.root.right_children.large)
    # # print(q.root.middle_children_r.small, q.root.middle_children_r.large)
    # print(q.root.right_children.small, q.root.right_children.large)
    # print(q.root.right_children.left_children.small, q.root.right_children.right_children.small)






