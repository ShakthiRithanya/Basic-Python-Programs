import sys

# --- Initial Setup ---
# Using a global dictionary for a simple user account simulation
ACCOUNTS = {
    # PIN: Balance
    1234: 999.99
}
MAX_CHANCES = 3
DEFAULT_PIN = 1234 # For easy reference
OVERDRAFT_LIMIT = 0.0 # No negative balance allowed

print("="*30, "Welcome to Python Bank ATM", "="*30)

# --- Input Handling Function ---

def get_positive_float_input(prompt):
    """Handles float input with validation."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Amount must be positive.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

# --- Main Logic Functions ---

def check_balance(current_balance):
    """Option 1: Display the current account balance."""
    print(f"\nYour current balance is: ${current_balance:.2f}")
    return current_balance

def make_withdrawal(current_balance):
    """Option 2: Handle money withdrawal with checks."""
    
    print("\nPlease choose a withdrawal option or enter '1' for custom amount:")
    print("Quick Withdrawals: 10, 20, 40, 60, 80, 100")
    
    # Prompt for withdrawal amount
    withdrawal_input = input("Enter withdrawal amount (or '1'): ")
    
    try:
        withdrawal_amount = float(withdrawal_input)
    except ValueError:
        print("\nInvalid input format.")
        return current_balance

    # Check for quick withdrawal options
    if withdrawal_amount in [10, 20, 40, 60, 80, 100]:
        amount = withdrawal_amount
    elif withdrawal_amount == 1:
        amount = get_positive_float_input("Please enter desired amount: ")
    else:
        print("\nINVALID AMOUNT. Please select a quick option or enter '1' for custom.")
        return current_balance

    # Banking Logic: Check for funds and overdraft limit
    if amount > current_balance:
        # Check against the absolute minimum (0.00 for this simple ATM)
        if current_balance - amount < OVERDRAFT_LIMIT:
             print("\nInsufficient Funds! Transaction cancelled.")
             return current_balance
    
    # Successful withdrawal
    current_balance -= amount
    print(f"\nWithdrawal successful! Please take your cash.")
    return current_balance

def make_deposit(current_balance):
    """Option 3: Handle money deposit."""
    deposit_amount = get_positive_float_input("\nHow much would you like to deposit? ")
    
    current_balance += deposit_amount
    print(f"\nDeposit successful! Your new balance is ${current_balance:.2f}")
    return current_balance

# --- Program Execution ---

def run_atm():
    chances = MAX_CHANCES
    current_balance = ACCOUNTS[DEFAULT_PIN] # Start with the default balance
    
    # --- PIN Verification Loop ---
    while chances > 0:
        try:
            pin = int(input(f"\nPlease enter your 4-digit PIN (Attempts left: {chances}): "))
        except ValueError:
            print("Invalid PIN format.")
            chances -= 1
            continue

        if pin == DEFAULT_PIN:
            print("\nCorrect PIN! Access Granted.")
            break
        else:
            print("\nINCORRECT PIN!!")
            chances -= 1
            if chances == 0:
                print("\nAccount blocked. Card retained.")
                sys.exit() # Exit the program
    
    # --- Main ATM Menu Loop (After successful PIN) ---
    restart = "Y"
    while restart.upper() not in ("N", "NO"):
        print("\n" + "="*40)
        print("1. Check Balance")
        print("2. Make a Withdrawal")
        print("3. Make a Deposit (Pay In)")
        print("4. Return Card (Exit)")
        
        try:
            option = int(input("\nWhat Would you like to Choose? (1-4): "))
        except ValueError:
            print("\nInvalid option. Please enter a number from 1 to 4.")
            continue # Loop back to show menu again

        if option == 1:
            current_balance = check_balance(current_balance)
            
        elif option == 2:
            current_balance = make_withdrawal(current_balance)
            
        elif option == 3:
            current_balance = make_deposit(current_balance)
            
        elif option == 4:
            print("\nPlease wait whilst your card is Returned....")
            print("Thank you for using Python Bank ATM.")
            sys.exit() # Exit the program
            
        else:
            print("\nPlease enter a correct number (1-4).")
            
        # Ask to continue only if an action was taken
        print(f"\nYour current balance is: ${current_balance:.2f}")
        restart = input("\nWould you like to do something else? (Y/N): ").strip()
    
    # Final exit message if user says 'No'
    print("\nThank you for your service.")

if __name__ == '__main__':
    run_atm()