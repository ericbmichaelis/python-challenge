# First we'll import the os module
import os
import csv
# Read and Write csv files 
budget_import = os.path.join('Resources', 'budget_data.csv')
budget_output = os.path.join('Resources', 'budget_anaylsis.txt')

# Open and Read the file
with open (budget_import) as financial_data 
read_file = csvreader(financial_data)

# Defining what I am trying to do 
total_months = 0
total_amount = 0
avg_change = []
increased_profits = [0,999999999999999999]
decreased_profits = [-999999999999999,0]

#Define header 
header = next(read_file)

# Define variables 
first_row = next(read_file)
total_months = total_months + 1
total_amount = total_amount + int(first_row[1])
prev_net = int(first_row[1])

# Iterate through to find value for totals
for row in read_file:
    total_months = total_months + 1 
    total_amount = total_amount + int(row[1])

# Greatest Increase and Decrease 
    net_change = int(row[1]) - prev_net

if net_change > greatest_increase[1]:
    greatest_increase[0] = row[0]
    greatest_increase[1] = net_change

if net_change < greatest_decrease[1]:
    greatest_decrease[0] = row[0]
    greatest_decrease[1] = net_change

avg_change = sum(net_change) / len(net_change)

summary = (  
f'Financial Data Summary'
f'______________________'
f'"Total Months": {total_months}\n'
f'"Net Amount": {total_amount}\n'
f'"Avg Change for P/L": {avg_change}\n'
f'"Date with Greatest Profits": {increased_profits}\n'
f'"Date with Greatest Loss": {decreased_profits}\n'








)





















