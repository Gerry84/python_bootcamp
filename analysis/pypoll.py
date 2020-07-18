# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("C:\\Users\\sjcgkern\\Desktop\\Gerry\\Knowledge\\Data Analytics Bootcamp\\MyRepo\\Python Module", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("C:\python", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
#    print(headers)
    # Print each row in the CSV file.
    for row in file_reader:
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 1
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        total_votes += 1


#print('Total Votes: ',total_votes)
#print('Candidate Options: ',candidate_options)
#print('Votes per Candidate: ',candidate_votes)

#for key, value in candidate_votes.items():
#    print(key, value)
#    print(f"{key} had {value/total_votes*100:.2f}% of votes")

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    print(f"\n{candidate_name}: {votes/total_votes*100:.1f}% ({votes:,})\n ")
    if votes > winning_count:
        winning_count = votes
        winning_candidate = candidate_name

print(f"---------------------------------------------------\n"
      f"Winner: {winning_candidate}\n"
      f"Winning Vote Count: {winning_count:,}\n"
      f"Winning Percentage: {winning_count/total_votes *100:.2f}%\n"
      f"---------------------------------------------------")
