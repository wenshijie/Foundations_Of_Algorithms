# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#chapter1
import numpy as np

#算法1.1 顺序查找
def seqsearch(S,x):
    '''参数为列表和数值'''
    if isinstance(S,list):
        location=-1
        n=len(S)
        i=0
        while (i<n)&(location==-1):
            if S[i]==x:
                location=i
                #print('{} in the list and first location is {}'.format(x,location))
            i +=1
        #if i>n-1:
            #print('{} not in the list'.format(x))
        return location #不存在返回-1,存在返回目标值的第一个地址
    else:
        print('please input a list')
#算法1.2 数组成员求和
def sum_list(S):
    if isinstance(S,list):
        result=0
        for i in range(len(S)):
            result=result+S[i]
        return result
    else:
        print('please input a list')
#算法1.3 交换排序
def exchangesort(S):
    if isinstance(S,list):
        for i in range(len(S)):
            for j in range(i+1,len(S)):
                if S[j]<S[i]:
                    S[j],S[i]=S[i],S[j]
        return S
    else:
        print('please input a list')
#算法1.4 矩阵乘法 计算两个n*n矩阵的乘积
        
def matrixmult(A,B):
    if (np.shape(A)==np.shape(B))&(np.shape(A)[0]==np.shape(A)[1]):
        #确保A,B 都为N*N
        n=np.shape(A)[0]
        C=np.zeros((n,n))#不用np.zeros_like(A)避免再次判断A的大小
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    C[i][j]=C[i][j]+A[i][k]*B[k][j]
        return C
    else:
        print('please in shape(A)=shape(B)')
#算法1.5 二分查找
def binsearch(S,x):
    if isinstance(S,list):
        low=0
        high=len(S)
        location=-1
        while (low<=high)&(location==-1):
            mid=int((low+high)/2)
            if S[mid]==x:
                location=mid
            elif S[mid]>x:
                high=mid-1
            else:
                low=mid+1
        return location#存在返回某一个目标值的地址 不存在返回-1
    else:
        print('please input a list')
            
#算法1.6斐波那契数列数列的第n项递归
def fib(n):
    if (isinstance(n,int))&(n>=0):
        if n<=1:
            return n
        else:
            return fib(n-1)+fib(n-2)
    else:
        print('please input nonnegative integer ')
#算法1.7菲波那切数列 迭代版
def fib2(n):
    if (isinstance(n,int))&(n>=0):
        '''用列表的话占内存'''
        if n==0:
            return n
        elif n==1:
            return n
        else:
            i,a,b=2,0,1
            while i<=n:
                tmp=b
                b=b+a
                a=tmp
                i+=1
        return b
    else:
        print('please input nonnegative integer ')
 
       
        
if __name__=='__main__':
    S=[1,2,3,2,4,5,6,7,8]
    S1=[1,2,3,4,5,6,7,8,9,10]
    x=2
    A=np.array([[2,3],[4,1]])
    B=np.array([[5,7],[6,8]])
    #ra=seqsearch(S,x)
    #result=sum_list(S)
    #S1=exchangesort(S)
    #C=matrixmult(A,B)
    #rbin=binsearch(S1,5)
    #fib=fib(6)
    #fib2=fib2(5)