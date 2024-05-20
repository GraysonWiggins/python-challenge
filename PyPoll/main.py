import csv
import os

# Get the path to the CSV file using a relative path
csv_file_path = os.path.join(os.path.dirname(__file__), 'Resources', 'election_data.csv')

# Initialize variables to store data
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Open the CSV file and read its contents
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row
    
    for row in csv_reader:
        total_votes += 1
        candidate_name = row[2]
        
        # Count the votes for each candidate
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Calculate the percentage of votes each candidate won
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidates[candidate] = (percentage, votes)
    
    # Determine the winner based on the popular vote
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, (percentage, votes) in candidates.items():
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save the results to a text file
output_file = os.path.join(os.path.dirname(__file__), 'PyPollAnalysis.txt')

with open(output_file, 'w') as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-------------------------\n")
    for candidate, (percentage, votes) in candidates.items():
        text_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("-------------------------\n")

print("Results saved to PyPollAnalysis.txt")