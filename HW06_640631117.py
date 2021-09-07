# -*- coding: utf-8 -*-
"""
Date: September 7,2021
Topic: Dataframe Manipulation (HW06)
@author: Chanwit Chanton ID:640631117
Third Commited
"""
import pandas as pd
df=pd.read_csv("avocado.csv") #Import dataset by using pandas

'''1)Which region sold the largest amount of avocado ?
In this region, where the biggest lot of sold avocado came from (4046, 4225, 4770) ?'''

print("Answer No.1\n")
df11=df.groupby('region')[['Total Volume','4046','4225','4770']].sum() # find sumation of Total Volume of avocado and each label which group by the region names
print("The region which sold the largest amount of avocado is",df11['Total Volume'].idxmax(),'\n') # Print out the region name which sold the largest amount of avocado

df12=df11.loc[df11['Total Volume'] == df11['Total Volume'].max()] # Extract the record of region which sold the largest amount of avocado
df1A=df12.drop(['Total Volume'], axis=1) # Cutting down the Total Volume columns 
print("In this region, the biggest lot of sold avocado came from the label No.",df1A.iloc[0].idxmax(),'\n') # Find out the biggest lot of sold avocado from the label No.

'''2)Which region sold the smallest amount of avocado ?
In this region, where the biggest lot of sold avocado came from (4046, 4225, 4770) ?'''

print("Answer No.2\n")
print("The region which sold the smallest amount of avocado is",df11['Total Volume'].idxmin(),'\n') # Print out the region name which sold the smallest amount of avocado

df21=df11.loc[df11['Total Volume'] == df11['Total Volume'].min()] # Extract the record of region which sold the smallest amount of avocado
df2A=df21.drop(['Total Volume'], axis=1) # Cutting down the Total Volume columns 
print("In this region, the biggest lot of sold avocado came from the label No.",df2A.iloc[0].idxmax(),'\n') # Find out the biggest lot of sold avocado from the label No.

'''3) Which region sold the highest price of avocado in average?'''

print("Answer No.3\n")
df31=df.groupby('region')[['AveragePrice']].mean() # find mean of AveragePrice of avocado which group by the region names
print(" The region which sold the highest price of avocado in average is",df31['AveragePrice'].idxmax(),'\n') # Print out the region name which sold the highest price of avocado in average

'''4) Find the total amount of income (Avg_Price*Total_Volume) of each region?'''

print("Answer No.4\n")
df41=df.groupby('region')[['Total Volume']].sum() # find sumation of Total Volume of avocado which group by the region names
df42=df.groupby('region')[['AveragePrice']].mean() # find  mean of AveragePrice of avocado which group by the region names
df4A=pd.DataFrame({"Amount of Income": []}) # Create empty new dataframe which name "Amount of Income"
df4A["Amount of Income"]=df41["Total Volume"]*df42["AveragePrice"] # Compute the Amount of Income by using mean of Avg_Price multiply by sumation of Total_Volume for each region
print(df4A,'\n') # Print out the total amount of income for each region

'''5) Let AVOCADO Average Weight : 4046 => 4 ounces, 4225 => 9 ounces, 4770 => 12 ounces
Find the number of sold avocadoes by region ?
Which region sold the largest number of avocados?'''

print("Answer No.5\n")
df51=df.groupby('region')[['4046','4225','4770']].sum() # find sumation of Total Volume of avocado in each label which group by the region names
df51.columns = ['4 ounces', '9 ounces','12 ounces'] # Rename label No. to size of avocado
df51['4 ounces']/=4 # Divide the Average Weight of avocado to the sumation of Total Volume of avocado in each label/ size 
df51['9 ounces']/=9
df51['12 ounces']/=12
df5A=pd.DataFrame({"Number of Sold Avocadoes in ounces": []}) # Create empty new dataframe which name "Number of Sold Avocadoes in ounces"
df5A["Number of Sold Avocadoes in ounces"]=df51["4 ounces"]+df51["9 ounces"]+df51["12 ounces"] # Compute Number of Sold Avocadoes in ounces by using sumation of all of labels/sizes
print(df5A,'\n') #  show the number of sold avocadoes by region
print("The region sold the largest number of  in ounces is",df5A["Number of Sold Avocadoes in ounces"].idxmax(),'\n') # Find out the region sold the largest number of  in ounces

'''6) Normally, the customers buy the avocados by unit or in a bags ?'''

print("Answer No.6\n")
df['Total Units']= df.iloc[:, 4:7].sum(axis=1) # Create new column name "Total Units" to contain the sumation of total volume of avocado from all labels '4046','4225','4770'
Unit_buy=sum(df['Total Units'] > df['Total Bags']) # Count condition to check the case that people buy in unit more for each record
Bag_buy=sum(df['Total Units'] < df['Total Bags']) # Count condition to check the case that people buy in bag more for each record

if Unit_buy > Bag_buy:
    print("Generally, the customers buy the avocados as an unit\n")
else:
    print("Generally, the customers buy the avocados as a bag\n") # show in general which one is generally
