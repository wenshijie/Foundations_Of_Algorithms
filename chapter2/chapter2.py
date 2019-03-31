# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 14:50:52 2018

@author: lenovo
"""

import numpy as np
# chapter2
# 算法2.1 二分查找（递归） 有序数组


def find_location(S, x):
    '''存在返回指针，不存在返回-1'''
    def location(low,high):
        if low>high:
            return -1
        else:
            mid=int((low+high)/2)
            if S[mid] == x:
                return mid
            elif x<S[mid]:
                return location(low,mid-1)
            else:
                return location(mid+1,high)
    return location(0, len(S)-1)

# 算法2.2 合并排序


def mergesort(S):
    n=len(S)
    if n>1:
        U=S[:int(n/2)]
        V=S[int(n/2):]
        return merge(mergesort(U),mergesort(V))
    return S
    
# 算法2.3 合并两个有序数组


def merge(U, V):
    long_u = len(U)
    long_v = len(V)
    n = long_u+long_v
    S = [0]*n  # 生成数组S用于存放合并的数组
    i, j, k = 0, 0, 0
    while (i < long_u)and(j < long_v):
        if U[i] < V[j]:
            S[k] = U[i]
            i += 1
        else:
            S[k] = V[j]
            j += 1
        k += 1
    if i >= long_u:  # V剩余
        while k < n:
            S[k] = V[j]
            k += 1
            j += 1
    else:  # U剩余
        while k < n:
            S[k] = U[i]
            k += 1
            i += 1
    return S

# 算法2.4 合并排序2


def mergesort2(S):

    def _mergesort2(low,high):
        if low<high:
            mid=int((low+high)/2)
            _mergesort2(low,mid)
            _mergesort2(mid+1,high)
            _merge2(low,mid,high)
            
    def _merge2(low, mid, high):
        '''合并'''
        n=high-low+1
        U=[0]*n
        i,j,k=low,mid+1,0
        while (i<=mid)and(j<=high):
            if S[i]<S[j]:
                U[k]=S[i]
                i+=1
            else:
                U[k]=S[j]
                j+=1
            k+=1
        if i>mid:
            while k<n:
                U[k]=S[j]
                k+=1
                j+=1
        else :
            while k<n:
                U[k]=S[i]
                k+=1
                i+=1
        S[low:high+1]=U[:]
    _mergesort2(0, len(S)-1)
    return S

# 算法2.6 快速排序


def quicksort(S):
    low = 0
    high = len(S)-1

    def _quicksort(low,high):
        if high>low:
            _quicksort(low,partition(low,high)-1)
            _quicksort(partition(low,high)+1,high)
    def partition(low,high):
        '''分割算法2.7'''
        pivotitem=S[low]
        j=low
        i=low+1
        while i<=high:
            if S[i]<pivotitem:
                j+=1
                tmp=S[j]
                S[j]=S[i]
                S[i]=tmp
            i+=1
        S[low]=S[j]
        S[j]=pivotitem
        return j
    _quicksort(low,high)
    return S


def strassen(A, B):  # 算法2.8 Strassen
    # 矩阵的行列都为2的幂次方
    na = np.shape(A)[0]
    nb = np.shape(B)[0]
    if (na <= 2) and (nb <= 2) and (na == nb):
        C = np.zeros((na, na))  # 不用np.zeros_like(A)避免再次判断A的大小
        for i in range(na):
            for j in range(na):
                for k in range(na):
                    C[i][j] = C[i][j] + A[i][k] * B[k][j]
        return C
    else:
        m = int(na/2)
        A11 = A[0:m, 0:m]
        A12 = A[0:m, m:na]
        A21 = A[m:na, 0:m]
        A22 = A[m:na, m:na]
        B11 = B[0:m, 0:m]
        B12 = B[0:m, m:na]
        B21 = B[m:na, 0:m]
        B22 = B[m:na, m:na]
        M1 = strassen(A11+A22, B11+B22)
        M2 = strassen(A21+A22, B11)
        M3 = strassen(A11, B12-B22)
        M4 = strassen(A22, B21-B11)
        M5 = strassen(A11+A12, B22)
        M6 = strassen(A21-A11, B11+B12)
        M7 = strassen(A12-A22, B21+B22)
        C = np.zeros((na, na))
        C[0:m, 0:m] = M1+M4-M5+M7
        C[0:m, m:na] = M3+M5
        C[m:na, 0:m]= M2+M4
        C[m:na, m:na] = M1+M3-M2+M6
        return C


def prod(a, b):  # 大整数可为负数
    max_value = max(abs(a), abs(b))
    n = len(str(max_value))
    if (a == 0) | (b == 0):
        return 0
    elif n <= 2:
        return a*b
    else:
        m = int(n/2)
        x = int(a/10**m)
        y = a%10**m
        w = int(b/10**m)
        z = b%10**m
        return prod(x, w)*10**(2*m) + (prod(x, z)+prod(w, y))*10**m + prod(y, z)


def prod2(a, b):
    max_value = max(abs(a), abs(b))
    n = len(str(max_value))
    if (a == 0) | (b == 0):
        return 0
    elif n <= 2:
        return a * b
    else:
        m = int(n / 2)
        x = int(a / 10 ** m)
        y = a % 10 ** m
        w = int(b / 10 ** m)
        z = b % 10 ** m
        r = prod2(x+y, w+z)
        p = prod2(x, w)
        q = prod2(y, z)
        return p * 10 ** (2 * m) + (r-p-q) * 10 ** m + q


if __name__=='__main__':
    S = [1, 2, 4, 5, 7, 9, 11, 13, 15, 17, 19, 21, 24]
    S1 = [3, 6, 8, 10, 14]
    S2 = [0, 5, 1, 2, 3, 6, 7, 2, 4, 9, 8, 10, 13, 12, 14]
    A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3], [4, 5, 6, 7]])
    B = np.array([[8, 9, 1, 2], [3, 4, 5, 6], [7, 8, 9, 1], [2, 3, 4, 5]])
    a, b = 1200, -23400
    result=find_location(S,11)
    # result=merge(S,S1)
    # result=mergesort2(S2)
    # result=quicksort(S2)
    # result = strassen(A,B)
    # print(result)
    # print(prod(a,b))
    #print(prod2(a, b))
    print(result)