# Election Audit

## Project Overview

The purpose of this election analysis is to audit the congressional election for the election commission. This audit was completed using python to analysis a .csv file of all ballots cast in the election. The code used in the audit then created outputs of the overall all results, winning candidate, and county with the highest turnout. This project will also make suggestions for how this process could be easily modified to audit any election results.

## Election Audit Results

### Vote Totals

- Total Votes:
  - 369,711
- County Votes and Percentage of Total Votes:
  - Jefferson: 38,855 (10.5%)
  - Denver: 306,055 (82.8%)
  - Arapahoe: 24,801 (6.7%)
- Candidate Votes and Percentage of Total Votes:
  - Charles Casper Stockham: 85,213 (23.0%)
  - Diana DeGette: 272,892 (73.8%)
  - Raymon Anthony Doane: 11,606 (3.1%)

### Results

- Largest Turnout: Denver County
- Winner: Diana DeGette
  - Winning Vote Percentage: 73.8%
  - Winning Vote Count: 272,892



## Election Audit Summary

The code written for this project is very versatile. With only some minor modifications, the same code could be used for any election. By simply changing the lists and dictionaries (and their corresponding references) from capturing counties to capturing ballot measures or referenda, you could use this same code to for any local or state-wide ballot initiative. The code to be changed is shown below:

```python
# Candidate Options and candidate votes.
# 1: Create a county list and county votes dictionary.
candidate_options = []
county_list = []
candidate_votes = {}
county_votes = {}


# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0
```

You could also use the same code to capture the state results for presidential elections. With some minor modifications, you could have the code provide county-level results (votes and winner per county) as well as summarizing the statewide results. The for loop below could easily be modified to capture the county-specific results for the presidential election:

```python
 # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        county_total_votes = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        county_votes_percentage = float(county_total_votes) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (
            f'{county_name}: {county_votes_percentage: .1f}% ({county_total_votes:,})\n')
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if(county_total_votes > county_voters):
            largest_county = county_name
            county_voters = county_total_votes


    # 7: Print the county with the largest turnout to the terminal.
    largest_turnout = (
        f"-------------------------\n"
        f"Largest Turnout: {largest_county}\n"
        f"-------------------------\n")
    print(largest_turnout)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_turnout)
```

Overall, this code is conducive to auditing any election, given the proper modifications. It is a very versatile and effective means of auditing elections and should be considered as a permanent tool for the Election Commission.

