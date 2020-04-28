#!/usr/bin/python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# plot mode to interactive mode
plt.ion()

# read confirmed data
df = pd.read_csv('time_series_covid19_confirmed_global.csv')

# 欠損データ補完
dd=df.iloc[:,0:4].fillna('-')
de=df.iloc[:,4:].fillna(method='ffill',axis=1)
dc=dd.join(de)
# to ndarray
npa=dc.values
row, col = npa.shape
print(npa.shape)
# 平均値の幅
w=7

for loc in range(row):
    x=np.ndarray([])
    y=np.ndarray([])
    for i in range(4,col-w):
        y=np.append(y,np.mean(npa[loc,i:i+w]))
        x=np.append(x,i)
    d=np.diff(y)
    # ここで平均値が200を超えているものに絞る
    if np.max(d) > 200:
        plt.title(npa[loc,0]+' '+npa[loc,1])
        plt.plot(x[1:],d)
        plt.draw()
        # 待ち時間
        plt.pause(5)
        plt.cla()

