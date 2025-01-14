# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:56:09 2018

@author: fatoks
"""
#this code split the dataset 2523 in train and test by 1800 and 723
import numpy as np
import pandas as pd

np.random.seed(1)
full_labels = pd.read_csv('./data1/Skycatch.csv')
full_labels.head()
grouped = full_labels.groupby('filename')
grouped.apply(lambda x: len(x)).value_counts()
gb = full_labels.groupby('filename')
grouped_list = [gb.get_group(x) for x in gb.groups]
train_index = np.random.choice(len(grouped_list),size=1800,replace=False)
test_index = np.setdiff1d(list(range(2523)), train_index)
train = pd.concat([grouped_list[i] for i in train_index])
test = pd.concat([grouped_list[i] for i in test_index])
train.to_csv('train_labels.csv', index=None)
test.to_csv('test_labels.csv', index=None)
