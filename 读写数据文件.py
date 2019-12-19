# coding:utf-8
import pandas as pd

df=pd.read_csv('.\\data_set\\country.csv',index_col=0)
df.to_excel('.\\data_set\\country.xlsx')
df.to_json('.\\data_set\\country.json')