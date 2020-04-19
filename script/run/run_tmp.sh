#!/bin/bash


#mvn --version

: '
cd ..; cd ..; #必须返回到pom.xml所在的目录，才能进行mvn clean或mvn clean package命令
mvn clean package
#mvn clean package -U
if [ $? != 0 ];then
    echo "build failed!"
	exit 1
fi

'

#yarn --cluster zjyprc-hadoop application -kill application_1564666114135_333647
#yarn --cluster zjyprc-hadoop application -kill application_1564666114135_334712
#hadoop --cluster zjyprc-hadoop fs -rm -r ${outputPath}

#scriptPath=script/run #工程相对路径
#localPath=/home/szm/tencentContest2020/data #本地绝对路径，这个路径不行，会出错!!!
localDataPath="E:/Software/Cygwin/setup/home/szm/tencentContest2020/data" #本地绝对数据保存路径
localScriptPath="E:/Software/Cygwin/setup/home/szm/tencentContest2020/contest2020V1/script" #本地绝对Script路径

#cat ${localDataPath}/test | grep hello > ${localDataPath}/szm.txt
#echo `cat ${localDataPath}/szm.txt`

echo `cat ${localDataPath}/test | grep hello`
echo "run test.py"
#/usr/bin/python script/data/test.py
#E:/Software/Cygwin/setup/usr/bin/python script/data/test.py
#/cygdrive/e/Software/Cygwin/setup/usr/bin/python script/data/test.py
#python script/data/test.py

#注意python实际的执行目录是: D:\software2\Anaconda3\setup\python.exe，而不是/usr/bin/python
#python E:/Software/Cygwin/setup/home/szm/tencentContest2020/contest2020V1/script/data/test.py
#python script/data/test.py #这行命令只能在当前script所在的目录才能执行
python ${localScriptPath}/data/test.py



echo "Finish the Task!"
exit 0