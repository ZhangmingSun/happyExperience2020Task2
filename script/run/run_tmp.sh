#!/usr/bin/env bash

#mvn clean package -U
: '
mvn clean package
if [ $? != 0 ];then
    echo "build failed!"
	exit 1
fi
'

#yarn --cluster zjyprc-hadoop application -kill application_1564666114135_333647
#yarn --cluster zjyprc-hadoop application -kill application_1564666114135_334712
#hadoop --cluster zjyprc-hadoop fs -rm -r ${outputPath}

scriptPath=script/run #工程相对路径
localPath=/home/szm/tencentContest2020/data #本地绝对路径

cat ${localPath}/test | grep szm > ${localPath}/szm.txt
echo `cat ${localPath}/szm.txt`

#=========================XXX========================
#echo "sh script/feature/gen_group_features.sh 7"
#sh script/feature/gen_group_features.sh 7

#echo "run gen_group_features_v2.sh 7 21"
#python script/tools/MultiAutoRun_8days.py script/feature/gen_group_features_v2.sh 7 21



echo "Finish the Task!"