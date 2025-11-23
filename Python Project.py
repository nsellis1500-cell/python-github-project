"""
Savings Goal Tracker
Author: Noah Ellis

This simple Python program helps a user estimate
how long it will take to reach a savings goal
based on their current savings and weekly contribution.
"""
# Task 1: Welcome message
print("Welcome to the Savings Goal Tracker!")


# Task 2: Ask the user for input
# Collect:
# - their name (optional)
# - their total savings goal
# - how much they have saved so far
# - how much they plan to save each week

name = input("What is your name? (Press Enter to skip) ")

goal_input = input("What is your total savings goal in dollars? ")
current_input = input("How much have you saved so far in dollars? ")
weekly_input = input("How much do you plan to save each week in dollars? ")


# Task 3 pt1: Convert input and perform a calculation 
# Use try/except so the program doesn't crash if the user
# types something that is not a number.

try:
    savings_goal = float(goal_input)
    current_savings = float(current_input)
    weekly_contribution = float(weekly_input)
except ValueError:
    print("\nPlease enter valid numeric values for money (e.g., 100 or 250.50).")
    exit()


# Extra validation to keep results meaningful
if savings_goal <= 0:
    print("\nYour savings goal must be greater than 0.")
    exit()

if current_savings < 0:
    print("\nCurrent savings cannot be negative.")
    exit()

if weekly_contribution <= 0:
    print("\nWeekly contribution must be greater than 0 to make progress.")
    exit()


# Task 3 pt2: Perform calculations

# How much is left to reach the goal
remaining_amount = savings_goal - current_savings

# If the user already met or passed their goal:
if remaining_amount <= 0:
    # Task 4: Display a clear result
    if name.strip():
        print(f"\nGreat job, {name}! You have already reached your savings goal!")
    else:
        print("\nGreat job! You have already reached your savings goal!")
    exit()

# Calculate weeks needed and percent toward goal
weeks_needed = remaining_amount / weekly_contribution
percent_complete = (current_savings / savings_goal) * 100


# Task 4: Display the result clearly

print("\n---------------- Savings Summary ----------------")

if name.strip():
    print(f"Hi, {name}!")
else:
    print("Hi there!")

print(f"Your total savings goal: ${savings_goal:,.2f}")
print(f"Current savings:        ${current_savings:,.2f}")
print(f"Amount remaining:       ${remaining_amount:,.2f}")
print(f"Planned weekly savings: ${weekly_contribution:,.2f}")

print(f"\nYou are currently {percent_complete:.1f}% of the way to your goal.")
print(f"If you keep saving ${weekly_contribution:,.2f} per week,")
print(f"you will reach your goal in approximately {weeks_needed:.1f} weeks.")

print("\nKeep going — every dollar moves you closer to your goal!")
