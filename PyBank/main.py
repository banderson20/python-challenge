import os
import csv
import statistics
import pandas as pd
from pathlib import Path

csvpath = os.path.join('..','Pybank', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    
    blank = []
    blank_date = []

    for row in csvreader:
        blank.append(int(row[1]))
        blank_date.append(row[0])


change_list = []

for row, current_row in enumerate(blank):
    if row < len(blank) - 1:
        next_value = blank[row + 1]
        change_list.append(int(next_value) - int(current_row))


avg_value = round(sum(change_list)/len(change_list), 2)
max_value = max(change_list)
min_value = min(change_list)

change_list.insert(0, "NaN")

combined_list = list(zip(change_list, blank_date))
for row in combined_list:
    if row[0] == max_value:
        max_date = row[1]

for row in combined_list:
    if row[0] == min_value:
        min_date = row[1]


print("Financial Analysis\n")

print("----------------\n")

print(f"Total Months: {len(blank)}\n")
print(f"Total: ${sum(blank)}\n")
print(f"Average Change: ${avg_value}\n")
print(f"Greatest Increase in Profits: {max_date} (${max_value})\n")
print(f"Greatest Decrease in Profits: {min_date} (${min_value})\n")

with open("Analysis/Results.txt", 'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------\n")
    f.write(f"Total Months: {len(blank)}\n")
    f.write(f"Total: ${sum(blank)}\n")
    f.write(f"Average Change: ${avg_value}\n")
    f.write(f"Greatest Increase in Profits: {max_date} (${max_value})\n")
    f.write(f"Greatest Decrease in Profits: {min_date} (${min_value})\n")




