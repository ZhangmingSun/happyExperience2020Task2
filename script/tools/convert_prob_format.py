#!/usr/bin/python
# -*- coding: UTF-8 -*-

from convertELogStrToValue import ConvertELogStrToValue
#import datetime

dict = {} #空字典

#========================================================
#转换概率格式
#功能1: Convert ELogStr To Value
#功能2: 限制小数位不能超过6位
#功能3: 对dict中按key升序排列
#========================================================
fs_label_prob = open('label_prob', 'r')
for line in fs_label_prob.readlines():
    line = line.strip()
    if dict.has_key(line.split(",")[0])==False :
        key = line.split(",")[0]
        if "e" in line.split(",")[1] :
            #Convert ELogStr To Value
            (tag, value) = ConvertELogStrToValue(line.split(",")[1])
            value = str(value)
            #以下是小数位太长，导致没转换，需特别处理
            if "e" in value :
                value = "0.000001"            
        else:
            value = line.split(",")[1]
        #截取8个字符，因为小数位不能超过6位
        if len(value)>8 :
            dict[key] = value[0:8]
        if len(value)<=8 :
            #dict[key] = value + "000000"[0:(8-len(value))]
            dict[key] = value
fs_label_prob.close()

#对dict中按key排序
#key=lambda item:item[0] -- 表示按item[0](即key)排序
#Note: sorted()函数返回的是由tuple组成的list
dict_sorted = sorted(dict.items(),key=lambda item:item[0])

#========================数据保存========================
fileObject = open('低空飞翔_09XX_X.csv', 'w')
for tuple in dict_sorted: 
    fileObject.write(tuple[0]+","+tuple[1])
    fileObject.write('\n')
fileObject.close()
