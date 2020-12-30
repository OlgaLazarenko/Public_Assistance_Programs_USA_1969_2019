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
new_output_file = config.get('SNAP_history_files','New_Output_File')


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

new_output_file = new_output_file[1:]
new_output_file = new_output_file[:-1]
print(new_output_file)




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
create a function to validate values at the following columns:
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
                    
                    output_file_writer.writerow(header) # write the header to the output file
                    errors_file_writer.writerow(header) # write the header to the errors file
                    line_count += 1
                
                else: # rows with values
                    new_line = [] # the list will contain values without comma 
                    for item in line :
                        item = item.replace(',','')
                        new_line.append(item)
                
                
                   

                    # validate the values at the column 'Fiscal Year'
                    # call the function 'validate_fiscal_year(fis_year)'
                    # which returns True(for values from 1969 to 2019 including) and returns False otherwise
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
                    else :
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

# open the output file with the validated data, create new columns,
# calculate values for the new columns and write the values to the output file

with open(output_file, 'r') as file1 :
    with open(new_output_file,'w', newline = '') as new_file :
        data_reader = csv.reader(file1, delimiter = ',') # reader to read the output file
        data_writer = csv.writer(new_file, delimiter = ',') # writer to write to the new output file 

        Particip_dict = {} # dictionary {fiscal year: avg participation}
        Benefit_dict = {}  # dictionary {fiscla year: avg benefit per person}

        zero_year = '1968'
        for row in data_reader :
            # populate the dictionaries with the values of the output file with validated data
            Particip_dict.update({row[0]:row[1]}) 
            Benefit_dict.update({row[0]:row[2]})


        
        # the values for the key='1968' will be taken from the mentioned above dictionaries
        zero_particip = Particip_dict.get('1969') 
        zero_benef = Benefit_dict.get('1969')

        # key:value where key='1968' to be added to the dictionaries
        Particip_dict.update({zero_year:zero_particip})
        Benefit_dict.update({zero_year:zero_benef})

        print()
      
        # create the header(the name of the columns)
        list_columns = ['Fiscal Year','Average Particiaption','% Change Avg Participation','Average Benefit per Person','% Change Avg Benefit per Person']
        # write the header to the new output file
        data_writer.writerow(list_columns) 


        # now we have to calculate the values for the new columns ('% Change Avg Participation' and '% Change Avg Benefit per Person' )
        year_num = int()
        
        for year_num in range(1969,(2019+1)) :
            current_year = year_num
            previous_year = (year_num) - 1
            
            current_particip = Particip_dict.get(str(current_year))
            previous_particip = Particip_dict.get(str(previous_year))
            change_particip =float(current_particip) - float(previous_particip) 
            
            current_benef = Benefit_dict.get(str(current_year))
            previous_benef = Benefit_dict.get(str(previous_year))
            change_benef = float(current_benef) - float(previous_benef)

            # Formula:    % change = (change * 100)/previous_value
            # perform the calculations
            change_percent_particip = round( ( (change_particip)*100/float(previous_particip)), 1)
            change_percent_benef = round( ((change_benef)*100/float(previous_benef)), 1)
            
            # compose a row for the new output file 
            list_new_values = [str(year_num),str(current_particip),str(change_percent_particip)
                                            ,str(current_benef),str(change_percent_benef)]

            # write the row to the new output file
            data_writer.writerow(list_new_values) # write to the new output file
            
# because the new output file is small we can            
# display the data from the now output file
print('The new output file:')
with open(new_output_file, 'rt') as file :
        values = file.readlines()
        for rows in values :
             print(rows, end = '')



#   ***   Plotting the output data using Pandas    ***
import pandas as pd

# read the output validated data into the dataframe 
df_public_assistance = pd.read_csv("E:\_Python_Projects_Data\Public_Assistance_Programs_US\_Output_SNAP_history_1969_2019.csv" ,
                    usecols = ['Fiscal Year',
                    'Average Participation' , 
                    'Average Benefit Per Person' ,
                     'Total Benefits(M)']
                )
print(df_public_assistance)
print()
print('-----------------------------')
print()
print('Create a line chart to show how the average benefit per person changed over the time')
print()
# add Matplotlib syntax to show the plot
import matplotlib.pyplot as plt
    
df_public_assistance.plot( x = 'Fiscal Year' ,
                             y = 'Average Benefit Per Person' , 
                             kind = 'line' ,
                             figsize = (8,6) ,
                             color = 'red' ,
                             grid = True )


# insert the title, the name for x-axis, y-axis
plt.title('Average benefit per person ($/month) over time')
plt.xlabel('Year')
plt.ylabel('Monthly Amount, $')
plt.legend(['average monthly amount per person,$'])
plt.show()

       
            
