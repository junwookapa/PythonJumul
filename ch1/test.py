import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cctv_seoul = pd.read_excel('./data/cctv_source.xlsx', encoding='utf-8')



#print(cctv_seoul.sort_values(by='소계', ascending=False).head(5))

cctv_seoul['최근증가율'] = (cctv_seoul['2018년'] +cctv_seoul['2017년'] + cctv_seoul['2016년'] + cctv_seoul['2015년']+cctv_seoul['2014년']+cctv_seoul['2013년']+cctv_seoul['2012년']) / cctv_seoul['2011년 이전']
#print(cctv_seoul.sort_values('최근증가율', ascending= False).head(5))

pop_seoul = pd.read_excel('./_1_SeoulCctv/population_seoul.xls', encoding='utf-8')
pop_seoul.drop([0], inplace =True)

pop_seoul['외국인비율'] =pop_seoul['인구 등록외국인 계'] / pop_seoul['인구 합계 계'] * 100
pop_seoul['고령자비율'] =pop_seoul['65세이상고령자'] / pop_seoul['인구 합계 계'] * 100


print(pop_seoul.sort_values(by='고령자비율', ascending=False).head())