#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np

#列表运算
li = [1,2,3]
print(li*3)
li_1 = [4,5,6]
print(li+li_1)
# for i in li:
#数组运算
arr = np.array([1,2,3])
arr_2 = np.array([4,5,6])
print(arr*3)
print(arr+arr_2)
print('-----------------------------')
##创建数组
#创建一维数组
data =[1,2,3]
arr = np.array(data)
print(arr)
#shape:查看数组形状，dtype查看数组类型
print('shape:',arr.shape)
print('dtype:',arr.dtype)

print('*'*30)
#创建二维数组
data=[[1,2.5,3],[4.1,5,6]]
arr_2 = np.array(data)
print(arr_2)
print('shape:',arr_2.shape)
print('dtype:',arr_2.dtype)


#创建三维数组
data = [[[1,2,3],[4,5,6]],
        [[2,2,2],[3,3,3]]]
arr_3=np.array(data)
print(arr_3)
print('shape:',arr_3.shape)
print('dtype:',arr_3.dtype)


#备注1：当创建多维数组时，形式要保持一致
arr = np.array([[1,2,3],[2,3,4]])
print(arr)
#备注2：数组中的元素类型一致，若不一致，则自动转成一致的数据类型
arr = np.array([2,4.5]) #unicode对象，占位32
print(arr.dtype)

#reshape()更改数组形状
arr = np.array([range(1,5),[5,6,7,8]])
print(arr)
#reshape()是会生成数组副本，不会在原数组上进行数组形状更改
arr =  arr.reshape(8)
print(arr)
arr = arr.reshape(2,4,1)
print(arr)
#-1,自动计算
arr = arr.reshape(-1,4)
print(arr)
#reshape更改后的形状元素个数要和 更改之前保持一致。
# arr = arr.reshape(3,9)
# print(arr)




#使用快捷函数创建数组
zero = np.zeros(8)
print(zero)
one = np.ones((3,4))
print(one)
print("asdfasdfasd")
empty = np.empty((2,1,1))
print(empty)
onel = np.ones_like(zero) #zeros_like(另外一个数组)
print(onel)
#生成单位数组
eye = np.eye(3,4)
print(eye)

#arange()生成数字序列，
arr = np.arange(1,5,2)#从1，3
print(arr)
#语法：arange([起点]，终点，[步长]),起点默认值0，步长默认值是1,左包含，右不包含
arr = np.arange(8)
print(arr)
arr = np.arange(3,7)
print(arr)
arr = np.arange(3,9,1.5)
print(arr)
#arange(),参数可以为负数,4,3,2,1
arr = np.arange(4,0,-1)
print(arr)
print(np.arange(-8,0))
#备注3：若填写步长，则一定需要将起始点进行填写
print(np.arange(0,8,2))

#参数dtype的作用：规定数组的数据类型
arr = np.array([1.3,2.5,6],dtype =np.int32)
print(arr)
print(arr.dtype)

arr_float = arr.astype(np.float)
print(arr_float)
print(arr_float.dtype)

arr = np.array(['a','b'])
print(arr.dtype)
arr_int = arr.astype(np.int32)
print(arr_int)



