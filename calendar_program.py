import calendar
import sys
from typing import Tuple

# --- Reusable Input Validation Functions ---

def validate_year() -> int:
    """Prompts the user for a 4-digit year and validates the input."""
    while True:
        year_str = input("Enter the year (format: YYYY): ").strip()
        
        # Check if it's a 4-digit number
        if year_str.isdigit() and len(year_str) == 4:
            # We can also add a reasonable range check (e.g., year > 1900) if needed.
            return int(year_str)
        else:
            print("❌ Kindly Enter a valid four-digit year number.")

def validate_month() -> int:
    """Prompts the user for a month (1-12) and validates the input."""
    while True:
        month_str = input("Enter month (format: 1-12): ").strip()
        
        # Check if it's a number and within the valid range
        if month_str.isdigit():
            month = int(month_str)
            if 1 <= month <= 12:
                return month
            else:
                print("❌ Kindly Enter a valid month number between 1 and 12.")
        else:
            print("❌ Kindly Enter a valid month number between 1 and 12.")

# --- Main Program Logic (Simplified from original) ---

def print_given_month():
    """
    Validates user input for year and month, and prints the corresponding calendar.
    """
    print("--- Monthly Calendar Generator ---")
    
    # 1. Get validated inputs using the dedicated functions
    # Original logic was split between two functions, now consolidated here for flow.
    year = validate_year()
    month = validate_month()
    
    # 2. Display the result
    print(f"\nCalendar for {calendar.month_name[month]} {year}:\n")
    
    # ORIGINAL LINE: print the month calendar
    print(calendar.month(year, month))

# --- Standard Entry Point ---
if __name__ == '__main__':
    # Use a try-except block to gracefully handle unexpected program termination
    try:
        print_given_month()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting.")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)