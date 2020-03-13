import pandas as pd
import numpy as np


#Filtering a dataset using some conditions
file = pd.read_csv("employees.csv")

file["Start Date"] =pd.to_datetime(file["Start Date"])#converts into date time
file["Last Login Time"] =pd.to_datetime(file["Start Date"])

#change the value of senior management ionto a bool
file["Senior Management"] = file["Senior Management"].astype("bool")

#groups all people into other , male and female thus reduce space
file["Gender"] = file["Gender"].astype("category")

#you can also use parse_dates attribute to the file example
'''
file = pd.read_csv("employees.csv" , parse_dates = ["Start Date" , "Last Login Time"])
'''



#filtering using a based condition

#get specific where gender is male
file[file["Gender"] == "Male"]#note the use of double equals sign for comparison


#getting all teams that are from finance
file[file["Team"] == "Finance"]  #same as print(file["Team"]=="Finance")

#getting people not in marketing team
notMarketing =[file["Team"] != "Marketing"]


#salary is greater than 10000

file[file["Salary"] > 10000]

#bonas Percent is less than 2
file[file["Bonus %"] < 2]

#working with dates
bfo1990 = file[file["Start Date"] <= "1990-01-01"]

#filtering with ,ore than one conditioon
#and used when both conditions has to be true
#or is used when either is to be true
#clue ========define the conditions separetely and then join them


#getting all females in the marketing team
female = file[file["Gender"] == "Female"]
teamMarketing =[file["Team"] = "Marketing"]


file[female & teamMarketing]

#rows that fits either of the condition passed

seniorMgt = file["Senior Management"]
less2004 =file["Start Date"] <= "2004-01-01"

#combine the condition
file[seniorMgt | less2004]


#many conditions can be combined to filter in more restricted format
#keep the contions is parenthesis example from the above conditions
file[(seniorMgt | less2004 )&(female & teamMarketing)]


#isin() check availabilty of a field
#example inlist format

results = file["Team"].isin(["Marketing" ,"Legal" , "Sales"])


#isnull() checks if a value is null and return true is null values
#notnull() returns true if it contains value
#example
null = file[file["Team"].isnull()]

notNull = file[file["Team"].notnull()]

#between() helps to generate new series within a specified range

#example employees earning between 10000 and 345000

file[file["Salary"].between(10000 , 345000)]

#using betwwen for date 
file[file["Start Date"].between("1990-01-54" , "2010-4-06")]



#duplicate() method allows extraction of duplicate rows
file[file["First Name"].duplicate(keep="first")]#first value of duplicate is not counted as duplicate because keep = first

#unique() and nunique() 
#example
file["Gender"].unique()#gives array of all uniques objects

#getting the total number of unique values
file["Team"].nunique(dropna = False) #same as len(file["Gender"].unique())
print(file)


