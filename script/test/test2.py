#!/usr/bin/env python  
# -*- coding:utf-8 -*-  

import pandas as pd
import numpy as np
from collections import defaultdict
import math
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 3:
        print("Error! You need to input 3 parameter!")
        sys.exit()

    #now_phase = 3
    #train_path="/home/szm/work/kddCup_2020_t2/data/underexpose_train"
    #test_path="/home/szm/work/kddCup_2020_t2/data/underexpose_test"
    now_phase = int(sys.argv[1])
    train_path = str(sys.argv[2])
    test_path = str(sys.argv[3])

    recom_item = []

    whole_click = pd.DataFrame()
    for c in range(now_phase + 1):
        print('read click phase:', c)
        click_train = pd.read_csv(train_path + '/underexpose_train_click-{}.csv'.format(c), header=None,  names=['user_id', 'item_id', 'time'])
        click_test = pd.read_csv(test_path + '/underexpose_test_click-{}.csv'.format(c), header=None,  names=['user_id', 'item_id', 'time'])
        all_click = click_train.append(click_test)
        whole_click = whole_click.append(all_click)

    # find most popular items
    top50_click = whole_click['item_id'].value_counts().index[:50].values
    top50_click = ','.join([str(i) for i in top50_click])
    print('find most popular items:', top50_click)

    #whole_query_df = pd.DataFrame()
    whole_query_df= pd.DataFrame(recom_item, columns=['user_id', 'time'])
    for c in range(now_phase + 1):
        print('read query phase:', c)
        test_query = pd.read_csv(test_path + '/underexpose_test_qtime-{}.csv'.format(c), header=None,  names=['user_id', 'time'])
        whole_query_df = whole_query_df.append(test_query)
    #whole_query_df.to_csv('/home/szm/work/kddCup_2020_t2/baseline.csv', index=False, header=None)

    fileObject = open('/home/szm/work/kddCup_2020_t2/submit_20200425_1.csv', 'w')
    for index, row in whole_query_df.iterrows():
        #print(row['user_id'], row['time'])
        fileObject.write(str(row['user_id']) + "," + top50_click)
        fileObject.write('\n')
    fileObject.close()
    '''
    '''

    '''
    recom_df = pd.DataFrame(recom_item, columns=['user_id', 'item_id', 'sim'])  
    result = get_predict(recom_df, 'sim', top50_click)  
    result.to_csv('baseline.csv', index=False, header=None)
    '''