#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime

dict_dnn = {}
dict_ftrl = {}
dict = {} # after merge dict

#========================把数据读入字典========================
#fs_dnn = open('1.txt', 'r')  #dnn
#fs_ftrl = open('2.txt', 'r') #ftrl
fs_dnn = open('dnn.csv', 'r')  #dnn
fs_ftrl = open('ftrl.csv', 'r') #ftrl

#读取part1，存入字典dict1
for line in fs_dnn.readlines():    #依次读取每行
    line = line.strip()   #去掉每行头尾空白
    dict_dnn[line.split(",")[0]] = line.split(",")[1]

#读取part2，存入字典dict2
for line in fs_ftrl.readlines():
    line = line.strip()
    dict_ftrl[line.split(",")[0]] = line.split(",")[1]

for (k,v) in dict_dnn.items():
    merge_value = float(dict_dnn[k])*0.75 + float(dict_ftrl[k])*0.25
    dict[k] = str(merge_value)[0:8]
    if "e" in str(merge_value) :
        dict[k] = "0.000002"

fs_dnn.close()
fs_ftrl.close()

#========================数据保存========================
fileObject = open('merge.低空飞翔_10XX_X.csv', 'w')
for (k,v) in dict.items():
    #print "dict[%s]=" % k,v 
    fileObject.write(str(k)+','+str(v))
    fileObject.write('\n')
fileObject.close()
