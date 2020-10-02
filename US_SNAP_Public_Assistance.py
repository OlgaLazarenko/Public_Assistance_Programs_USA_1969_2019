#!/bin/python3
'''

Project Name: US_Public_Food_Assistance_1969_2019
Date: Sep 28, 2020
Author: Olga Lazarenko
Description: The dataset provides data about public assistance probram SNAP 

            SNAP (Supplemental Nutrition Assistance Program) is the successor to 
            the Food Stamps probram. The program provides food assistance 
            to low-income families in the form of a debit card.
            According to 2016 POS data about SNAP-eligible vendors the three most 
            purchased types of food: meats, sweetened beverages, vegetables.
Purpose: Explore various aspects of US Public Assistance. 
        Create visualizations to show trends over recent years.
                1) read the initial data from the dataset
                2) validate the data
                3) write the validated data to the output file
                4) invalide data will be written to the errors file
                5) if possible, to correct invalide data and write them to the output file
                7) create new calculated fields:
                    - Avg Participant, % change
                    - Avg Benefit per Person, % change
                    


Specification: the dataset contains 6 fields/ columns
                1) Fiscal Year (should be between 1969 and 2019 including, fiscal year runs from October to October)
                2) Average Participants (thousands of people)
                3) Average Benefits (average montly dollars per person)
                4) Total Benefits (USD millions)
                5) Other Costs (USD millions, including the Federal share of State,
                                admininstrative expenses, Nutrition Education, employmnet and training)
                6) Total Costs(USD millions)

Data Source: https://www.kaggle.com/jpmiller/publicassistance
            SNAP_history_1069_2019

'''

import sys, csv

input_file = 'E://_Python_Projects_Data/Public_Assistance_Programs_US/SNAP_history_1969_2019.csv'
output_file = 'E://_Python_Projects_Data/Public_Assistance_Programs_US/SNAP_history_output.csv'

# create a function to modify every row and turn the rows to lists and validate the values
# each row contains 6 values/ columns
# a problem is some values in the row have the double quotes because it is a decimal number
# integer values do not have double quotes 
# the function will remove double quotes and the comma separating thousands
# the function will return a list of values to be validated
print()
my_line = '''2000,"17,194",72.62,"14,984.32","2,070.70","17,054.02"'''
'''
x = my_line.splitlines()
print(x)
print()
new_line = my_line.split('"')
print(new_line)
print('********************')

for a in new_line:
    if a == ',' or a == '' :
        new_line.remove(a)
print(new_line)
print()

new_list = []
for item in new_line :
    item = item.replace(',','')
    new_list.append(item)
print(new_list)
print('@ --------------------- @')
'''

# create a function to modify rows
def modify_row(my_line) :
    new_line = my_line.splitlines()
    new_line = my_line.split('"')
    for a in new_line :
        if a == ',' or a == '' :
            new_line.remove(a)
        a.replace(', ','')

    line_list = []
    for a in new_line :
        line_list.append(a)
    
    print(line_list)
    print('######')
    
    
    return line_list

    

    # call the function modify_row(my_line)
print('++++++++++++++++++++++')
result = modify_row(my_line) 
print(result)
print('++++++++++++++++++++++')


'''
print()
my_string = '2000,"17,194",72.62,"14,984.32","2,070.70","17,054,02"'
line = my_string
print(my_string)
print()
def modify_line(my_string) :
    new_string = my_string.split('"')
    print(new_string)
    print()

    my_list = []

    # value[0]
    part_list = new_string[0].split(',')
    print('-------------')
    part_list.pop(3)
    print(part_list)

    for a in part_list :
    my_list.append(a)

    # value[1]
    new_string[1] = new_string[1].replace(',', '')
    my_list.append(new_string[1])

    print('**********')
# value[2]
new_string[2] = new_string[2][1:4]
print(new_string[2])
print('**********')
part_list = new_string[2].split(',')
print(part_list)


for a in part_list:
    my_list.append(a)

# value[3]
print(new_string)
print(new_string[3])
new_string[3] = new_string[3].replace(',','')
print(new_string[3])
my_list.append(new_string[3])
print(my_list)

# value[4]
part_list = new_string[4].split(',')
print(part_list)
part_list.pop(0)
for item in part_list:
    my_list.append(item)
print(my_list)
'''
with open(input_file,'rt') as data_file:
    with open(output_file,'w') as result_file:
        reader = csv.reader(data_file, quotechar = '"',delimiter = ',',quoting = csv.QUOTE_ALL, skipinitialspace = True)
        header = data_file.readline()
        result_file.write(header)

        line_list = [] # declare a list
        lines=data_file.readlines()
        for line in lines:
            #print(type(line))
            
        
            # perform the data validation for each column/field
            # slit each line  into the  list of values
            
            


            result_file.write(line)


with open(output_file,'rt') as file: 
	for i in range(0,20):
	    text=file.readline() #read the first ten rows
	    print(text, end='')
print('------------------------------------------')
print()

