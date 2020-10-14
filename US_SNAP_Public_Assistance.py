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
                    print('***********')
                    line_count += 1
                
                else:
                    new_line = [] # the list will contain values without comma 
                    for item in line :
                        item = item.replace(',','')
                        new_line.append(item)
                

                    # valudate the values of the columns

                    # validate the valuses at the column 'Fiscal Year'
                    # call the function 'validate_fiscal_year(fis_year)'which returns True(for values from 1969 to 2019 including)
                    #  and returns False otherwise
                    result_year = validate_fiscal_year(new_line[0])
                    if result_year == False :
                        errors_file_writer.writerow(new_line)
                    

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
	for i in range(0,6) :
	    text=file.readline() 
	    print(text, end = '')
print('------------------------------------------')

print('The errors file:')
with open(errors_file, 'rt') as file2 :
    for n in range (0,6) :
        text2 = file2.readline()
        print(text2, end = '')

print()
# when we look at the errors file, we can notice that there is incorrect Fiscal Year value '1982 3]'
# let's eliminate this error
# to have the correct value, we only take '1982' the first four numbers 
# step 1 : open the errors_file, read the line, correct the error
# step 2 : open the output_file, write the corrected line to it according to the fiscal year sequence

with open(errors_file, mode = 'r') as bad_file :
    with open(output_file, mode = 'a', newline = '') as good_file :
        bad_file_reader = csv.reader(bad_file, delimiter = ',')
        good_file_writer = csv.writer(good_file, delimiter = ',')

        for line in bad_file_reader :
            print(line)
            correct_fis_year = (line[0][0:5])
            print(correct_fis_year)

        line.remove(line[0])
        line.insert(0,correct_fis_year)
        print(line)
