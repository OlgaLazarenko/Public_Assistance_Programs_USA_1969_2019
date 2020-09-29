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

import sys
input_file = 'E://_Python_Projects_Data/Public_Assistance_Programs_US/SNAP_history_1969_2019.csv'
output_file = 'E://_Python_Projects_Data/Public_Assistance_Programs_US/SNAP_history_output.csv'
with open(input_file,'rt') as data_file:
    with open(output_file,'w') as result_file:
        header = data_file.readline()
        result_file.write(header)

        
        lines=data_file.readlines()
        for line in lines:
            result_file.write(line)


with open(output_file,'rt') as file: 
	for i in range(0,11):
		text=file.readline() #read the first ten rows
		print(text, end='')
print('------------------------------------------')
print()

