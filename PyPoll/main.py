import os
import csv

candidates = []
candidate_votes = {}
total_votes = 0

csvpath = os.path.join('poll_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        total_votes = total_votes + 1
        cand_name = row[2]
        if cand_name not in candidates:
            candidates.append(cand_name)
            candidate_votes[cand_name] = 0
            candidate_votes[cand_name] = candidate_votes[cand_name] + 1
        else:
            candidate_votes[cand_name] = candidate_votes[cand_name] + 1

winning_votes = 0

output_file = "Election Results.txt"

output = (
    f"\nElection Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n")

with open(output_file, "w") as txt_file:
    txt_file.write(output)
    print(output)
    for cand_name in candidates:
        votes = candidate_votes[cand_name]
        vote_percent = (votes /total_votes) * 100
        if (votes > winning_votes):
            winning_votes = votes
            winner = cand_name
        output_2 = f"{cand_name}: {vote_percent:.3f}% ({votes})\n" 
        txt_file.write(output_2)
        print(output_2)
    output_final = (
        f"----------------------------\n"
        f"The winner is {winner}\n"
        f"with {winning_votes} votes\n")
    txt_file.write(output_final)
    print(output_final)