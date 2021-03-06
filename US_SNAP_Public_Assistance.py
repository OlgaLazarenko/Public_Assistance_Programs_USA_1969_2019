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
print()
print()



#   ***   Plotting the output data     ***


import pandas as pd    # import pandas package to read the files
import matplotlib.pyplot as plt   # add Matplotlib syntax to show the plot


# 1)   *** ---  Read the validated data --- ***
# 1.1) read the output data 
df_public_assistance = pd.read_csv("E:\_Python_Projects_Data\Public_Assistance_Programs_US\_Output_SNAP_history_1969_2019.csv" ,
                    usecols = ['Fiscal Year',
                    'Average Participation' , 
                    'Average Benefit Per Person' ,
                     'Total Benefits(M)'])

print("DataFrame df_public_assistance")
print(df_public_assistance)
print()
print('-----------------------------')
print()
'''
# 1.2) read the file with calculated columns 
df_avg_change = pd.read_csv("E:\_Python_Projects_Data\Public_Assistance_Programs_US\_New_Output_SNAP_history_1969_2019.csv" ,
                    usecols = ['Fiscal Year',
                    '% Change Avg Participation' , 
                    '% Change Avg Benefit per Person']
                    )
print()
print('dataFrame df_avg_change')
print(df_avg_change)
print()
print()

# ----------------------------------------------------------------------------------------------

# 2)    ***   ---  Create Line Charts  ---   ***
# 2.1) The line chart to display the average benefit per person over time
df_public_assistance.plot( x = 'Fiscal Year' , # define the  x-axis
                             y = 'Average Benefit Per Person' , # define the y-axis
                             kind = 'line' , # define the plot type
                             figsize = (8,6) , # define the figure size
                             color = 'red' , # define the color of the plot
                             grid = True ,  # show the gridlines 
                             fontsize = 10  # set up the font size
                              )


# insert the title, the name for x-axis, y-axis
plt.title('Average benefit per person ($/month) over time')
plt.xlabel('Year')
plt.ylabel('Monthly Amount, $')
plt.legend(['average monthly amount per person,$'])
plt.show()


# 2.2) The line chart to display the total benefits/(USD millions) over time 
df_public_assistance.plot( x = 'Fiscal Year' , # define the x-axis
                            y = 'Total Benefits(M)' , # define the y-axis
                            kind = 'line' , # define the plot type
                            figsize = (8,6) , # set up the figure size
                            color = 'purple' , # set up the color of the chart
                            grid = True , # display the gridlines
                            fontsize = 8 # set up the font size
                       )
# display the title of the plot, the x-axis and the y-axis title
plt.title('SNAP Public Assistance Total Benefits (millions,$), 1969-2019')   
plt.xlabel('Year')                  
plt.ylabel('Benefits, $ millions')
plt.legend(['SNAP total benefits'])
plt.show()

# -----------------------------------------------------------------------------------------------

# 3)   *** --- Multiple Lines Chart --- ***
# 3.1) Display two line charts on the same figure

x = df_public_assistance['Fiscal Year']
y1 = df_public_assistance['Average Benefit Per Person']
y2 = df_public_assistance['Total Benefits(M)']

fig = plt.figure(figsize=(6,10)) # define the size of the figure

# fig = plt.grid( b = True , which = 'major' , color = 'grey', linestyle = 'dashed')  

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

line1 = ax1.plot(x , y1 , 'tab:blue' ) # or color = 'blue'
line2 = ax2.plot(x , y2 , 'tab:purple')

# set up the gridlines parameters
ax1.grid( b = True , which = 'major' , color = 'grey', linestyle = 'dashed')
ax2.grid( b = True , which = 'major' , color = 'grey', linestyle = 'dashed' )

# display the titles for the subplots
ax1.title.set_text('Monthly Assitance per Person' )
ax2.title.set_text('Total Benefits' )

# display the labels for x-axis and y-axis
ax1.set( ylabel = 'Money Amount, $' )
ax2.set( xlabel = 'Fiscal Year' , ylabel = 'Money Amount, $ millions')

plt.subplots_adjust(hspace=0) # remove vertical gap between subplots
plt.show()

# -----------------------------------------------------------------------------------------------------------
 
# 4)  ***  ---  Create Vertical Bar Charts ---  ***
# 4.1) draw a vertical bar chart '% Change Avg Participation' over time
df_avg_change.plot.bar( x = 'Fiscal Year' , # define the x-axis
                         y = '% Change Avg Participation', # define the y-axis
                         color = ( df_avg_change['% Change Avg Participation'] > 0 ).map({True :'green' , False : 'red'}) ,
                         # dispaly the columns representing positive values in green color
                         # dsipaly the columns of negative values in red color
                         figsize = (17,5) , # set up the figure size
                         rot = 30 , # dispaly the numbers of x-axis at the rotation of 30 degrees
                         fontsize = 8 # set up the fontsize 
                        )

plt.grid( 'major', axis='y' , color = 'grey' , linestyle = '--' , linewidth = 0.5) # set up the gridline parameters
# display the title of the plot, the x-axis and the y-axis title
plt.title('Change of SNAP Recipients Number (% , compare to the previous year) over time')
plt.xlabel('Fiscal Year')
plt.ylabel('Change of Avg Participation,%')

# set up teh backgound color for the plot
ax = plt.gca()
ax.set_facecolor('lightgrey')

plt.show(block = True) # display the chart


# 4.2) draw a vertical bar chart '% Change Avg Benefit per Person'
df_avg_change.plot.bar( x = 'Fiscal Year' , # define the x-axis
                        y = '% Change Avg Benefit per Person', # define the y-axis 
                        color = ( df_avg_change['% Change Avg Benefit per Person'] > 0 ).map({ True : 'blue' , False : 'orange'}) ,
                        # dispaly the columns representing positive values in blue color
                        # dsipaly the columns of negative values in orange color
                        figsize = (17,5) , # set up the figure size
                        rot = 30 , # display the numbers of x-axis at the 30 degrees rotation
                        fontsize = 8 # set up the fontsize
                        )

plt.grid( 'minor', axis='y', color = 'grey' , linestyle = '--', linewidth = 0.5) # set up the gridline parameters
# display the title of the plot, the x-axis and the y-axis title
plt.title('Change of Average Benefit per Person (%, compare to the previous year) over time')
plt.xlabel('Fiscal Year')
plt.ylabel('Change of Avg Benefit per Person, %')

# set up the background color for the plot
ax = plt.gca()
ax.set_facecolor('lightyellow')

plt.show() # dispaly the chart


# 4.3) show two bar charts at the same figure
x = df_avg_change['Fiscal Year']
y1= df_avg_change['% Change Avg Participation']
y2 = df_avg_change['% Change Avg Benefit per Person']

fig = plt.figure(figsize=(20 , 7))
# fig.set_facecolor('lightyellow')  set up the color of the figure

ax = plt.subplot(111)
ax.bar( x , y1, width = 0.3 , align = 'center' ,  color = 'green' )
ax.bar( x-0.3, y2 , width = 0.3 , align = 'center' , color = 'blue' )
ax.set_facecolor('lightyellow')

ax.grid( 'minor', axis='y', color = 'grey' , linestyle = '--', linewidth = 0.5) # set up the gridline parameters

plt.show() # to display the chart


# 4.4) creat a stacked bar chart
w = 0.4 # declare the variable for the column width
# fig , ax = plt.subplot(111)

x = df_avg_change['Fiscal Year']
y1= df_avg_change['% Change Avg Participation']
y2 = df_avg_change['% Change Avg Benefit per Person']


plt.bar( x, y1 )
plt.bar( x , y2 , bottom = y1)

plt.xlabel('Fiscal Year')
plt.ylabel('Change, %')
plt.legend( (line1, line2), ('% Change Avg Participation','% Change Avg Benefit per Person'), loc=0)


plt.show()


#------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
'''
# 5)   ***  ---   Answer the Questions  ---   ****
# 5.1) What year there was the biggest monthly benefit per person?

