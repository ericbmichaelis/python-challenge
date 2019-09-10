# Import csv
import csv
import os

# Files to Load and Output
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Analysis", "election_analysis.txt")

#Create varibles to loop through 
total_votes = 0

#List for Options and Dictionary for Votes
candidate_options = []
candidate_votes = {}

#Dependant Variables 
winning_candidate = ""
winning_votes = 0 

#Read File 
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

# Iterate through file 

for row in reader: 
    total_votes = total_votes + 1 
    candidate_name = row[2]
    candidate_votes[candidate_name] = 0
    candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1


election_results = (
        f"\nelection Results\n"
        f"Total Votes: {total_votes}\n"
    print(election_results, end="")







