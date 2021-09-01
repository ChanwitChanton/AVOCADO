# -*- coding: utf-8 -*-
"""
Date: September 1,2021
Topic: Dataframe Manipulation (HW06)
@author: Chanwit Chanton ID:640631117
First Commited
"""
import pandas as pd
df=pd.read_csv("avocado.csv") #Import data by using pandas

'''1)Which region sold the largest amount of avocado ?
In this region, where the biggest lot of sold avocado came from (4046, 4225, 4770) ?'''

df_=df.groupby('region')[['Total Volume']].sum()

df_sorted=df_.sort_values(by=['Total Volume'], ascending=[False])
print(df_sorted.head(5))

'''2)2)Which region sold the smallest amount of avocado ?
In this region, where the biggest lot of sold avocado came from (4046, 4225, 4770) ?'''

print(df_sorted.tail(5))


'''3) Which region sold the highest price of avocado in average?'''

'''4) Find the total amount of income (Avg_Price*Total_Volume) of each region?'''

'''5) Let AVOCADO  Average Weight : 4046 => 4 ounces, 4225 => 9 ounces, 4770 => 12 ounces
    Find the number of sold avocadoes by region ?
    Which region sold the largest number of avocados ?'''

'''6) Normally, the customers buy the avocados by unit or in a bags ?'''