import pandas as pd
import csv

#import the csv file
Bank_Data = pd.read_csv('Budget_Data_1.csv')

Num_Months = Bank_Data['Date'].nunique()

Total_Revenue = sum(Bank_Data['Revenue'])

Average_Revenue = Total_Revenue/Num_Months
Average_Revenue = Average_Revenue.round(2)

Increase_Date = Bank_Data[Bank_Data['Revenue'] == Bank_Data['Revenue'].max()]['Date']
Decrease_Date = Bank_Data[Bank_Data['Revenue'] == Bank_Data['Revenue'].max()]['Date']
Increase_Date = Increase_Date.to_string(header=None, index=None)
Decrease_Date = Decrease_Date.to_string(header=None, index=None)

Max = Bank_Data['Revenue'].max()
Min = Bank_Data['Revenue'].min()

print(Num_Months)
print(Total_Revenue)
print(Average_Revenue)
print(Increase_Date)
print(Decrease_Date)
print(Max)

file = open('Revenue_Results.txt','w')
file.write('Financial Analysis\n')
file.write('-----------------\n')
file.write("Total Months: " + str(Num_Months)+"\n")
file.write("Total Revenue: $" + str(Total_Revenue)+"\n")
file.write("Average Revenue Change: $" + str(Average_Revenue)+"\n")
file.write("Greatest Increase in Revenue: " + Increase_Date + " ($" + str(Max)+")\n")
file.write("Greatest Decrease in Revenue: " + Decrease_Date + " ($" + str(Min)+")\n")