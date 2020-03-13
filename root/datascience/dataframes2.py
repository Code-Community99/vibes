import pandas as pd
import numpy as np


#open the csv
file = pd.read_csv("nba.csv")
#print(file)

print(file.head(2))#gets first 2 rows
#methods used for 

print(file.shape)

#file.dtypes   gives datatypes of every column
 print(file.axes) #gives a list of columns

 print(file.info())  #gives the summary of the dataframes#

newCsv = pd.read_csv("revenue.csv" ,index_col = "Date")
print(newCsv)

colSum = newCsv.sum()
print(colSum)  #returns the sum of the columns...downwards...totals of each column...in col 1,2,3


#for summing rows  ...use
rowSum = newCsv.sum(axis= "columns")

print(rowSum)

#you can extract a column by its name it has no spaces
#e.g
file = pd.read_csv("nba.csv")

#print(file.Name)   #gets the column named Name


#if the name has spaces you can put them in a list structure e.g

print(file["College"])# the best way

#extracting more than two columns

ex1 = file [ ["Name" ,"Team","College","Salary"] ]
#print(ex1)

#adding new column  to a dataframe
#just assign a value to a column you want
#e.g adding column called sport to ...file...
file["Sports"] = "Basketball"  #add the column with the name basketball to the whole dataframe

print(file)


#Insert method  e.g
#file.insert(locationIndexYouWant,column = nameYouWant ,value="ValueYouWannaInsert")


#to count the occurence of values use value_counts()

print(file["Team"].value_counts())#gets occurence of the team

#dealing with null values designated with NAN
#can be down through obj.dropna()
#it drops any row that has one or more NAN
print(file.dropna())

#placing a subset method performs dropna for the specified column 

print(dropna(submit = ["Names","College"]))

#filling NAN values with another values
#.....replace = file.fillna(0) #this works for consistent dataset...with same datatype

#example2 that makes it more consistent to each column
file["salary"].fillna(0,inplace = True)
file["College"].fillna("No College Found" , inplace=True)

#converting datatypes using astype() method

#file.dtypes .. or file.info()..gives datatypes for every column

#converting float to intergers is as shown below for salary
file["Salary"]=file["Salary"].astype("int")

file["Team"] .nunique()  #gets the number of i=unique elements
file["Team"] = file["Team"].astype("categorical")  #categorises data into different unique categories

#values can be sorted using sort_values()  example
 sort = file.sort_values("Name" , ascending = True)# sorts by name


#sorting using multiple columns
#example
file.sort_values( ["Team" , "College"] , ascending = [True , False] )
#the above is asc True for Team and False for college

#rank method 
#rank method is given into a single series example
file["Salary"].rank(ascending=False) #used to add position in rank types






```