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
                2) Average Participation (thousands of people)
                3) Average Benefits (average monthly dollars per person)
                4) Total Benefits (USD millions)
                5) Other Costs (USD millions, including the Federal share of State,
                                admininstrative expenses, Nutrition Education, employmnet and training)
                6) Total Costs(USD millions)

Data Source: https://www.kaggle.com/jpmiller/publicassistance
            SNAP_history_1969_2019

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

'''
create a function to modify every row and turn the rows to lists and validate the values;
each row contains 6 values/ columns
a problem is that some values in the row have the double quotes because these values contain the comma
integer values do not have double quotes 
the function will remove double quotes and the comma separating thousands
the function will return a list of values to be validated
'''

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
                if line_count == 0 : # the header
                    header = line
                    # insert new columns name (Avg Participation, % change and Avg Benefit Per Person, % change)
                    print(type(header))
                    print(header)
                    header.insert(6,'Avg Participation % change')
                    header.insert(7,'Avg Benefit Per Person % change')
                    print(header)
                    output_file_writer.writerow(header) # write the header to the output file
                    errors_file_writer.writerow(header) # write the header to the errors file
                    line_count += 1
                
                else: # rows with values
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

                        wrong_year = new_line[0]
                        correct_year = wrong_year[0:4]

                        new_line.pop(0) # wrong year values is removed from the line
                        new_line.insert(0,correct_year) # the correct year value is inserted into the line
                        
                    '''
                    validate the values of the other columns:
                    'Average Participation' 
                    'Average Benefit Per Person' 
                    'Total Benefits(M)' 
                    'Other Costs' 
                    'Total Costs(M)'

                    call the function 'validate_expense(cost)'
                    '''
                    
                    for n in range(1,5) : # iterate from the column 2) to the column 5) and validate the values
                        # call the function validate_expense(cost) which returns True/ or False
                        result_cost = validate_expense(new_line[n])
                        if result_cost == False :
                            errors_file_writer.writerow(new_line)
                            continue

                    result_cost = validate_expense(new_line[5]) # validate the values of the last column 6)
                    if result_cost == False :
                        errors_file_writer.writerow(new_line)
                        continue
                    else:

                        # create dictionaries
                        Participant_dict = {}
                        Benefit_dict = {}

                        current_year = new_line[0]
                        current_particip = new_line[1]
                        current_benef = new_line[2]

                        Participant_dict.update({current_year:current_particip})
                        Benefit_dict.update({current_year:current_benef})


                        zero_year = 1968
                        zero_particip = Participant_dict.get(1969)
                        zero_benef = Benefit_dict.get(1969)

                        print(zero_year)
                        print(zero_particip)
                        print(zero_benef)

                        output_file_writer.writerow(new_line)
                        
print('_________________________________')
print('The output file:')
# at the output file the data is organized at the consecutive Fiscal Year order ( from 1969 to 2019)
with open(output_file,'rt') as file :
    validated_data = file.readlines()
    # because the output file is not big, let's look at the all validated rows in the output file 
    # to ensure the fiscal years in the correct sequence/ order
    for rows in validated_data :
        print(rows, end = '')
    
print('___________________________________')

print('The errors file:')
with open(errors_file, 'rt') as file2 :
    with open(output_file, 'a') as file3:
        
        invalid_data = file2.readlines()
        for rows in invalid_data :
             print(rows, end = '')
        


print()
print()
'''
# read the output file with validated data and create two calculated columns
# at this step the data of each columns are valid
# create  new columns with calculated values 
# 1) Avg Participant, % change
# 2) Avg Benefit per Person, % change
                        
# new_line
# create a dictioanary Participant_dict = [1961:N1, 1962:N2.....]

# create dictionaries Participant_dict={year:thousands of people} and Benefit_dict={year:avg mounthly dollars per person}
                        Participant_dict = {}
                        Benefit_dict = {}

                        

                        current_year = int(new_line[0])
                        print(current_year)
                        pre_year = int(new_line[0])-1
                        print(pre_year)
                        current_particip = float(new_line[1])
                        current_benef = float(new_line[2])

                        # populate the dictionalry
                        Participant_dict.update({current_year:current_particip})
                        Benefit_dict.update({current_year:current_benef})




                        # the year of 1969 will be the starting point 
                        # we make the assuptions the values for the 1968 will be the same as for 1969 year
                        zero_year = 1968
                        zero_particip = int(new_line[1])
                        
                        # add this to the dictionary
                        Participant_dict.update({zero_year:zero_particip})
                        print(Participant_dict)

                        zero_benef = new_line[2]
                        Benefit_dict.update({zero_year:zero_benef})
                        print(Benefit_dict)

                        # the formula to calculate % change  = ( ((previous year value)-(current year value))*100 )/ (previous year value)
                       
                        pre_particip = float()
                        pre_particip = (Participant_dict.get(pre_year))
                        print(pre_particip)
                        change_particip = float()

                        # change_particip = ( ((pre_particip)-(current_particip))*100/(pre_particip) )      
            
'''     
    