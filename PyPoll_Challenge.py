# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("..", "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = ["Arapahoe", "Denver", "Jefferson"]
voting_data = [{"county":"Arapahoe", "candidate_votes": 422829},
                {"county":"Denver", "votes": 463353},
                {"county":"Jefferson", "votes": 432438}]
for county_dict in voting_data:
    print(county_dict)

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
county_dict.items()

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    headers = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        county_name = row[1]

            # 4b: Add the existing county to the list of counties.
        if county_name not in county_options:

            # 4c: Begin tracking the county's vote count.
            county_votes[candidate_name] = 0

        # 5: Add a vote to that county's vote count.
            county_votes[candidate_name] += 1

#Determine winning vote count and candidate
#Determine if votes are greater than winning_count.
if(votes > winning_count) and (vote_percentage > winning_percentage):
    #If true set winning count = votes and winning_percent = vote_percentage.
    winning_count = votes
    winning_candidate = candidate_name
    winning_percentage = vote_percentage

#Determine the percentage of votes for each candidate by looping through the counts
#Iterate thru the candidate list.
NL = '\n'
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,}){NL}")

    print(candidate_results)

#Print
NL = '\n'
winning_candidate_summary = (
    f"-------------------------{NL}"
    f"Winner: {winning_candidate}{NL}"
    f"Winning Vote Count: {winning_count:,}{NL}"
    f"Winning Percentage: {winning_percentage:.1f}%{NL}"
    f"-------------------------{NL}")

print(winning_candidate_summary)

# Save the results to our text file.
with open(file_to_save, "a") as txt_file:

    # Print the final vote count (to terminal)
    NL = '\n'
    election_results = (
        f"{NL}Election Results{NL}"
        f"-------------------------{NL}"
        f"Total Votes: {total_votes:,}{NL}"
        f"-------------------------{NL}")
        f"County Votes: {county_votes;,}{NL}")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    NL = '\n'
    for county_dict in election_results
        # 6b: Retrieve the county vote count.
        votes = county_votes[candidate_name]
        # 6c: Calculate the percentage of votes for the county.
        county_percentage = float(votes) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,}){NL}")

        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(election_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
             winning_count = votes
             winning_county = county_name
             winning_percentage = vote_percentage

    # 7: Print the county with the largest turnout to the terminal.
    NL = '\n'
    winning_county_summary = (
        f"-------------------------{NL}"
        f"Winner: {winning_county}{NL}"
        f"Winning Vote Count: {winning_count:,}{NL}"
        f"Winning Percentage: {winning_percentage:.1f}%{NL}"
        f"-------------------------{NL}")

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

    # Save the final candidate vote count to the text file.
    NL = '\n'
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,}){NL}")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    NL = '\n'
    winning_candidate_summary = (
        f"-------------------------{NL}"
        f"Winner: {winning_candidate}{NL}"
        f"Winning Vote Count: {winning_count:,}{NL}"
        f"Winning Percentage: {winning_percentage:.1f}%{NL}"
        f"-------------------------{NL}")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
