# -*- coding: utf-8 -*-
"""
Date: September 5,2021
Topic: Dataframe Manipulation (HW06)
@author: Chanwit Chanton ID:640631117
Second Commited
"""
import pandas as pd
df=pd.read_csv("avocado.csv") #Import data by using pandas

'''1)Which region sold the largest amount of avocado ?
In this region, where the biggest lot of sold avocado came from (4046, 4225, 4770) ?'''

print("Answer No.1\n")
df1=df.groupby('region')[['Total Volume','4046','4225','4770']].sum()
print("The region which sold the largest amount of avocado is",df1['Total Volume'].idxmax(),'\n')
#maxValues = df1['4046','4225','4770'].max(axis = 1)

#a=df1['Total Volume'].idxmax()


'''2)Which region sold the smallest amount of avocado ?
In this region, where the biggest lot of sold avocado came from (4046, 4225, 4770) ?'''

print("Answer No.2\n")
print("The region which sold the smallest amount of avocado is",df1['Total Volume'].idxmin(),'\n')

'''3) Which region sold the highest price of avocado in average?'''

print("Answer No.3\n")
df31=df.groupby('region')[['AveragePrice']].mean()
print(" The region which sold the highest price of avocado in average is",df31['AveragePrice'].idxmax(),'\n')


'''4) Find the total amount of income (Avg_Price*Total_Volume) of each region?'''

print("Answer No.4\n")
df41=df.groupby('region')[['Total Volume']].sum()
df42=df.groupby('region')[['AveragePrice']].mean()
df4A=pd.DataFrame({"Amount of Income": []})
df4A["Amount of Income"]=df41["Total Volume"]*df42["AveragePrice"]
print(df4A,'\n')

'''5) Let AVOCADO Average Weight : 4046 => 4 ounces, 4225 => 9 ounces, 4770 => 12 ounces
Find the number of sold avocadoes by region ?
Which region sold the largest number of avocados?'''

print("Answer No.5\n")
df51=df.groupby('region')[['4046','4225','4770']].sum()
df51.columns = ['4 ounces', '9 ounces','12 ounces']
df51['4 ounces']*=4
df51['9 ounces']*=9
df51['12 ounces']*=12
df5A=pd.DataFrame({"Number of Sold Avocadoes in ounces": []})
df5A["Number of Sold Avocadoes in ounces"]=df51["4 ounces"]+df51["9 ounces"]+df51["12 ounces"]
print("The region sold the largest number of  in ounces is",df5A["Number of Sold Avocadoes in ounces"].idxmax(),'\n')

'''6) Normally, the customers buy the avocados by unit or in a bags ?'''

print("Answer No.6\n")
df['Total Units']= df.iloc[:, 4:7].sum(axis=1)
Unit_buy=sum(df['Total Units'] > df['Total Bags'])
Bag_buy=sum(df['Total Units'] < df['Total Bags'])

if Unit_buy > Bag_buy:
    print("Generally, the customers buy the avocados as an unit\n")
else:
    print("Generally, the customers buy the avocados as a bag\n")
