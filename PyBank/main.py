import csv
import os

# Get the path to the CSV file using a relative path
csv_file_path = os.path.join(os.path.dirname(__file__), 'Resources', 'budget_data.csv')

# Initialize variables to store data
total_months = 0
net_total = 0
changes = []
months = []

# Open the CSV file and read its contents
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row
    previous_profit_loss = 0
    
    for row in csv_reader:
        total_months += 1
        net_total += int(row[1])
        
        current_profit_loss = int(row[1])
        if total_months > 1:
            change = current_profit_loss - previous_profit_loss
            changes.append(change)
            months.append(row[0])
        
        previous_profit_loss = current_profit_loss

# Calculate the average change
average_change = round(sum(changes) / len(changes), 2)

# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Get the corresponding month for the greatest increase and decrease
increase_month = months[changes.index(greatest_increase)]
decrease_month = months[changes.index(greatest_decrease)]

# Specify the full path for the text file
output_file = os.path.join(os.path.dirname(__file__), 'PyBankAnalysis.txt')

# Save the results to the text file
with open(output_file, 'w') as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("----------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${net_total}\n")
    text_file.write(f"Average Change: ${average_change}\n")
    text_file.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
    text_file.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n")

print("Results saved to PyBankAnalysis.txt")