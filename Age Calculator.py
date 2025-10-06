# Calculate the complete age of a person in years, months and days

import datetime

def calculate_full_age(born):
    """
    Calculates the complete age (years, months, and days) between the
    date of birth (born) and today.
    """
    today = datetime.date.today()

    # 1. Calculate complete years
    # Unga original logic correct-a dhan irundhadhu for years:
    # Subtract 1 from year if today's birthday hasn't passed yet.
    years = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    # 2. Calculate months
    if today.month < born.month:
        # If today's month is before birth month (e.g., Today is Jan, Born is June)
        # We take months from the previous year.
        months = 12 - born.month + today.month
    elif today.month == born.month:
        # If months are the same, check days
        if today.day < born.day:
            # If today's day is before birth day (e.g., Today 1st, Born 15th)
            months = 11 # The full month hasn't completed yet, so it's 11 months from last year.
        else:
            months = 0
    else: # today.month > born.month
        # If today's month is after birth month (e.g., Today is June, Born is Jan)
        months = today.month - born.month
    
    # Adutha correct check: If today's day is less than born day,
    # the current month hasn't been completed, so subtract 1 month.
    if today.day < born.day:
        months -= 1
        # If months becomes negative (e.g., months was 0, now -1), 
        # it means we need to take a full year off.
        if months < 0:
             months += 12 # This accounts for the month borrowed from the year calculation.


    # 3. Calculate days
    if today.day < born.day:
        # If today's day is before birth day (e.g., Today 1st, Born 15th)
        # We need to borrow days from the previous month.
        # Get the last day of the previous month
        last_day_of_prev_month = (today.replace(day=1) - datetime.timedelta(days=1)).day
        days = last_day_of_prev_month - born.day + today.day
    else:
        # Simple subtraction
        days = today.day - born.day

    return years, months, days

def main():

    # Get the date of birth with error handling
    while True:
        try:
            dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
            # Use datetime.datetime.strptime for robust parsing and validation
            born_date = datetime.datetime.strptime(dob_str, '%Y-%m-%d').date()
            
            if born_date > datetime.date.today():
                 print("Error: Date of birth cannot be in the future. Please try again.")
                 continue # Go back to the start of the loop
            
            break # Exit the loop if parsing is successful and date is valid
            
        except ValueError:
            print("Error: Invalid date format or value. Please use YYYY-MM-DD format (e.g., 1990-10-25).")


    # Calculate the age
    years, months, days = calculate_full_age(born_date)

    # Print the age
    print("-" * 30)
    print(f"Your complete age is:")
    print(f"{years} years, {months} months, and {days} days.")
    print("-" * 30)


if __name__ == '__main__':
    main()