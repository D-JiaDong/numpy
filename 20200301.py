#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
#下标 0，1，2
li = [1,2,3]
print(li[1])
print('------------------------------------')
#数组索引
#一维数组索引
arr = np.array([1,2,3])
print(arr[1])
#二维的索引
arr = np.array([np.arange(1,4),np.arange(4,7)])
print(arr)
#筛选二维数组时,下标[行，列]
print(arr[0,1])
print(arr[1,2])
print(arr[1][2])
print('*'*30)
#三维的索引
'''
三维数组的结构：2,2,3
[1,2,3
4,5,6]
[2,2,2
3,3,3]
'''
data = [[[1,2,3],[4,5,6]],
        [[2,2,2],[3,3,3]]]
arr = np.array(data)
print(arr)
print(arr.shape)
#三维数组的筛选，[表（二维数组），行，列]
print(arr[0,1,2])
print(arr[1,1,1])
#第二种索引筛选方式
print(arr[0,1,2])
print(arr[0][1][2])


print('--------------数组切片--------------')
li = [1,2,3]
print(li[1:])
#[(起始位置)：(终止位置)：(步长)]
#注：所有参数都为默认值时，则不需要写两个：，只需要写一个就可以
arr = np.arange(8)
print(arr)
#数组的切片运算也是左包含，右不包含
print(arr[3:8])
print(arr[3:])
print(arr[:3])
print(arr[0:3])
print(arr[::2])
print(arr[3::2])
#切片时，起始位置，终止位置，步长都要是整数
#print(arr[1.3::])

#二维数组的切片
arr = np.array([np.arange(1,5),[5,6,7,8],[9,10,11,12]])
print(arr)
print(arr[1])
print(arr[:,2])
print(arr[:,0])
print(arr[1,2:])
print(arr[1:,2])
print(arr[0::2,3])
print(arr[1,::3])
print(arr[::2,1:3])
print('----------三维数组----------')
#三维数组切片
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)
#[先筛表，行，列]
print(arr[:,1,1:])
#[2,8]
print(arr[:,0,1])
print(arr[:])

#数组元素重新赋值,语法，先筛选，再赋值
print('----------------------------------------')
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
arr[0,1] = 20
print(arr)
arr[0,1:] = 30
print(arr)
arr_30 = arr[0,1:]
print(arr_30)
#此时相当于，把31这个整数赋值给变量arr_30
# arr_30 = 31
# print(arr_30)
#整个数组都重新赋值，需要将数组内数字全部筛选出来
arr_30[:]=31
#在数组进行赋值时，直接将数组地址复制给新的数组，而不是直接把数给了数组
print(arr_30)
print(arr)

print('----------------------------------')
arr_31 = arr[0,1:].copy()
print(arr_31)
arr_31[:]=22
print(arr_31)
print(arr)


#布尔索引，筛选时，[布尔数组],True所对应的位置为所选，False则淘汰
#布尔类型，True，False
#布尔数组[True,False]

arr = np.ones((4,4))
for i in range(4):
    arr[i] = i
print(arr)
bo = np.array([True,True,True,False])
print(bo)
print(arr[bo])
print(arr[:,bo])


names = np.array(['Bob','Jame','Bob','Jack'])
print("(((((")
print(names =='Bob')
print(arr[:,names =='Bob'])
print(arr[2:,names =='Bob'])
print(names!='Bob')
print(arr[names!='Bob'])
print((names=='Bob')|(names=='Jack'))
print(arr[(names=='Bob')|(names=='Jack')])
print('--------------------------------------')
print(arr)
print(arr>2)
arr[arr>2]=11
print(arr)

print("asdfasdfadsfffffffffffffffffffffffffff")
#花式索引,就是把所需要的行或列放在一个列表内
arr = np.ones((4,4))
for i in range(4):
    arr[i] = i

print(arr[[1,2]])
print(arr[:,[1,2]])
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print('----------------------------------')
#(0,1),(1,0)
print(arr[[0,1],[1,0]])
print(arr[[0,1,1],[0,1,2]])
print('----------------------------------')
#负号，代表从下向上数，起始是从-1开始的
print(arr[-1])
print(arr[[-1,-2],2])
print('----------------------------------')
arr = np.ones((4,4))
for i in range(4):
    arr[i] = i
print(arr)
#两重花式索引 改变列的顺序
arr[:,0]=0;
print(arr[[0,2,3]][:,[1,0,2,3]])  #[0,1,2,3]
print('*'*30)
###两个数组进行矢量计算，就是对应位数字分别进行计算。+-*/%,
# 如果是两个数组进行计算的话，形状要保持一致
arr = np.array([[1,2,3],[4,5,6]])
arr_1= np.array([[2,2,2],[3,4,4]])
print(arr+arr_1)
print(arr*arr_1)
print(arr*3)
print(1/arr)
# arr_2 = np.array([[1,1,1,1],[2,2,2,2]])
# print(arr+arr_2)
#特殊形式，广播

print('*'*30)
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
arr_index = np.array([1,1,1])
print(arr+arr_index)
arr_columns = np.array([[2],[2]])
print(arr+arr_columns)
