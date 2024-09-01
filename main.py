import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#used to read excel file and show the first and last 5 rows of excel sheet.
data=pd.read_excel('Generic University Data Updated.xlsx' ,
                    sheet_name= 'Student Data')
print (data.shape)
print (data.head())
print (data.tail())

#This statement will filter out and print the top 5 rows with the filtered out columns
data=data.drop([ "Aid Type", "ID", "Pell Grant Amount", "Postal Code", "City"], axis=1)
print (data.head()) 

#filters made to show California schools
cal_filter = data.loc[data["State"]== "California"]

#filter made to show Female students
female_filter = data.loc[data["Gender"]=="female"]

print ("Data showing only California Schools")
print (cal_filter.head())
print ("Data showing only Female Students")
print (female_filter.head())

#OPEN SCHOOL SHEET
open_school = pd.read_excel('Generic University Data Updated.xlsx' , sheet_name= 'Schools')

open_school.set_index('School', inplace=True)
#open_school.columns = list(map(str, open_school.columns))

#add total column to excel sheet
open_school['Total']=open_school.sum(axis=1, numeric_only=True)

#Define new variable: year, to combine years form 2008-2018
years = list(map(str, range(2008,2018)))

business = open_school.loc[["Business and Management"] , years]
#plot line graph of scholarship amount from school of business

business= business.transpose()

business.plot(kind="line")
plt.title('Scholarship Amount from School of Business')
plt.ylabel('Scholarship Amount')
plt.xlabel('Years')


print(open_school)


all = open_school.loc[["Health Sciences", "Social Sciences", "Arts and Humanities", "Business and Management", "Engineering"],years]
all = all.transpose()
all.plot(kind = "line")
plt.title('All Schools')
plt.ylabel('Scholarship Amount')
plt.xlabel('2018')
all=all.transpose()

#all = all.sort_values(by=['2018'], ascending=False, axis=0)
#print(all['2018'].head(1))

#select appropriate sheet 
programs=pd.read_excel('Generic University Data Updated.xlsx' , sheet_name= 'Programs')

#set index for graph
programs.set_index('Program', inplace=True)

#create a total column
programs['Total']=programs.sum(axis=1, numeric_only=True)

#create total column to show top 5 programs with highest scholarship
programs.sort_values(['Total'], ascending = False, axis = 0, inplace = True)
print(programs.head())
program_five = programs.head()
programs = programs.transpose()
years = list(map(str, range(2008,2018)))
program_five = program_five [years].transpose()

#create a stacked graph
program_five.plot(kind = 'area', stacked = True, figsize=(10,8))
plt.title('Highest Amount of Scholarship between 2008 - 2018')
plt.ylabel('Money')
plt.xlabel('Year')


#select appropriate sheet 
programs=pd.read_excel('Generic University Data Updated.xlsx' , sheet_name= 'Programs')

#set index for graph
programs.set_index('Program', inplace=True)

years = list(map(str, range(2008,2018)))

#define the three business programs
programs_three = programs.loc[["Computer Science", "Information Management", "Business Administration"], years].transpose()


programs_three.plot(kind="hist", figsize = (10, 8))

plt.title('Selected Programs of CS, IM, and BA')
plt.ylabel('Frequency')
plt.xlabel('Scholarship Amount')

plt.show()


