import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import platform
import matplotlib
import matplotlib.font_manager as fm
from matplotlib import font_manager, rc

path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
fontprop = fm.FontProperties(fname=path, size=18)

cctv_seoul = pd.read_excel('./data/cctv_source.xlsx', sep=',\s+', delimiter=',', encoding="utf-8", skipinitialspace=True)


cctv_seoul.rename(columns={cctv_seoul.columns[0]: '자치구'}, inplace=True)
cctv_seoul['자치구'] = cctv_seoul['자치구'].str.strip()
cctv_seoul['자치구'] = cctv_seoul['자치구'].str.replace(" ","")
#print(cctv_seoul.sort_values(by='소계', ascending=False).head(5))

cctv_seoul['최근증가율'] = (cctv_seoul['2018년'] +cctv_seoul['2017년'] + cctv_seoul['2016년'] + cctv_seoul['2015년']+cctv_seoul['2014년']+cctv_seoul['2013년']+cctv_seoul['2012년']) / cctv_seoul['2011년 이전']
#print(cctv_seoul.sort_values('최근증가율', ascending= False).head(5))

pop_seoul = pd.read_excel('./data/population_seoul.xls', sep=',\s+', delimiter=',', encoding="utf-8", skipinitialspace=True)
pop_seoul.drop([0], inplace =True)

pop_seoul['외국인비율'] =pop_seoul['인구 등록외국인 계'] / pop_seoul['인구 합계 계'] * 100
pop_seoul['고령자비율'] =pop_seoul['65세이상고령자'] / pop_seoul['인구 합계 계'] * 100

data_result = pd.merge(cctv_seoul, pop_seoul, on='자치구')
del data_result['2011년 이전']
del data_result['2012년']
del data_result['2013년']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']
del data_result['2017년']
del data_result['2018년']

del data_result['인구 합계 남자']
del data_result['인구 합계 여자']

del data_result['인구 등록외국인 남자']
del data_result['인구 등록외국인 여자']

del data_result['인구 한국인 남자']
del data_result['인구 한국인 여자']
del data_result['기간']
del data_result['세대']
del data_result['세대당인구']


data_result.rename(columns={data_result.columns[3]: '인구수'}, inplace=True)
data_result.rename(columns={data_result.columns[4]: '한국인'}, inplace=True)
data_result.rename(columns={data_result.columns[5]: '외국인'}, inplace=True)
data_result.rename(columns={data_result.columns[6]: '고령자'}, inplace=True)

data_result.sort_values(by ='소계', ascending=False)
print(data_result.sort_values(by ='소계', ascending=False).head())

#data_result['소계'].plot(kind='barh', grid=True, figsize=(10,10))

data_result['소계'].sort_values().plot(kind='barh', grid=True, figsize=(10,10))


#plt.ylabel('하이로', fontproperties=fontprop)
#plt.show()

fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)

plt.figure(figsize=(14,10))




f1 = np.poly1d(fp1)
fx = np.linspace(100000, 700000, 100)
data_result['오차'] = np.abs(data_result['소계'] - f1(data_result['인구수']))
plt.figure(figsize=(10,10))
plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')


plt.figure(figsize=(14,10))
plt.scatter(data_result['인구수'], data_result['소계'], 
            c=data_result['오차'], s=50)


plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')
df_sort = data_result.sort_values(by='오차', ascending=False)            
for n in range(10):
    print(df_sort['자치구'][n])
    plt.text(df_sort['인구수'][n]*1.02, df_sort['소계'][n]*0.98, 
             df_sort['자치구'][n], fontsize=15, fontproperties=fontprop)



plt.xlabel('인구수', fontproperties=fontprop)
plt.ylabel('CCTV', fontproperties=fontprop)
plt.grid()
plt.show()