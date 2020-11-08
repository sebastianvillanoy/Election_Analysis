# Add our dependencies
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

    # Loop each row in the csv and colelct info
    for row in file_reader:
        # count total votes 
        total_votes += 1 
        # collect candidate names into candidate_options list and candidate_votes dictionary
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]= 0
        candidate_votes[candidate_name] += 1

    #Print collected totals
    #print(total_votes)
    #print(candidate_options)
    #print(candidate_votes)
    
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file: 
    # Write some data to the file.
    txt_file.write("Counties in the Election")
    txt_file.write("\n-----------------------")
     # Write three counties to the file.
    txt_file.write("\nArapahoe\nDenver\nJefferson")
