import os
import csv

# Specify the file to read from
Electioncsvpath = os.path.join(".", "Resources", "election_data.csv")

# Define the function and have it accept the 'election_data' as its sole parameter
def print_winner(election_data):
    # For readability, it can help to assign your values to variables with descriptive names
    # CSV headers: Ballot ID, Country, Candidate
    Ballot_ID = str(election_data[0])
    Country = str(election_data[1])
    Candidate = str(election_data[2])
    
    return Ballot_ID, Country, Candidate

# Open the file within the 'with' statement
with open(Electioncsvpath) as Electioncsvfile:
    csvreader = csv.reader(Electioncsvfile, delimiter=',')
    
    # Skip the header row
    next(csvreader)

    # Initialise a counter for total months, total profit/losses, Previous profit/loses, and change in profits
    total_Votes = 0
    candidate_votes ={}
    

    # Iterate through each row in the CSV file
    for row in csvreader:
        # Increment the total votes counter for each row
        total_Votes += 1
        
# Extract the candidate name from the current row
        candidate_name = row[2]

# Update the candidate's vote count in the dictionary
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

# Calculate and print the required results            
result_text = f'Election Results\n'
result_text += f'-----------------------\n'
result_text += f'Total Votes: {total_Votes}\n'
result_text += f'-----------------------\n'

# The percentage of votes each candidate won
# Iterate through the candidate_votes dictionary
for candidate, votes in candidate_votes.items():
    # Calculate the percentage of votes each candidate won
    percentage = (votes / total_Votes) * 100

# Print and append to the result_text and percentage values in 3 decimal places
    result_text += f'{candidate}: {percentage:.3f}% ({votes})\n'


# The winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)       

# Display and export the total number of months and net total amount
result_text += f'-------------------------\n'
result_text += f'Winner: {winner}\n'
result_text += f'-------------------------\n'

print(result_text)

# Export the result to a text file
output_file_path = os.path.join(".", "Analysis", "result.txt")
with open(output_file_path, 'w') as output_file:
    output_file.write(result_text)
