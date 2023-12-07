import os
import csv

# Specify the file to read from
Budgetcsvpath = os.path.join(".", "Resources", "budget_data.csv")

# Define the function and have it accept the 'budget_data' as its sole parameter
def print_profit(budget_data):
    # For readability, it can help to assign your values to variables with descriptive names
    # CSV headers: date, Profit/Losses
    Date = str(budget_data[0])
    Profit_losses = int(budget_data[1])
    
    return Date, Profit_losses

# Open the file within the 'with' statement
with open(Budgetcsvpath) as Budgetcsvfile:
    csvreader = csv.reader(Budgetcsvfile, delimiter=',')
    
    # Skip the header row
    next(csvreader)

    # Initialise a counter for total months, total profit/losses, Previous profit/loses, and change in profits
    total_months = 0
    total_profit_losses = 0
    previous_profit_loss = 0
    changes_in_profits = []
    months = []

    # Iterate through each row in the CSV file
    for row in csvreader:
        # Increment the total months counter for each row
        total_months += 1
        
        # Call the function to get the Date and Profit_losses
        date, profit_losses = print_profit(row)

        # Add profit/loss to the total
        total_profit_losses += profit_losses

        # Calculate changes in profits
        if previous_profit_loss != 0:
            change = profit_losses - previous_profit_loss
            changes_in_profits.append(change)
            months.append(date)

        # Update previous profit/loss for the next iteration
        previous_profit_loss = profit_losses

# Calculate the average change
average_change = sum(changes_in_profits) / len(changes_in_profits)

# Find the greatest increase and decrease
greatest_increase = max(zip(changes_in_profits, months))
greatest_decrease = min(zip(changes_in_profits, months))

# Display and export the total number of months and net total amount
result_text = f'Financial Analysis\n'
result_text += f'-----------------------\n'
result_text += f'Total Months: {total_months}\n'
result_text += f'Total: $ {total_profit_losses}\n'
result_text += f'Average Change: $ {average_change:.2f}\n'
result_text += f'Greatest Increase in Profits: {greatest_increase[1]} (${greatest_increase[0]})\n'
result_text += f'Greatest Decrease in Profits: {greatest_decrease[1]} (${greatest_decrease[0]})\n'

print(result_text)

# Export the result to a text file
output_file_path = os.path.join(".", "Analysis", "result.txt")
with open(output_file_path, 'w') as output_file:
    output_file.write(result_text)