# to answer the question the data frame 'df_public_assistance' will be sorted 
# by the column  'Average Benefit per Person' in descending way to have the largerst value at the top
# and indexed by the row position

print('********-------')
print(df_public_assistance.sort_values( by ='Average Benefit Per Person' , ascending = False))
print()
df_public_assistance_benefit_sorted = df_public_assistance.sort_values( by ='Average Benefit Per Person' , ascending = False , inplace = False) 
print()

print('df_public_assistance_sorted')
print(df_public_assistance_benefit_sorted)
print()

row_max_benefit_per_person = df_public_assistance_benefit_sorted.head(1)
print(row_max_benefit_per_person)
'''
# find the year of the biggest benefit per person
max_benefit_year = df_public_assistance.loc[df_public_assistance['Average Benefit Per Person'] == df_public_assistance['Average Benefit Per Person'].max()
print(max_benefit_year)
'''


print()
# or we can do this way: without sorting by the column 'Average Benefit Per Person' at the descending way
column = df_public_assistance['Average Benefit Per Person']
max_value_benefit = column.max()
print('max_value_benefit:  ' + str(max_value_benefit) )
print()
print('****')
print()

# or we can find it at the different way; returns the entire row
print(df_public_assistance[df_public_assistance['Average Benefit Per Person'] == df_public_assistance['Average Benefit Per Person'].max()  ] )

