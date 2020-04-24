#!/bin/bash


: '
cd ..; cd ..; #必须返回到pom.xml所在的目录，才能进行mvn clean或mvn clean package命令
mvn clean package
#mvn clean package -U
if [ $? != 0 ];then
    echo "build failed!"
	exit 1
fi
'

#mvn --version
#echo `which python`

#scriptPath=script/run #工程相对路径
localDataTestPath="/home/szm/work/kddCup_2020_t2/data/underexpose_test"
localDataTrainPath="/home/szm/work/kddCup_2020_t2/data/underexpose_train"
localProjectPath="/home/szm/work/kddCup_2020_t2/happyExperience2020Task2" #

#python ${localProjectPath}/script/data/test.py
python ${localProjectPath}/script/test/test.py



echo "Finish the Task!"
exit 0