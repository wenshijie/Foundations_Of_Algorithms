# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 00:11:48 2018

@author: lenovo
"""
#work1
#找出最大数
def find_max(S):
    if isinstance(S,list):
        s_max = S[0]
        i=1
        while i<len(S):
            if S[i]>s_max:
                s_max=S[i]
            i+=1
        return s_max
    else:
        print('please input a list')
#找出最小值
def find_min(S):
    if isinstance(S,list):
        s_min=S[0]
        i=1
        while i<len(S):
            if S[i]<s_min:
                s_min=S[i]
            i+=1
        return s_min
    else:
        print('please input a list')
#1.3找出列表中三个元素组成的集合
def find_three(S):
    if isinstance(S,list):
        S=list(set(S))#去重
        n=len(S)
        if n>2:
            
            results = []
            for i in range(n-2):
                for j in range(i+1,n-1):
                    for k in range(j+1,n):
                        result=[S[i],S[j],S[k]]
                        results.append(result)
            return results
        else:
            print('原列表不重复的元素少于三个')
            return S
                    
    else:
        print('please input a list')
#1.4插入排序，二分法查找下一个插入位置
def insertionsort_binarysearch(S):
    if isinstance(S,list):
        n=len(S)
        for i in range(1,n):
            low=0
            high=i
            switch=True
            while switch:
                if S[i]<=S[int((low+high)/2)]:
                    if (int((low+high)/2)==0)or(S[i]>=S[int((low+high)/2)-1]):
                        tmp=S[i]
                        while i>int((low+high)/2): 
                            S[i]=S[i-1]
                            i-=1
                        S[int((low+high)/2)]=tmp
                        switch=False
                    else:
                        high=int((low+high)/2)
                else:#S[i]>S[int((low+high)/2)]
                    if (int((low+high)/2)==i-1)or(S[i]<=S[int((low+high)/2)+1]):
                        tmp=S[i]
                        while i>int((low+high)/2)+1:
                           
                           S[i]=S[i-1]
                           i-=1
                        S[int((low+high)/2)+1]=tmp
                        switch=False
                    else:
                        low=int((low+high)/2)
        return S
    else:
        print('please input a list')
#1.4插入排序，二分法查找下一个插入位置(2)    
def insertionsort_binarysearch2(S):
#定义二分查找下一个插入位置       
    def binary_search(low,high,S,i):#上限，下限索引和列表
        if S[i]<=S[int((low+high)/2)]:
            if (int((low+high)/2)==0)or(S[i]>=S[int((low+high)/2)-1]):
                tmp=S[i]
                while i>int((low+high)/2): 
                    S[i]=S[i-1]
                    i-=1
                S[int((low+high)/2)]=tmp
            else:
                binary_search(low,int((low+high)/2),S,i)
        else:#S[i]>S[int((low+high)/2)]
            if (int((low+high)/2)==i-1)or(S[i]<=S[int((low+high)/2)+1]):
                tmp=S[i]
                while i>int((low+high)/2)+1:                   
                   S[i]=S[i-1]
                   i-=1
                S[int((low+high)/2)+1]=tmp
            else:
                binary_search(int((low+high)/2),high,S,i)
               
    if isinstance(S,list):
        n=len(S)
        for i in range(1,n):
            low=0
            high=i
            binary_search(low,high,S,i)
        return S
    else:
        print('please input a list')    
#1.5计算两个整数的最大公约数
def gcd(m,n):
    if (isinstance(n,int)) & (isinstance(m,int)):
        r=m%n
        if r==0:
            return n
        else:
           return gcd(n,r)
    else:
        print('please input integer')
def gcd2(m,n):
    if (isinstance(n,int)) & (isinstance(m,int)):
        if n==0:
            return m
        else:
            return gcd(n,m%n)
    else:
        print('please input integer')
#1.6 找出最大值和最小值,比较次数不超过1.5n
def find_max_min(S):
    if isinstance(S,list):
        if S[0]<S[1]:
            min_value=S[0]
            max_value=S[1]
        else:
            min_value=S[1]
            max_value=S[0]
        i=2
        n=len(S)
        while i<n-1:
            if S[i]<=S[i+1]:
                if S[i+1]>max_value:
                    max_value=S[i+1]
                if S[i]<min_value:
                    min_value=S[i]
            else:
                if S[i]>max_value:
                    max_value=S[i]
                if S[i-1]<min_value:
                    min_value=S[i-1]
            i+=2
        if i==n-1:#奇数个时刚好为剩余最后一个地址为n-1，偶数个时比较玩 i=n
            if S[i]>max_value:
                max_value=S[i]
            if S[i]<min_value:
                min_value=S[i]
        return max_value,min_value
    else:
        print('please input a list')
#1.7确定一个准完全二叉树是否是堆，完全二叉树与其他资料定义有差别。准完全二叉树定义如下
#essentially complete binary tree：all its levels are full except possible
# the last level，where only some rightmost leaves may be missing
#假设此二叉树保存为一个list,只有右侧确实左侧都是满的或最后的单叶点是左叶点
def ecbt_heap(S):
    if isinstance(S,list):
        i=0
        n=len(S)
        while 2*i+1<n-1:#2*i+1不是最后一个节点
            if (S[i]<S[2*i+1]) or (S[i]<S[2*i+2]):
                return False
            i+=1
        if 2*i+1==n-1:
            if S[i]<S[2*i+1]:
                return False
        return True
    else:
        print('please input a list')
#12 数组范围在1-kn 取k=1,互不相同的数组,且为只为整数
def sort12(S):
    if (isinstance(S,list))and(min(S)>=1):
        B=[0]*(max(S)+1)#创建长度为列表S最大值的列表，因为指针从0开始+1
        for i in S:
            B[i]=i
        C=B[:]#不能用直接赋值或copy
        for j in C:
            if j==0:
                B.remove(0)
        return B
    else:
        print('列表要求元素互不相同、整数、大于等于1')

    
        
        
if __name__=='__main__' :
    S=[1,2,3,4,5,6,7,8]
    S2=[1,2,2,2,2]
    S3=[1,4,6,4,2,2,5,7,9]
    S4=[9,8,7,6,5,4,3,2,1,13]
    #s_max=find_max(S)
    #s_min=find_min(S)
    #result=find_three(S2)
    #result_s=insertionsort_binarysearch2(S3)
    #gc=gcd2(10,4)
    #ma,mi=find_max_min(S3)
    #result=ecbt_heap(S3)
    result=sort12(S4)
    
    
