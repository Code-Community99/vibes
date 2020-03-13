import pandas as pd
import numpy as np


#get data loaded into the dataframe

data = pd.read_csv("2009_census_data_roofing_materials.csv")

#replace files with NAN with a certain flags
#data[].fillna(0, inplace=True)

#here are the columns for our data
'''['District', 'rural/urban', '%_of_Households_Corrugated_Iron_Sheets','%_of_Households_Tiles', '%_of_Households_Concrete',
       'Asbestos_%_of_Households_Sheets', '%_of_Households_Grass',
       '%_of_Households_Makuti', '%_of_Households_Tin',
       '%_of_Households_Mud/Dung', '%_of_Households_Other', 'Households',
       'No_Corrugated_Iron_Sheets', 'No_Tiles', 'No_Concrete',
       'No_Asbestos_Sheets', 'No_Grass', 'No_Makuti', 'No_Tin', 'No_Mud/Dung',
       'No_Other', 'County', 'MTEF', 'Location_1', 'Province', 'OBJECTID']'''


for x in data.columns:
	print(x)#print columns
#print(data.columns)

#data filtering with NAN and replace them
#replace files with NAN with a certain flags
#data[].fillna(0, inplace=True)
data.fillna("Not Found" ,inplace=True)

print(data)

#get the mean population
meanHouseholds = data["Households"]
meanIronSheets = data["No_Corrugated_Iron_Sheets"]
meanAsbesto = data["No_Asbestos_Sheets"]

print(meanHouseholds)
print(meanIronSheets)
print(meanAsbesto)