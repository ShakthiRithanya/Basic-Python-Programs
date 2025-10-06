import sys

# --- Core Operation Definitions (Functions) ---
# Functions for arithmetic operations
def add(num1: float, num2: float) -> float:
    return num1 + num2

def subtract(num1: float, num2: float) -> float:
    return num1 - num2

def multiply(num1: float, num2: float) -> float:
    return num1 * num2

def divide(num1: float, num2: float) -> float:
    # IMPORTANT: Check for division by zero before calculating
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return num1 / num2

# ----------------------------------------------------------------------
# --- Input Handling Function ---

def get_numeric_input(prompt: str) -> float:
    """Gets and validates a numerical input from the user."""
    while True:
        try:
            # Use float for flexibility (can handle integers and decimals)
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number (digit).")
        except EOFError:
            # Handles Ctrl+D/Ctrl+Z input termination
            print("\nInput cancelled. Exiting.")
            sys.exit(0)


# ----------------------------------------------------------------------
# --- Main Execution Logic ---
def run_calculator():
    """Main function to run the calculator program."""
    
    # 1. Get the initial two numbers once
    print("--- SIMPLE CONSOLE CALCULATOR ---")
    num1 = get_numeric_input("Enter the first number: ")
    num2 = get_numeric_input("Enter the second number: ")

    # 2. Display Operation Menu
    print("\nChoose operation:")
    print("Press 1 for Add")
    print("Press 2 for Subtract")
    print("Press 3 for Multiply")
    print("Press 4 for Division")
    print("Press E to Exit")

    # 3. Operation Loop (Original while True loop retained)
    while True:
        # Take input from the user
        choice = input("Enter choice (1/2/3/4/E): ").strip().lower()

        if choice == 'e':
            print("Thank you for using the calculator. Goodbye!")
            break
            
        if choice in ('1', '2', '3', '4'):
            try:
                # --- Execute Operation ---
                if choice == '1':
                    result = add(num1, num2)
                    op_symbol = "+"
                elif choice == '2':
                    result = subtract(num1, num2)
                    op_symbol = "-"
                elif choice == '3':
                    result = multiply(num1, num2)
                    op_symbol = "*"
                elif choice == '4':
                    result = divide(num1, num2)
                    op_symbol = "/"
                    
                # Print the result (Common output for all operations)
                print(f"\n{num1} {op_symbol} {num2} = {result}")

            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

            # --- Next Calculation Logic (Modified for clarity) ---
            next_step = input("\nDo you want to continue operations with these numbers? (yes/no): ").strip().lower()
            if next_step in ("no", "n"):
                break
            
            # If 'yes', the loop continues, prompting for a new choice.

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or E to exit.")

# --- Standard Entry Point ---
if __name__ == "__main__":
    run_calculator()