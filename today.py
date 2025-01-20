from datetime import datetime

# Get today's date
today = datetime.now()
year = today.year

# Calculate the start and end of the year
start_of_year = datetime(year, 1, 1)
end_of_year = datetime(year, 12, 31)

# Days elapsed and remaining
days_elapsed = (today - start_of_year).days + 1
days_remaining = (end_of_year - today).days

# Create a motivational message
def motivational_message():
    if days_elapsed <= 30:
        return "The year has just started—set the tone for success!"
    elif days_remaining < 30:
        return "The year is wrapping up—make every day count!"
    else:
        return "You're in the middle of the journey—stay consistent and focused!"

# Print the results
print(f"Today's Date: {today.strftime('%B %d, %Y')}")
print(f"Days Elapsed: {days_elapsed}")
print(f"Days Remaining: {days_remaining}")
print("\nMotivational Message:")
print(motivational_message())
