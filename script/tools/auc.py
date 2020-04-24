#!/usr/bin/python
import sys
import math

#created by heqingquan

def scoreAUC(labels,probs):
    i_sorted = sorted(xrange(len(probs)),key=lambda i: probs[i],
                      reverse=True)
    auc_temp = 0.0
    TP = 0.0
    TP_pre = 0.0
    FP = 0.0
    FP_pre = 0.0
    P = 0;
    N = 0;
    last_prob = probs[i_sorted[0]] + 1.0
    for i in xrange(len(probs)):
        if last_prob != probs[i_sorted[i]]:
            auc_temp += (TP+TP_pre) * (FP-FP_pre) / 2.0
            TP_pre = TP
            FP_pre = FP
            last_prob = probs[i_sorted[i]]
        if labels[i_sorted[i]] == 1:
          TP = TP + 1
        else:
          FP = FP + 1
    auc_temp += (TP+TP_pre) * (FP-FP_pre) / 2.0
    auc = auc_temp / (TP * FP)
    return auc

def read_file():
    labels = []
    probs = []
    for line in sys.stdin:
        sp_line = line.split()
        labels.append(int(sp_line[0]))
        if float(sp_line[1]) < 1e-8:
            probs.append(1e-8)
        else:
            probs.append(float(sp_line[1]))
    return labels,probs
def get_pos_count(labels):
    count = 0
    for i in labels:
        if i == 1:
            count +=1
    return count

def scoreMetrics(labels,probs):
    i_sorted = sorted(xrange(len(probs)),key=lambda i: probs[i],
                      reverse=True)
    auc_temp = 0.0
    rmse_temp = 0.0
    logloss_temp = 0.0
    TP = 0.0
    TP_pre = 0.0
    FP = 0.0
    FP_pre = 0.0
    P = 0;
    N = 0;

    last_prob = probs[i_sorted[0]] + 1.0
    for i in xrange(len(probs)):
        if last_prob != probs[i_sorted[i]]:
            auc_temp += (TP+TP_pre) * (FP-FP_pre) / 2.0
            TP_pre = TP
            FP_pre = FP
            last_prob = probs[i_sorted[i]]
        if labels[i_sorted[i]] == 1:
          TP = TP + 1
        else:
          FP = FP + 1
        
        #add by myself to avoid inputing 0.0 or 1.0 score
        if probs[i_sorted[i]] == 0.0 :
            probs[i_sorted[i]] = 0.000001
        if probs[i_sorted[i]] == 1.0 :
            probs[i_sorted[i]] = 0.999999
        #if probs[i_sorted[i]]>0 and (1-probs[i_sorted[i]])>0:
        logloss_temp += labels[i_sorted[i]]*math.log(probs[i_sorted[i]])+(1-labels[i_sorted[i]])*math.log(1-probs[i_sorted[i]])
        
        rmse_temp += math.pow(labels[i_sorted[i]] - probs[i_sorted[i]], 2)
    auc_temp += (TP+TP_pre) * (FP-FP_pre) / 2.0
    auc = auc_temp / (TP * FP)
    rmse = math.sqrt(rmse_temp / len(probs))
    logloss = -logloss_temp/len(probs)
    return auc, rmse ,logloss

if __name__ == "__main__":
    #print "usage:cat out | AUC.py"
    labels,probs = read_file()
    #auc = scoreAUC(labels,probs)
    auc,rmse,logloss = scoreMetrics(labels,probs)
    pos_count = get_pos_count(labels)
    count = len(labels)
    print "Logloss:",logloss
    print "AUC:",auc
    print "RMSE:",rmse
    print "Count:",count
    print "Pos:",pos_count
    print "Neg/Pos:",float(count-pos_count)/pos_count

