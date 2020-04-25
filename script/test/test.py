#!/usr/bin/env python  
# -*- coding:utf-8 -*-  

import pandas as pd
from collections import defaultdict
import math


if __name__ == "__main__":
    now_phase = 3
    #train_path = 'data/underexpose_train'
    #test_path = 'data/underexpose_test'
    train_path="/home/szm/work/kddCup_2020_t2/data/underexpose_train"
    test_path="/home/szm/work/kddCup_2020_t2/data/underexpose_test"
    #train_path = 'E:/Software/Cygwin/setup/home/szm/KDD_Cup_2020_t2/data/underexpose_train'
    #test_path = 'E:/Software/Cygwin/setup/home/szm/KDD_Cup_2020_t2/data/underexpose_test'
    recom_item = []

    whole_click = pd.DataFrame()
    for c in range(now_phase + 1):
        print('phase:', c)
        click_train = pd.read_csv(train_path + '/underexpose_train_click-{}.csv'.format(c), header=None,  names=['user_id', 'item_id', 'time'])
        click_test = pd.read_csv(test_path + '/underexpose_test_click-{}.csv'.format(c), header=None,  names=['user_id', 'item_id', 'time'])

        all_click = click_train.append(click_test)
        whole_click = whole_click.append(all_click)
        #item_sim_list, user_item = get_sim_item(all_click, 'user_id', 'item_id', use_iif=True)

        '''
        for i in tqdm(click_test['user_id'].unique()):
            rank_item = recommend(item_sim_list, user_item, i, 500, 50)
            for j in rank_item:
                recom_item.append([i, j[0], j[1]])
        '''

    # find most popular items
    top50_click = whole_click['item_id'].value_counts().index[:50].values
    top50_click = ','.join([str(i) for i in top50_click])
    print('find most popular items:', top50_click)

    fileObject = open('/home/szm/work/kddCup_2020_t2/out_test.csv', 'w')
    fileObject.write(top50_click)
    fileObject.write('\n')
    fileObject.close()

    '''
    recom_df = pd.DataFrame(recom_item, columns=['user_id', 'item_id', 'sim'])  
    result = get_predict(recom_df, 'sim', top50_click)  
    result.to_csv('baseline.csv', index=False, header=None)
    '''