import os
import csv
import statistics
import pandas as pd
from pathlib import Path


election_budget_csv = os.path.join('..','PyPoll', 'Resources', 'election_data.csv')

# Import the comic_books_expanded.csv file as a DataFrame
election_budget_df = pd.read_csv(election_budget_csv)

candidate_list = election_budget_df["Candidate"].value_counts(sort=False)
ballot_list = election_budget_df["Candidate"].unique()
combinded_list = list(zip(ballot_list, candidate_list))

Total_votes =len(election_budget_df)


print("Election Results")

print("----------------\n")

print(f"Total Votes {Total_votes}")

print("----------------\n")

for row in combinded_list:
    percent = row[1]/Total_votes * 100
    percent = round(percent, 3)
    print(f"{row[0]}: {percent}% ({row[1]})")

print("----------------\n")

most_votes = 0
for row in combinded_list:
    if row[1]> most_votes:
        most_votes = row[1]

for row in combinded_list:
    if row[1] == most_votes:
        print(f"Winner: {row[0]}")

print("----------------")


with open("Analysis/Results.txt", 'w') as f:
    f.write("Election Results\n")

    f.write("----------------\n")

    f.write(f"Total Votes {Total_votes}\n")

    f.write("----------------\n")
    for row in combinded_list:
        percent = row[1]/Total_votes * 100
        percent = round(percent, 3)
        f.write(f"{row[0]}: {percent}% ({row[1]})\n")
    f.write("----------------\n")
    for row in combinded_list:
        if row[1] == most_votes:
            f.write(f"Winner: {row[0]}\n")
    f.write("----------------\n")