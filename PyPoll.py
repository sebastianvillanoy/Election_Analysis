# Add our dependencies
import csv
import os

# Add the filename variable that references the path to election_results.csv
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:
     # To do: read and analyze data here:
     
     # Read the file object with the reader function.
    file_reader = csv.reader(election_data)   
    
    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)
     
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file: 
    # Write some data to the file.
    txt_file.write("Counties in the Election")
    txt_file.write("\n-----------------------")
     # Write three counties to the file.
    txt_file.write("\nArapahoe\nDenver\nJefferson")
