import os
import csv

date = []
money = []
total_months = 0
total_money = 0
grt_inc = 0
grt_dec = 0

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        date.append(row[0])
        money.append(row[1])
        total_months = total_months + 1
        total_money = total_money + int(row[1])
        if int(row[1]) > int(grt_inc):
            grt_inc = row[1]
            inc_month = str(row[0])
        if int(row[1]) < int(grt_dec):
            grt_dec = row[1]
            dec_month = str(row[0])
        
avg_change = total_money/total_months

output_file = "Financial Analysis.txt"

output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_money}\n"
    f"Average Revenue Change: ${avg_change}\n"
    f"Greatest Increase in Revenue: {inc_month} (${grt_inc})\n"
    f"Greatest Decrease in Revenue: {dec_month} (${grt_dec})\n")

with open(output_file, "w") as txt_file:
    txt_file.write(output)

print(output)