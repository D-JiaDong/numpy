import numpy as np
data = [['图书编号' ,'图书名称','图书种类','图书价格','出版时间'],
        [1,'Python编程基础','计算机',77.5,'2018-01'],
        [2,'诗歌大全','文学艺术',30.5,'2015-04'],
        [3,'机器学习时间','数学',101.5,'2017-06'],
        [4,'唐宋简史','文学艺术',60.5,'2016-04']]

book_info=np.array(data)
print(book_info)
print("------------------------------")
book_info[3,2]='计算机'
print(book_info)
print("------------------------------")
book_info_comput=book_info[book_info[:,2]=="计算机"]
print(book_info_comput)
print("------------------------------")
price=book_info[1:,3].astype(np.float)
book_1=book_info[1:]
book_1=book_1[price>50]
print(book_1[:,1])
print("------------------------------")
print(book_info[[1,2,3,4],[4]])
print("------------------------------")
print(price*5)









