import os
import csv
from datetime import datetime

csvpath10 = 'C:/git/python_challenge/PyBank/Resources/budget_data.csv'  # Replace with the path to your data file

data_list=[] 
col1 = []
col2 = []
change=0
change_list=[]

with open(csvpath10) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
    data_list=list(csvreader)
    
    for row in data_list:
      
        col1.append(row[0])
        col2.append(int(row[1]))  # Convert the second column to integers

        Total=sum(col2)
        count=len(col1)
   

    change = [col2[i] - col2[i - 1] for i in range(1, len(col2))]
    change_list=change
    
    avg_change=(sum(change))/len(change)
                  
    
    High_profit=max(change_list)
    High_profit_month = col1[change_list.index(High_profit)+1]
        
    greatest_loss=min(change_list)
    greatest_loss_month=col1[change_list.index(greatest_loss)+1]
        
    print("Financial Analysis")
    print("------------------")
    print("Total Profit/Loss: ${:,.2f}".format(Total))
    print("Total Months: ", count)
    print("Average Profit/Loss :{:,.2f}".format(avg_change))
    print("Month with Greatest increase in Profits : {} (${:,})".format(High_profit_month, High_profit))
    print("Month with Greatest decrease : {} (${:,})".format(greatest_loss_month, greatest_loss))