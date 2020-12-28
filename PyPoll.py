# Election Analysis
# What we need:
#   1. Total number of votes cast
#   2. Complete list of candidates who received votes
#   3. Percentage of votes each candidate won
#   4. Total number of votes each candidate won
#   5. Winner of the election based on popular vote.

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter, candidate options variables.
total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning candidate, winning count tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:


    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in csv file.
    for row in file_reader:
        # Add to the total vote count:
        total_votes += 1

        # Assign candidate name to value in 3rd column of each row.
        candidate_name = row[2]

        # Add unique candidate names to candidate options variable.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add vote to that candidate's total count.
        candidate_votes[candidate_name] += 1

    # Get percentage of total votes for each candidate.
    # Loop through candidates.
    for candidate in candidate_votes:
        # Assign candidate's votes.
        votes = candidate_votes[candidate]
        # Calculate percentage.
        vote_percentage = float(votes) / float(total_votes)

        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        print(f"{candidate}: {vote_percentage*100:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

    winning_candidate_summary = (
    f"---------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------------\n")
    print(winning_candidate_summary)

