import pandas as pd
import os
import numpy as np
import collections
import datetime
from sklearn.preprocessing import OneHotEncoder
from sklearn.svm import SVC



# 文件名
filename = './NSL-KDD/KDDTrain+_20Percent.txt'
test_data_filename = './NSL-KDD/KDDTest+.txt'
# 攻击类型字典
attack_dict = {
    'normal': 'normal',
    
    'back': 'DoS',
    'land': 'DoS',
    'neptune': 'DoS',
    'pod': 'DoS',
    'smurf': 'DoS',
    'teardrop': 'DoS',
    'mailbomb': 'DoS',
    'apache2': 'DoS',
    'processtable': 'DoS',
    'udpstorm': 'DoS',
    
    'ipsweep': 'Probe',
    'nmap': 'Probe',
    'portsweep': 'Probe',
    'satan': 'Probe',
    'mscan': 'Probe',
    'saint': 'Probe',

    'ftp_write': 'R2L',
    'guess_passwd': 'R2L',
    'imap': 'R2L',
    'multihop': 'R2L',
    'phf': 'R2L',
    'spy': 'R2L',
    'warezclient': 'R2L',
    'warezmaster': 'R2L',
    'sendmail': 'R2L',
    'named': 'R2L',
    'snmpgetattack': 'R2L',
    'snmpguess': 'R2L',
    'xlock': 'R2L',
    'xsnoop': 'R2L',
    'worm': 'R2L',
    
    'buffer_overflow': 'U2R',
    'loadmodule': 'U2R',
    'perl': 'U2R',
    'rootkit': 'U2R',
    'httptunnel': 'U2R',
    'ps': 'U2R',    
    'sqlattack': 'U2R',
    'xterm': 'U2R'
}


def pre_process(df,attack_dict):
    '''
        预处理函数
        输入DataFrame对象、label字典
        返回numpy array对象
        处理流程：
            修改label映射->字符Encoder->onehot Encoder->normlization
    '''
    
    df[41]  = df[41].map(attack_dict)

    arr = [1,2,3,41]
    dics = {}
    num_dict = {}
    for i in arr:
        count_dic = dict(collections.Counter(df.iloc[:,i]))
        dics[i] = dict(zip(list(count_dic.keys()),range(len(list(count_dic.keys())))))
        num_dict[i] = len(list(count_dic))
        df[i] = df[i].map(dics[i])  
    np_data = np.array(df)
    ohe_arr = [1,2,3]
    np_lab = np_data[:,-2:]
    np_data = np_data[:,:-2]

    for i in ohe_arr:
        ohe = OneHotEncoder()
        ohe.fit(list(map(lambda x:[x],range(num_dict[i]))))
        np_data = np.delete(np_data,i,axis=1)
        oh = ohe.transform(list(map(lambda x:[x],list(df[i])))).toarray()
        oh = np.array(oh)
        print(oh.shape)
        np_data = np.c_[np_data,oh]
    np_data = np.c_[np_data,np_lab]

    need_norm = [ 0,  1,  2,  4,  5,  6,  7,  9, 10, 11, 12, 13, 14, 15, 16,
        19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
        34, 35, 36, 37]

    for i in need_norm:
        if np.std(np_data[:,i]) != 0:
            np_data[:,i] = (np_data[:,i] - np.mean(np_data[:,i]))/np.std(np_data[:,i])
    
    return np_data


def make_data(data1,data2,attack_dict):
    data = pd.concat([data1,data2])
    num1 = data1.shape[0]
    num2 = data2.shape[0]
    data = pre_process(data,attack_dict)
    train_data = data[:num1,:]
    test_data = data[num1:,:]
    train_x = train_data[:,:-2]
    train_y = train_data[:,-2]
    test_x = test_data[:,:-2]
    test_y = test_data[:,-2]
    return (train_x,train_y),(test_x,test_y)


if __name__ == "__main__":
    # 读取数据
    df_train = pd.DataFrame(pd.read_table(filename,header=None,encoding='gb2312',sep=','))
    df_test = pd.DataFrame(pd.read_table(test_data_filename,header=None,encoding='gb2312',sep=','))
    (train_x,train_y),(test_x,test_y) = make_data(df_train,df_test,attack_dict)

    print('START')
    start = datetime.datetime.now()
    svm = SVC(C=5000.0, kernel='rbf', gamma=0.001)
    
    svm.fit(train_x,train_y)
    end = datetime.datetime.now()
    t = end-start
    print('END')

    print(t.seconds)

    
    

    print(test_x.shape,train_x.shape)
    y_hat = svm.predict(test_x)
    print('The accuracy is {0}'.format(np.sum(test_y == y_hat)/len(test_y)))