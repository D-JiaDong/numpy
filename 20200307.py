#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    result = []
for i in range(n):
    if  cond1[i] and cond2[i]: # 都为True
         result.append(0)
    elif cond1[i]: # cond1`为True
         result.append(1)
    elif cond2[i]: # cond2为True
         result.append(2)
     else: # 都为False
         result.append(3)
'''
import numpy as np
cond1 = np.array([True,False,False,True])
cond2 = np.array([False,True,False,True])
#结果1，2，3，0
#logical_and(),&
res = np.where(np.logical_and(cond1,cond2),0,np.where(cond1,1,np.where(cond2,2,3)))
print(res)

#数学和统计的一些方法
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
#求和
print(arr.sum())
#axis(轴值)
#按照行的方向，对每一列进行求值
print(arr.sum(axis = 0))
#按照列的方向，对每一行进行求值
print(arr.sum(axis = 1))

#求平均值.mean()
arr_mean = np.arange(3)  #[0,1,2]
print(arr_mean.mean())
print(arr.mean())
print(arr.sum()/9)
print(arr.mean(axis = 1))
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
#方差std()  [x1,x2,x3,...xn],std^2 = (（xi-x(平))^2).sum()/n
temp = (((arr-arr.mean())**2).sum())/9
print(np.sqrt(temp))
print(arr.std())

#累计求和cumsum，累计求乘cumpord
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(arr.cumsum())
print(arr.cumsum(axis = 0))
print(arr.cumsum(axis = 1))

arr_3d = np.array([[[1,1],
                    [2,2]],
                   [[3,3],
                    [4,4]]])
print(arr_3d.shape)
print(arr_3d.cumprod())
#三维数组中，两个二维数组进行累计乘法
print(arr_3d.cumprod(axis = 0))
#每个二维数组的行的方向，列进行累计乘法
print(arr_3d.cumprod(axis = 1))
#每个二维数组的列的方向，行进行累计乘法
print(arr_3d.cumprod(axis = 2))


#argmax（），argmin(),查看数组中，最大数值和最小数值的下标
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(arr.argmax())
print(arr.argmin())

#####布尔型数组的函数操作#####
#True 1,False 0
print(arr>4)
print((arr>4).sum())
bool_arr = (arr>=3)&(arr<=5)
print(bool_arr.sum())
print(arr[bool_arr].mean())

#any()只要元素中有True即为True,all()所有元素都为True才为True ，经常针对布尔数组进行使用

print(bool_arr)
print(bool_arr.any())
print(bool_arr.all())

######对数组进行排序######
#sort()
arr = np.array([[8,3,2],
                [3,2,5],
                [6,7,8]])
#sort()是在原数组的基础上进行排序的，arr.sort()会返回None值
# arr.sort()
# print(arr)
arr.sort(axis = 0)
print(arr)
arr.sort(axis =1)
print(arr)

##### 多数组间的逻辑运算####
names = np.array(['Bob','Jame','Jack','Bob','Jame'])
#唯一化，unique()
print(np.unique(names))

arr_1 = np.array([2,3,4,9,5])
arr_2 = np.array([1,3,4,11,15])
#计算交集
print(np.intersect1d(arr_1,arr_2))
#并集
print(np.union1d(arr_1,arr_2))
#差集，选取，在arr_1中但不在arr_2中的元素
print(np.setdiff1d(arr_1,arr_2))
#判断arr_1中元素是否在arr_2中，返回布尔数组
print(np.in1d(arr_1,arr_2))
#选取的元素，只在其中一个数组里面
print(np.setxor1d(arr_1,arr_2))

#####线性代数函数#####
arr_1= np.array([[8,9],
                 [11,12]])
arr_2 = np.array([[1,3],
                  [2,3]])
#取方阵对角线上的数值
print(np.diag(arr_1))
#求方阵对角线值得和
print(np.trace(arr_1))
#计算矩阵乘法
#1*8+2*9  3*8+3*9
#1*11+2*12  11*3+12*3
print(np.dot(arr_1,arr_2))
print(arr_1.dot(arr_2))

###矩阵###
#线性代数中使用得数据类型
A = np.mat([[0,1,2],[1,0,3],[4,-3,8]])
print(type(A))
print(A)
#在做矩阵逆运算时，矩阵要求是方阵
#矩阵的逆运算，A-1 = A*/|A|, AA-1 = 单位矩阵
#linalg ,是针对线性代数中运算的函数库
inv= np.linalg.inv(A)
print(inv)
print(A*inv)

#求线性方程的解
#Ax = b ，A是矩阵，b一维数组（或二维数组），x未知变量
b = np.array([0,8,-9])
x = np.linalg.solve(A,b)
print(x)
print(np.dot(A,x))

#求矩阵特征值和特征向量
#Cx = ax,C为已知矩阵，a是个标量，特征值
#x是特征向量，一维的向量
C = np.mat('3 -2;1 0')
print(C)
# C = np.mat([[3,-2],[1,0]])
# print(C)
#np.linalg.eig返回两个结果集，第一个是特征值结果集，第二个是对应的特征向量
c1,c2 = np.linalg.eig(C)
print(c2)
print('left:',np.dot(C,c2[:,0]))
print('right:',np.dot(c1[0],c2[:,0]))
print('left:',np.dot(C,c2[:,1]))
print('right:',np.dot(c1[1],c2[:,1]))


#np.random,随机生成数的库
#正态分布，均值，空值最高点位置，默认值是0，方差，图形形状，默认值1，>1,矮胖，<1高瘦
#randn 随机数符合标准的正态分布
arr_randn = np.random.randn(2,3)
print("adfkssssssssssssssssssss")
print(arr_randn)
#loc 均值，scale 方差，size个数
arr_normal = np.random.normal(loc = 2,scale = 2,size = 10 )
print(arr_normal)
#随机 生成[0,1)均匀分布的数值 大于等于零 小于一
print("ssssssssssssssssssssssssssss")
print(np.random.rand(3,2,1))
#随机生成整数low,high,size
print(1111111111111111111111111111111)
print(np.random.randint(3,9,(2,3)))
#随机生成种子
np.random.seed(1676)
print(np.random.randn(5))
print(np.random.randn(5))
np.random.seed(1676)
print(np.random.randn(5))
#正态分布N（μ，σ2）曲线中，μ一定时，σ越大，曲线越“矮胖”；σ越小，曲线越“瘦高”，表示取值越集中．


