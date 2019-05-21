# -*- coding: utf-8 -*-
"""
Created on 2018/8/2

@author: xing yan
"""

# -*- coding: utf-8 -*-
# __author__="ZJL"

#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


a = [{"a":1,"b":2,"c":3},{"d":4,"e":5},{"f":6,"g":7},{"h":8,"i":9}]

def fenye(datas, pagenum, pagesize):
    if datas and isinstance(pagenum, int) and isinstance(pagesize, int):
        return datas[((pagenum - 1) * pagesize):((pagenum - 1) * pagesize) + pagesize]


print(fenye(a, 2, 3))