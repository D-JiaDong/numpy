#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    Nnmpy中提供的数值运算函数

'''
import numpy as np

#平方根sqrt()和e的多少次方,exp()
arr_empty = np.empty((3,4))
print(arr_empty)
for i in range(3):
    arr_empty[i] = i
print(arr_empty)
print(np.sqrt(arr_empty))
print(np.exp(arr_empty))
#二元函数，接收的两个数组形状要一致
arr_1 =np.random.uniform(0,14,12).reshape(3,4)
print(arr_1)
arr_2 = np.arange(1,13).reshape(3,4)
print(arr_2)
#两个数组对位比较，maximum（）新数组取大的值，新数组minimum（）取小的值
print(np.maximum(arr_1,arr_2))
print(np.minimum(arr_1,arr_2))

#取绝对值函数
arr = np.array([-1,2,3,-4,0])
print(np.abs(arr))
print(np.sign(arr))
#ceil()向上取整的函数
arr = np.array([2.3,4.9,5.7,1.1])
print(np.ceil(arr))
#floor()向下取整的函数
print(np.floor(arr))
# rint()四舍五入
print(np.rint(arr))
#around,规定保留几位小数
arr_float =np.array([224.343255,412.141546,2342.1432546])
#decimals是控制小数位保留几位，可以为负数，即约掉小数点前几位
print(np.around(arr_float,decimals=-1))
print(np.modf(arr_float))
#  +-*/
arr1=np.ones(4)
arr1 =np.array([2,5,1,2])
arr2 = np.arange(3,7)
print(np.add(arr1,arr2))
print(arr1+arr2)
#power(arr1,arr2),arr1的arr2次方
print(arr1)
print(arr2)
print(np.power(arr1,arr2))
#copysign(arr1,arr2),把arr2的符号全部赋值给arr1
arr3 = np.array([-1,3,9,7])
print(np.copysign(arr2,arr3))
print(arr2)
print(arr2>arr3)
arr4 = np.array([1,0,0,4])
arr5 = np.array([2,3,0,-4])
#逻辑与运算，两个数值同时为真即为真,结果集是布尔集，0为假，其他数值都为真
print(np.logical_and(arr4,arr5))
#逻辑或运算，同时为0才为假，其他都为真
print(np.logical_or(arr4,arr5))
#异或运算，一真一假则为真
print(np.logical_xor(arr4,arr5))

#np.where
cond = np.array([True,False,True,True,False])
arr1 = np.array([1.1,1.2,1.3,1.4,1.5])
arr2 = np.array([2.1,2.2,2.3,2.4,2.5])
#需求，若cond为真，取arr1中数值，若cond为假，取arr2中的数值
result = [(a if c else b) for a,b,c in zip(arr1,arr2,cond)]
print(result)
res = np.where(cond,arr1,arr2)
print(res)
#where()中第二个和第三个参数可以不为数组，也可以是一个标量
res_2 = np.where(cond,arr1,0)
print(res_2)
#where(),可以直接写布尔数组,则会返回数组中，满足条件的下标
print(np.where(arr1>1.3))

cond1 = np.array([True,False,False,True])
cond2 = np.array([False,True,False,True])
(1,2,3,0)