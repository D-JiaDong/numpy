#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    Numpy 文件存储

'''
import numpy as np
#将数组存储成无格式的二进制文件
arr = np.arange(0,10).reshape(2,5)
print(arr)
print(arr.dtype)
#.bin为后缀的文件是二进制文件
arr.tofile(r'D:\1-zr\晚班-02\20200306\arr_tofile.bin')
#无格式的二进制文件，重新读取到python文件中时，需要重新定义数据类型和形状
arr_fromfile = np.fromfile(r'D:\1-zr\晚班-02\20200306\arr_tofile.bin')
print(arr_fromfile)
print(arr_fromfile.dtype)
arr_fromfile.dtype = np.int32
print(arr_fromfile.dtype)
print(arr_fromfile.reshape(2,5))

#将数组存储成二进制numpy格式文件，save（）存，load（）取
#numpy二进制文件后缀是'.npy'
np.save(r'D:\1-zr\晚班-02\20200306\arr_save.npy',arr)
arr_save =np.load(r'D:\1-zr\晚班-02\20200306\arr_save.npy')
print(arr_save)
#同时存储多个数组至磁盘空间，savez()
#.npz(相当于压缩包)
arr_zz = np.ones((3,3))
#默认情况，存入磁盘的数组，命名为arr_i,可以利用别名=数组名，进行重新命名
np.savez(r'D:\1-zr\晚班-02\20200306\arr_savez.npz',arr,zz=arr_zz)
arr_savez = np.load(r'D:\1-zr\晚班-02\20200306\arr_savez.npz')
print(arr_savez)
#使用，存在磁盘中的数组名字
print(arr_savez['arr_0'])
print(arr_savez['zz'])

#将数组存储成文本文件(.txt,.csv）
#savetxt(),loadtxt()
#调整存储格式，fmt=格式输出,delimiter（元素之间以什么形式间隔，默认是’  ’）
np.savetxt(r'D:\1-zr\晚班-02\20200306\arr_savetxt.csv',arr,fmt='%d',delimiter=',')#
arr = np.loadtxt(r'D:\1-zr\晚班-02\20200306\arr_savetxt.csv',delimiter=',')
print(arr)



