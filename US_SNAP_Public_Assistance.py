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

import configparser
import csv, os


my_files= 'E:\_Python_Projects\GitHub_Public_Assistance_Programs_USA_1969_2019\Data_Files_SNAP_history.ini'

config = configparser.ConfigParser() # initialize a ConfigParser object
config.read(my_files)
print()
print(str(config.sections()) + ' :')


#get the files from the configuration file Variables_File.ini
input_file = config.get('SNAP_history_files','Input_File')
output_file = config.get('SNAP_history_files','Output_File')
errors_file = config.get('SNAP_history_files','Errors_File')
print()
input_file = input_file[1:]
input_file = input_file[:-1]
print(input_file)

output_file = output_file[1:]
output_file = output_file[:-1]
print(output_file)

errors_file = errors_file[1:]
errors_file = errors_file[:-1]
print(errors_file)
print()



# open and read the data file

# create a function to modify every row and turn the rows to lists and validate the values
# each row contains 6 values/ columns
# a problem is some values in the row have the double quotes because it is a decimal number
# integer values do not have double quotes 
# the function will remove double quotes and the comma separating thousands
# the function will return a list of values to be validated


# create a function to validate the values in the column 1) 'Fiscal Year' (should be a positive integer, from 1969 to 2019)
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
Average Participantion ... column 2)
Average Benefit Per Person ... column 3)
Total Benefits(M) ... column 4)
Other Costs ... column 5)
Total Costs(M) ... column 6)
'''

def validate_expense(cost) : 
    cost = cost.replace('.','') # remove the dot from the value
    result_cost = cost.isdigit() # to find out if the value only contains the digits 
    return result_cost # the function will return True or False


with open(input_file, mode = 'r') as data_file :
    with open(output_file, mode = 'w', newline = '') as result_file : # newline='' is used to avoid an empty string after each row
        with open(errors_file, mode = 'w', newline = '') as bug_file :
            data_file_reader = csv.reader(data_file, delimiter = ',', quotechar = '"') # to read the initial file
            output_file_writer = csv.writer(result_file, delimiter = ',') # to write to the output file
            errors_file_writer = csv.writer(bug_file, delimiter = ',') # to write to the errors file 
        
        
            line_count = 0
            for line in data_file_reader :
                if line_count == 0 :
                    header = line
                    output_file_writer.writerow(header) # write the header to the output file
                    errors_file_writer.writerow(header) # write the header to the errors file
                    print(line)
                    line_count += 1
                
                else:
                    new_line = [] # the list will contain values without comma 
                    for item in line :
                        item = item.replace(',','')
                        new_line.append(item)
                
                   

                    # validate the values at the column 'Fiscal Year'
                    # call the function 'validate_fiscal_year(fis_year)'which returns True(for values from 1969 to 2019 including)
                    #  and returns False otherwise
                    result_year = validate_fiscal_year(new_line[0])
                    if result_year == False :
                        errors_file_writer.writerow(new_line) # write to the errors file

                        # correct the invalid fiscal year ( instead of '1982' we have '1983 3]')
                        correct_fis_year = new_line[0][0:5]
                        new_line.remove(new_line[0])
                        new_line.insert(0,correct_fis_year)
                        correct_line = new_line
                        output_file_writer.writerow(correct_line)
                        continue
                    

                    # validate the values of the other columns
                    # 'Average Participation', 'Average Benefit Per Person', 'Total Benefits(M)', 'Other Costs', 'Total Costs(M)'
                    # call the function 'validate_expense(cost)'
                    
                    for n in range(1,6) : # iterate from the column 2) to the column 5) and validate the values
                        result_cost = validate_expense(new_line[n])
                        if result_cost == False :
                            errors_file_writer.writerow(new_line)

                    result_cost = validate_expense(new_line[5]) # validate the values of the last column 6)
                    if result_cost == False :
                        errors_file_writer.writerow(new_line)
                    else:
                        output_file_writer.writerow(new_line)

print('_________________________________')
print('The output file:')
with open(output_file,'rt') as file :
    valideted_data = file.readlines()
    # because the output file is not big, let's look at the all validated rows in the output file 
    # to ensure the fiscal years in the correct sequence/ order
    for rows in valideted_data :
        print(rows, end = '')
    
print('___________________________________')

print('The errors file:')
with open(errors_file, 'rt') as file2 :
    for n in range (0,6) :
        text2 = file2.readline()
        print(text2, end = '')




         
            
        
            
     
