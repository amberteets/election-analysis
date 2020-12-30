# Election Analysis
# What we need:
#   1. Total number of votes cast
#   2. Complete list of candidates who received votes
#   3. Percentage of votes each candidate won
#   4. Total number of votes each candidate won
#   5. Winner of the election based on popular vote.

# Challenge Analysis
#   1. Voter turnout for each county.
#   2. Percentage of votes for each county out of the total count.
#   3. County with the highest turnout.

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter, candidate options/votes variables.
total_votes = 0
candidate_options = []
candidate_votes = {}
# Initialize county options/votes variables.
counties = []
county_votes = {}

# Winning candidate, winning count, winning percentage tracker.
winning_candidate = ''
winning_count = 0
winning_percentage = 0
# Voter turnout tracker
highest_turnout_county = ''
highest_turnout = 0
highest_turnout_percentage = 0

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
        
        # CANDIDATE TRACKING
        # Assign candidate name to value in 3rd column of each row.
        candidate_name = row[2]

        # Add unique candidate names to candidate options variable.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add vote to that candidate's total count.
        candidate_votes[candidate_name] += 1

        # COUNTY TRACKING
        # Assign county to value in 2nd column of each row
        county = row[1]

        # Add unique counties to counties variable.
        if county not in counties:
            counties.append(county)

            # Begin tracking that county's votes.
            county_votes[county] = 0
        
        # Add votes to that county's total count.
        county_votes[county] += 1

    # Save results to text file.
    with open(file_to_save, "w") as txt_file:

        election_results = (
            f"\nElection Results\n"
            f"---------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"---------------------------\n"
        )
        print(election_results, end="")

        txt_file.write(election_results)

        # Get percentage of total votes for each candidate.
        candidate_intro = (
            f"Candidate Summary\n"
            f"---------------------------\n"
        )
        print(candidate_intro)
        txt_file.write(candidate_intro)
        # Loop through candidates.
        for candidate in candidate_votes:
            # Assign candidate's votes.
            votes = candidate_votes[candidate]
            # Calculate percentage.
            vote_percentage = (float(votes) / float(total_votes))*100

            # Print out each candidate's name, vote count, and percentage of
            # votes to the terminal.
            candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results, end="")
            # Print candidate results to text file.
            txt_file.write(candidate_results)

            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate

        # Winning Candidate Summary
        winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
        # Print winning candidate summary to terminal.
        print(winning_candidate_summary)
        # Print winning candidate summary to text file.
        txt_file.write(winning_candidate_summary)

        # Determine Voter Turnout by County
        county_intro = (
            f"County Summary\n"
            f"---------------------------\n"
        )
        print(county_intro)
        txt_file.write(county_intro)
        
        # Loop through counties
        for county in county_votes:
            # Assign county votes
            votes = county_votes[county]
            # Calculate % of votes from each county out of total vote count
            vote_percentage = (float(votes) / float(total_votes))*100

            # Print each county, its vote count, and % of total votes to terminal
            county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
            print(county_results)
            # Print county results to text file
            txt_file.write(county_results)

            if (votes > highest_turnout) and (vote_percentage > highest_turnout_percentage):
                highest_turnout = votes
                highest_turnout_percentage = vote_percentage
                highest_turnout_county = county

        # County Turnout Summary
        county_turnout_summary = (
            f"---------------------------\n"
            f"Largest County Turnout: {highest_turnout_county}\n"
            f"---------------------------\n"
        )
        print(county_turnout_summary)
        txt_file.write(county_turnout_summary)
