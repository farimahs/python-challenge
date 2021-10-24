import os
import csv

# Set path for file and open/read csv file
csv_path = os.path.join ('Resources','budget_data.csv')

months = []
dates = []
profit_losses = []

with open (csv_path) as csv_file:
    csv_reader = csv.reader (csv_file, delimiter =',')


    
# Splitting Months from the first column in the dataset
    for row in csv_reader:
        first_column = row[0].split('-')
        dates.append(first_column)
        second_column = row[1]
        profit_losses.append(second_column)

# Removing the column headers 'Date' and 'Profit/Losses' from the lists        
    dates.pop(0)
    profit_losses.pop(0)

# Changing data type from string to integer
    profit_losses_integer = [int(x) for x in profit_losses]
    
# Creating a list of all months in the dataset    
    for date in dates:
        months.append(date[0])

# Calculating the changes in "Profit/Losses" over the entire period
    changes = []
    for i in range(len(profit_losses_integer)-1):
        difference = profit_losses_integer[i+1]-profit_losses_integer[i]
        changes.append(difference)

    max = changes[0]
    for i in range (len(changes)-1):
        if changes[i+1] > max:
            max = changes[i+1]
# max date is pullig from 'dates' list and its indees are one more than the changes list, because changes list has 85 rows instead of 86 since we have subtracted two values
            max_date_month = dates[i+2][0]
            max_date_year = int(dates[i+2][1]) + 2000

    min = changes[0]
    for i in range (len(changes)-1):
        if changes[i+1] < min:
            min = changes[i+1]
# min date is pullig from 'dates' list and its indees are one more than the changes list, because changes list has 85 rows instead of 86 since we have subtracted two values
            min_date_month = dates[i+2][0]
            min_date_year = int(dates[i+2][1]) + 2000
    
    
    print("Financial Analysis")
    print("--------------------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total: ${sum(profit_losses_integer)}")
    print(f"Average Change: ${round(sum(changes)/len(changes),2)}")
    print(f"Greatest Increase in Profits: {max_date_month}-{max_date_year} $({max})")
    print(f"Greatest Decrease in Profits: {min_date_month}-{min_date_year} $({min})")

# Exporting the analysis results into a text file
    analysis = open ('analysis.txt', 'w')

    analysis.write("Financial Analysis" + "\n")
    analysis.write("--------------------------------------" + "\n")
    analysis.write(f"Total Months: {len(months)}" + "\n")
    analysis.write(f"Total: ${sum(profit_losses_integer)}" + "\n")
    analysis.write(f"Average Change: ${round(sum(changes)/len(changes),2)}" + "\n")
    analysis.write(f"Greatest Increase in Profits: {max_date_month}-{max_date_year}  $({max})" + "\n")
    analysis.write(f"Greatest Decrease in Profits: {min_date_month}-{min_date_year}  $({min})" + "\n")


    analysis.close()


    
        



