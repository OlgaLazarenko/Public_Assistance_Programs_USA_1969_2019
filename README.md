# Public_Assistance_Programs_USA_1969_2019
             
 The project was build using the data source: [Kaggle.com](https://www.kaggle.com/jpmiller/publicassistance?select=SNAP_history_1969_2019.csv)
             SNAP_history_1969_2019
             
 The dataset provides data about public assistance probram SNAP (Supplement Nutrition Assistance Program) 
 the successor of the Food Stamps probram. The program provides food assistance 
 to low-income families in the form of a debit card.
 According to 2016 POS data about SNAP-eligible vendors the three most purchased types of food: meats, sweetened beverages, vegetables.
 
 The purpose of the project is to explore various aspects of US Public Assistance and create visualizations to show trends:
 -read the initial data
 -validate the data
 -write the validated data to the output file
 -write the invalid data to the errors file
 -if possible, correct the invalid data and append to the output file
 -creat calculated fields( Avg Participant % change, Avg Benefit per Person % change)
 
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
The validated/ correct data can be used for the following data manipulations and for visualization.
As well the calculated colunms will be created:
-Percent Change of Average Participation
-Percent Change of total Benefits 