# to find the year for the biggest benefit per person
year_max_benefit = df_public_assistance_benefit_sorted.loc[0].at['Fiscal Year']
print('year_max_benefit :  ' +  str(year_max_benefit))

# to find the year of the biggest benefit per person without sorting the data frame
# the column 'Average Benefit Per Person' contains the max value of the benefits; use the function df['column_name'].max()
# the column 'Fiscal Year' contains the looked up value of the year
# max_year = df_public_assistance.loc['Fiscal Year'].at['Average']

print('---------------------------------------------------------------------------------------------------------------------')
print()
'''
# 6)   *** ---  Create Functions to Build Grapths  ---   ***

# 6.1) Create a function to build a single line chart
def build_line_chart( x_axis , y_axis , line_color ):
    df_public_assistance.plot( x =  x_axis, # define the  x-axis
                    y = y_axis , # define the y-axis
                    kind = 'line' , # define the plot type
                    figsize = (8,6) , # define the figure size
                    color = 'line_color' , # define the color of the plot
                    grid = True ,  # show the gridlines 
                    )


    #   insert the title, the name for x-axis, y-axis
    plt.title('Average benefit per person ($/month) over time')
    plt.xlabel('Year')
    plt.ylabel('Monthly Amount, $')
    plt.legend(['average monthly amount per person,$'])
    plt.show()

# call the function
build_line_chart( 'Fiscal Year' , 'Average Benefit Per Person' , 'red' )
'''

# Read the data file with unemployment rate
df_rates = pd.read_csv("E:\\_Python_Projects_Data\\Public_Assistance_Programs_US\\US_Unemployment_Rates_by_Years.csv" ,
                    usecols = ['Year',
                    'Unemployment Rate %' , 
                    'GDP Growth %' ,
                     'Inflation %']
                     )

print('** -----------------------------------')
print('Unemployemnt rates , GDP growth rate, Inflation rate')
print()
print(df_rates)
print()
#  *** -----   Create a chart to show the umemployment rate over time --- *** 
# Line chart
df_rates.plot( x = 'Year' , # define the  x-axis
                             y = 'Unemployment Rate %' , # define the y-axis
                             kind = 'line' , # define the plot type
                             figsize = (8,6) , # define the figure size
                             color = 'red' , # define the color of the plot
                             grid = True ,  # show the gridlines 
                             fontsize = 10  # set up the font size
                              )


