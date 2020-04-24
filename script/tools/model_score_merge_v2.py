#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import datetime
import sys
#参数个数：len(sys.argv)
#脚本名：    sys.argv[0]
#参数1：     sys.argv[1]

list_label = []
list_model1_score = []
list_model2_score = []
list_merge_score = [] # list for merge

if len(sys.argv) <= 1:
    print("Error! You need to input one parameter -- the percentage!!!")
    sys.exit()

#percentage = float(0.75) #表示model占比75%
percentage = float(sys.argv[1])

#========================把数据读入字典========================
fs_model1 = open('ftrl_model', 'r') #注意是空格分隔
fs_model2 = open('mlr_model', 'r') #注意是逗号分隔

#读取part1，存入字典dict1
for line in fs_model1.readlines():    #依次读取每行
    line = line.strip()   #去掉每行头尾空白
    list_model1_score.append(line.split(" ")[1]) #注意是空格分隔
    list_label.append(line.split(" ")[0])

#读取part2，存入字典dict2
for line in fs_model2.readlines():
    line = line.strip()
    #dict_model2[line.split(",")[0]] = line.split(",")[1]
    list_model2_score.append(line.split(",")[1])

#预先判断一下
if len(list_model1_score) != len(list_model2_score):
    print("Error! The length of two model is not same, please check again!!!")
    sys.exit()

for i in range(len(list_model1_score)):
    merge_score = float(list_model1_score[i])*percentage + float(list_model2_score[i])*(1-percentage)
    if "e" in str(merge_score) or merge_score == 0 :
        list_merge_score.append("0.000002")
    else:
        list_merge_score.append(str(merge_score)[0:8])

fs_model1.close()
fs_model2.close()

#========================数据保存========================
fileObject = open('twoModel_merge_result_'+str(percentage), 'w')
for i in range(len(list_model1_score)):
    #print "dict[%s]=" % k,v 
    fileObject.write(list_label[i] + ' ' + list_merge_score[i])
    fileObject.write('\n')
fileObject.close()
