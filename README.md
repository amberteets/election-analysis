# Election Analysis

## Overview of Election Audit

In order to complete the audit of a recent election, the Colorado Board of Elections aims to verify the following information:
- The total number of votes cast in the election.
- A breakdown of the number of votes cast for each candidate, along with each candidate's percentage of the total votes.
- The winner of the election based on popular vote.
- A breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- The county with the highest voter turnout.

## Resources Used

- Data: election_results.csv
- Python (3.9.1)
- VS Code (1.52.1)

## Election Audit Results

- The analysis yielded a total vote count for the election of 369,711 votes cast.
- The number of votes and the percentage of total votes for each county in the precinct were as follows:
   - Jefferson: 10.5% (38,855 votes)
   - **Denver: 82.8% (306,055 votes)**
   - Arapahoe: 6.7% (24,801 votes)
- **Denver** county had the largest number of votes in the precinct (306,055)
- The number of votes and the percentage of total votes that each candidate received were as follows:
   - Charles Casper Stockham: 23.0% (85,213 votes)
   - **Diana DeGette: 73.8% (272,892 votes)**
   - Raymon Anthony Doane: 3.1% (11,606 votes)
- **Diana DeGette** was the winner of the election with 73.8% of the popular vote (272,892 votes). 

## Election Audit Summary

The script used to conduct this election audit is versatile and can be used (with minor modifications) for any election. The script is agnostic as to the number of candidates and the number of voting districts (e.g. counties, states, etc.), so it will work for elections of any scale, with any number of candidates who receive votes.