# insert the title, the name for x-axis, y-axis
plt.title('Unemployment Rate (%) over time')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate, %')
plt.legend(['Unemployment Rate, %'])
plt.show()
print()
# Bar chart
df_rates.plot.bar( x = 'Year' , # define the x-axis
                        y = 'Unemployment Rate %', # define the y-axis 
                        color = 'red' ,
                        figsize = (15,6) , # set up the figure size
                        rot = 90 , # display the numbers of x-axis at the 30 degrees rotation
                        fontsize = 8 # set up the fontsize
                        )

plt.grid( 'minor', axis='y', color = 'grey' , linestyle = '--', linewidth = 0.5) # set up the gridline parameters
# display the title of the plot, the x-axis and the y-axis title
plt.title('Unemployment rate (%) over time')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate, %')

# set up the background color for the plot
ax = plt.gca()
ax.set_facecolor('lightyellow')

plt.show() # dispaly the chart

#  *** ----  Creat a chart to show inflation rate (%) over time  ---- ****
# Line chart
df_rates.plot( x = 'Year' , # define the  x-axis
                             y = 'Inflation %' , # define the y-axis
                             kind = 'line',
                             figsize = (8,6) , # define the figure size
                             color = 'blue' , # define the color of the plot
                             grid = True ,  # show the gridlines 
                             fontsize = 10  # set up the font size
                              )
# insert the title, the name for x-axis, y-axis
plt.title('Inflation,(%) over time')
plt.xlabel('Year')
plt.ylabel('Inflation rate, %')
plt.legend(['Inflation rate, %'])
plt.show()
print()

# *** ---- Create a chart to show the GDP growth over time
# Line chart
df_rates.plot( x = 'Year' , # define the  x-axis
                             y = 'GDP Growth %' , # define the y-axis
                             kind = 'line',
                             figsize = (8,6) , # define the figure size
                             color = 'green' , # define the color of the plot
                             grid = True ,  # show the gridlines 
                             fontsize = 10  # set up the font size
                              )
# insert the title, the name for x-axis, y-axis
plt.title('GDP growth ')
plt.xlabel('Year')
plt.ylabel('GDP growth,%')
plt.legend(['GDP Growth, %'])
plt.show()
print()

# Bar chart 
df_rates.plot.bar( x = 'Year' , # define the x-axis
                        y = 'GDP Growth %', # define the y-axis 
                        color = ( df_rates['GDP Growth %'] > 0 ).map({ True : 'green' , False : 'yellow'}) ,
                        # dispaly the columns representing positive values in green color
                        # dsipaly the columns of negative values in yellow color
                        figsize = (17,5) , # set up the figure size
                        rot = 30 , # display the numbers of x-axis at the 30 degrees rotation
                        fontsize = 8 # set up the fontsize
                        )

plt.grid( 'minor', axis='y', color = 'grey' , linestyle = '--', linewidth = 0.5) # set up the gridline parameters
# display the title of the plot, the x-axis and the y-axis title
plt.title('GDP Growth, %')
plt.ylabel('GDP growth,%')

# set up the background color for the plot
ax = plt.gca()
ax.set_facecolor('lightgrey')

plt.show() # dispaly the chart


# --------------------------------------------
# Show the unemployment rate, inflation, GDP growth on the same figure


# Display two line charts on the same figure

x = df_rates['Year']
y1 = df_rates['GDP Growth %']
y2 = df_rates['Inflation %']
y3 = df_rates['Unemployment Rate %']

plt.plot(x,y1, label = 'GDP Growth', color = 'green')
plt.plot(x,y2,label = 'Inflation %', color = 'orange')
plt.plot(x,y3,label = 'Unemployment rate,%' , color = 'red')
fig = plt.figure(figsize=(6,10))
plt.show()





