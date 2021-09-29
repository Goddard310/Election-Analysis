# # The Data We Need to Retrieve
# # 1. Total number of votes cast
# # 2. List of candidates who received votes
# # 3. Percentage of votes each candidate received
# # 4. Total number of votes each candidate
# # 5. Winner of election based on popular vote
# import datetime
# now = datetime.datetime.now()
# print("The time is", now)
# import csv
# dir(csv)
# # Assign a variable for the file to load and the path.
# file_to_load = '/Users/jasongoddard/Desktop/Analytics_Projects/Election-Analysis/Resources/election_results.csv'
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#      # To do: perform analysis.
#      print(election_data)

# # To do: perform analysis.

# # Close the file.
# election_data.close()

# import csv
# import os
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write three counties to the file.
#      txt_file.write("Arapahoe")
#      txt_file.write("Denver")
#      txt_file.write("Jefferson")

#      # Write three counties to the file.
#      txt_file.write("Arapahoe, Denver, Jefferson")

# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Open the election results and read the file.
# with open(file_to_load) as election_data:

# # Read the file object with the reader function.
#     file_reader = csv.reader(election_data)
#  # Print each row in the CSV file.
#     for row in file_reader:
#         print(row)

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

