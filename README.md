# Public_Assistance_Programs_USA_1969_2019
             
 The project was build using the data source: [www.Kaggle.com](https://www.kaggle.com/jpmiller/publicassistance?select=SNAP_history_1969_2019.csv)
             SNAP_history_1969_2019.

 Additional data about the unemployment rate: [www.thebalance.com]https://www.thebalance.com/unemployment-rate-by-year-3305506]
             
 The dataset provides the data about public assistance probram SNAP (Supplement Nutrition Assistance Program) 
 the successor of the Food Stamps probram. The program provides food assistance 
 to low-income families in the form of a debit card.
 According to 2016 POS data about SNAP-eligible vendors the three most purchased types of food: meats, sweetened beverages, vegetables.
 
 The purpose of the project is to explore the various aspects of US Public Assistance:
 - [x] read the initial data
 - [x] validate the data
 - [x] write the validated data to the output file
 - [x] write the invalid data to the errors file
 - [x] if it's possible, correct the invalid data and append to the output file
 - [x] create calculated fields( Avg Participant % change, Avg Benefit per Person % change)

 - [x] create visualizations to show the trends
 - [x] create a plot/(line chart) to show the Average Participation/(thousands of people) over the time period 1969-2019
 - [x] create a plot to show the Average Benefit Per Person/monthly $ amount per person over the time period 1969-2019
 - [x] create a plot to show the Total Benefits over the time 
 - [x] display the line charts Average Benefit Per Person and Total Benefits over time as the subplots on the same figure

 - [x] create the bar chart ' % Change Avg Participation' over time to show the change at the number of beneficiaries over time
 - [x] create the bar chart '% Change Avg Benefit per Person' over time to show  the avg monthly assistance per person over time
 - [] show two bar charts at the same figure ( '% Change Avg Particiapation' and '% Change Avg Benefit per Person' over time)
 - [x] create grouped bar charts plot
 - [] create stacked bar charts plot

 - [] create a function to build a line chart
 - [] create a function to build multiple line charts at the same figure
 - [] create a function to build a bar line chart
 - [] create a function to show multiple bar charts at the same figure

 - [] find the data about the inflation for 1969-2019, the cost of living
 - [] answer the question : What year there was the biggest monthly benefit per person?
 - [] answer the question : What year there was the biggest SNAP total assistance?
 - [] answer the question : What year there was the max number of participants/recepients?
"
 
 ### Specification: the dataset contains 6 fields/ columns
                - Fiscal Year (should be between 1969 and 2019 including, fiscal year runs from October to October)
                - Average Participants (thousands of people)
                - Average Benefits (average montly dollars per person)
                - Total Benefits (USD millions)
                - Other Costs (USD millions, including the Federal share of State,
                                admininstrative expenses, Nutrition Education, employmnet and training)
                - Total Costs(USD millions)
                
  
 
 
### The following Python modules are used : configparser, csv, os 
The file with initial data will be opened and the data will be read with the configuration file (Data_Files_SNAP_history.ini).

Some values in rows have the double quotes because these values contain the comma, thus the reader will be used to read the initial data.

The function `validate_fiscal_year(fis_year)` is created to  validate the values in the column 'Fiscal Year' 
(should be a positive integer, from 1969 to 2019, inculding)

The function `validate_expense(cost)` is created to validate values at the following columns:
Average Participantion,
Average Benefit Per Person,
Total Benefits(M),
Other Costs,
Total Costs(M).

### The output of the code is the files: 
```
'output file' with the validated/ correct data
'errors file' with invalid data
'new_output file' containing new columns with calculated values
```
The invalid data will be pushed to the 'errors file' and will be looked at more closely, if it is possible it will be corrected
and will be written to the output file with valid data.

The validated/ correct data can be used for the following data manipulations and for visualization.
As well the calculated colunms will be created:
- Percent Change of Average Participation 
- Percent Change of Average Benefit per Person

The formula for the calculated columns:
`Percent Change = (The current year value - the previous year value)*100/(The previous year value)`.

The new_output file will contain the columns:
- Fiscal Year (the values will be transferred from the output file)
- Average Participants (the values from the output file)
- % Change Avg Participants (calculated values)
- Average Benefit per Person (the values from the output file)
- % Change Avg Benefit per Person (calculated values)

In order to make necessary calculations two dictionaries will be created: 
- Benefit_dict{key(fiscal year):value(average benefit per person)}
- Particip_dict{key(fiscal year):value(avg participatins)}

The values for the formula will be obtained by searching the dictionaries for the required year(key) using `dict.get(key`) function.
As the result of the code we have two files `output_file` and `new_output_file`, 
the both contain the validated data wich can be used for visialization; the files have the common column 'Fiscal Year'.
              
           

