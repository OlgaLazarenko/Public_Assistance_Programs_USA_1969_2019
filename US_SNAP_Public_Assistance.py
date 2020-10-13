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
errors_file = 'E://_Python_Projects_Data/Public_Assistance_Programs_US/SNAP_history_errors.csv'

# create a function to modify every row and turn the rows to lists and validate the values
# each row contains 6 values/ columns
# a problem is some values in the row have the double quotes because it is a decimal number
# integer values do not have double quotes 
# the function will remove double quotes and the comma separating thousands
# the function will return a list of values to be validated
print()

# create a function to modify rows, some values incuded double quotes
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
    
    correct_line_list = []
    for item in line_list :
        item = item.replace(',','')  
        item = item.strip() 
        correct_line_list.append(item)
    return correct_line_list


# create a function to remove a comma in a value
def remove_comma(value) :
    new_value = value.replace(',','')
    return new_value


# validate the columns values
# create a function to validate the values in the column Fiscal Year (should be a positive integer, from 1969 to 2019)



def validate_fiscal_year(fis_year) :
    if fis_year.isdigit() :
        if 1969 <= int(fis_year) <= 2019 :
            result_year = True
        else:
            result_year = False
    else:
        result_year = False
    return result_year


'''
create a function to validate values at the following comunms:
Average Participantion ... result_list[1]
Average Benefit Per Person ... result_list[2]
Total Benefits(M) ... result_list[3]
Other Costs ... result_list[4]
Total Costs(M) ... result_list[5]
'''
def validate_expense(cost) : # the function will return True or False
    cost = cost.replace('.','') # remove the dot from the value
    result_cost = cost.isdigit()
    return result_cost


# create a function to turn a list into a csv string
def turn_list_into_csv_string(my_list) :
    my_str = ",".join(my_list)
    return my_str



with open(input_file, mode = 'r') as data_file :
    with open(output_file, mode = 'w', newline = '') as result_file : # newline='' is used to avoid an empty string after each row
        data_file_reader = csv.reader(data_file, delimiter = ',', quotechar = '"') # to read the initial file
        output_file_writer = csv.writer(result_file, delimiter = ',') # to write to the output file
        
        
        line_count = 0
        for line in data_file_reader :
            if line_count == 0 :
                header = line
                output_file_writer.writerow(header)
                print(line)
                print('***********')
                line_count += 1
                
            else:
                new_line = [] # the list will contain values without comma 
                for item in line :
                    item = item.replace(',','')
                    new_line.append(item)
                print(new_line)
                output_file_writer.writerow(new_line)
                line_count += 1
               
        


           
                

print('_________________________________')
with open(output_file,'rt') as file : 
	for i in range(0,6) :
	    text=file.readline() 
	    print(text, end = '')
print('------------------------------------------')

'''
with open(errors_file, 'rt') as file2 :
    for n in range (0,6) :
        text2 = file2.readline()
        print(text2, end = '')

'''
