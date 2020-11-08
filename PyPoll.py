# Add dependencies
import csv
import os

# Add the filename variable that references the path to election_results.csv
file_to_load = os.path.join("Resources", "election_results.csv")

# Initialize variables, lists and dictionaries.
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)   
    
    # Extract the header row and store into a list
    headers = next(file_reader)

    # Loop through each row in the csv file and collect info
    for row in file_reader:
        # count total votes 
        total_votes += 1 
        # collect candidate names into candidate_options list and update candidate_votes dictionary
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]= 0
        candidate_votes[candidate_name] += 1

# Create a filename variable to a direct or indirect path to the election_analysis file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election_analysis file and write collected information into it.
with open(file_to_save, "w") as txt_file:

    # Store the election results into a variable
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    
    # Write the election results into the election_analysis file
    print(election_results, end="")
    txt_file.write(election_results)

    # Loop through the dictionary of candidate_votes for the keys and values
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Store the candidate results in a variable 
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Write the candidate results into the election_analysis file
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine the winning count, percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    
    # store the winning candidate summary in a variable
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    
    # Write the winning candidate summary into the election_analysis file
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)