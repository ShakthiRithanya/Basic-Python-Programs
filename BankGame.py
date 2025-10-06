# default password is 4758
import random
import sys # Added for proper program exit

# --- Global/Initial Variables (Set outside the function for better scope) ---
# NOTE: The default password check logic in the original code relies on this fixed value
DEFAULT_PIN = 4758 

class BankGame :
    # Using staticmethod and class is unnecessary here, but retained the structure
    @staticmethod
    def main( args) :
        print("---WELCOME TO ELIX BANKING SERVICES---")
        print("")
        print("________________________")
        print("Enter your name: ")
        name = input()
        
        # Original code used 'do loop' concept, which translates to a 'while True' loop
        print("Hi, " + name + "\b, Welcome to my program!") # Added comma for better reading
        print("____________________________")
        
        # --- Start/Repeat Logic ---
        print("Do you want to start/repeat the program?")
        print("Enter Y for Yes and N for No: ")
        temp = input()[0]
        
        # --- Variables (Initialize inside main) ---
        # The original code had a major error: it asked for the password *before* the loop, 
        # but the variable 'passw' was hardcoded to 4758, ignoring the input.
        
        # 1. Password/Balance Setup
        passw = DEFAULT_PIN # The actual current password (starts as default)
        bal = 10000         # Current account balance
        # leftbal = 0       # Unused variable removed for cleanliness but left if needed for compatibility
        
        # 2. PIN Verification (Fixed Logic)
        verified = False
        print("If you don\'t know the password refer the first line of the program")
        
        # New loop for robust PIN entry (up to 3 tries)
        attempts = 3
        while attempts > 0 and not verified:
            try:
                print("Please enter the password: ")
                entered_pin = int(input())
                if entered_pin == passw:
                    verified = True
                    break
                else:
                    print("You have entered wrong password.....Try again!")
                    attempts -= 1
            except ValueError:
                print("Invalid input. Please enter a number.")
                attempts -= 1
        
        if not verified and attempts == 0:
             print("Too many wrong attempts. Program terminated.")
             return 0 # Exit if verification fails
             
        
        # --- Main Program Loop (Fixed Logic) ---
        # Condition when the statement goes true i.e.- temp equals Y/y
        while True :
            if (temp == 'Y' or temp == 'y') and verified :
                # --- START OF BANKING OPERATIONS ---
                
                # The original code had redundant passw == 4758 check inside the loop. Removed it.
                print("")
                print(f"Welcome back, {name}! Your initial account balance is Rs. {bal}") # Added f-string
                
                # Using for statement to perform 5 operation on each login (Changed to while loop limit)
                x = 0
                
                # The original logic runs for x <= 6 (7 operations). Retained the original loop limit.
                while (x <= 6) : 
                    print("0. Exit")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Change passcode")
                    print("4. Check balance")
                    print("5. Customer care")
                    print("Enter the serial no. of your choice")
                    
                    try:
                        choice = int(input())
                    except ValueError:
                        print("Invalid choice! Enter a number.")
                        continue # Skip to next iteration
                        
                    # --- CAPTCHA Verification (Retained and fixed) ---
                    print("Enter captha to verify that you are not a robot.")
                    captha = random.randrange(10000)
                    print(captha)
                    print("Enter the number shown above: ")
                    
                    try:
                        verify = int(input())
                    except ValueError:
                        verify = -1 # Assign a non-matching value on error

                    if (verify == captha) :
                        # If captha gets matched, then these switch statements are executed.
                        if (choice==0):
                            print("BYE!......" + name + " HAVE A NICE DAY!")
                            print("__________________________")
                            print("@author>[@programmer-yash")
                            print("Please comment here or open an issue if you have any queries or suggestions!")
                            print("")
                            print("#hacktoberfest")
                            return 0 # Use return to exit the function
                        
                        elif(choice==1):
                            # --- Deposit ---
                            print("You have chosen to deposit.")
                            print("Enter the amount to deposit : ")
                            try:
                                deposit = int(input())
                                if deposit <= 0:
                                    print("Deposit amount must be positive.")
                                elif deposit > 0: # Only deposit positive amounts
                                    bal = bal + deposit
                                    print(str(deposit) + " has been deposited to your account.")
                                    # print("Left balance is " + str(bal)) # Original line
                                    print(f"Current balance is Rs. {bal}")
                            except ValueError:
                                print("Invalid amount entered.")

                        elif(choice==2):
                            # --- Withdraw ---
                            print("You have chosen to withdraw.")
                            print("Enter the amount to be withdrawn")
                            try:
                                withdraw = int(input())
                                if withdraw <= 0:
                                    print("Withdrawal amount must be positive.")
                                elif withdraw > bal:
                                    print("INSUFFICIENT FUNDS. Cannot withdraw.")
                                else:
                                    # print(str(+withdraw) + " has been withdrawn from your account.") # Original line
                                    print(f"Rs. {withdraw} has been withdrawn from your account.")
                                    bal = bal - withdraw
                                    print("Check the cash printer.")
                                    # print("Left balance is " + str(bal)) # Original line
                                    print(f"Current balance is Rs. {bal}")
                            except ValueError:
                                print("Invalid amount entered.")

                        elif(choice==3):
                            # --- Change Passcode ---
                            print("You have chosen to change passcode.")
                            print("Enter the current passcode: ")
                            try:
                                check = int(input())
                                if (check == passw) :
                                    print("Enter the new passcode (4 digits):")
                                    newP = int(input())
                                    passw = newP # Update the *live* password
                                    print("Your new password is " + str(newP))
                                else :
                                    print("Wrong passcode!")
                            except ValueError:
                                print("Invalid passcode entered.")

                        elif(choice==4):
                            # --- Check Balance ---
                            print("You have chosen to check balanace.")
                            print("Your current account balance is " + str(bal))
                            
                        elif(choice==5):
                            # --- Customer Care ---
                            print("You have chosen for customer care.")
                            print("Contact us at:")
                            print("           Email: yash197911@gmail.com")
                            
                        else:
                            print("Wrong choice!!! Choose again...!")
                    else :
                        # CAPTCHA failed
                        print("xCAPTHA NOT CORRECTx")
                        
                    x += 1 # Increment operation counter
                
                # --- End of x <= 6 loop ---
                
                # Ask to restart the whole process (Y/N)
                print("\n7 Operations completed.")
                print("Do you want to start/repeat the program?")
                print("Enter Y for Yes and N for No: ")
                try:
                    temp = input()[0]
                except IndexError:
                    temp = 'N' # Default to N if no input
                
                # If the user wants to continue (temp='Y'), the outer loop will repeat.
                # If the user enters 'N', the 'temp' check below handles the exit.
                continue # Go to the outer while loop's condition check
            
            # --- Condition when user chooses to exit (N/n) ---
            elif(temp == 'N' or temp == 'n') :
                print("BYE!......" + name + " HAVE A NICE DAY!")
                print("__________________________")
                # print("@author>[@programmer-offbeat]") # Retained author tag
                print("Please comment here if you have any queries or suggestions!")
                print("--OR--")
                print("create an issue")
                print("I will rightly see and reply to your messages and suggestions!")
                print()
                print("HAPPY CODING!:-)")
                return 0 # Use return to exit the function
            
            # --- Condition for Invalid Y/N input ---
            else :
                print("Err!..... You have entered a wrong choice!")
                print("Try again....!")
                
                # Ask again for Y/N choice
                print("Do you want to start/repeat the program?")
                print("Enter Y for Yes and N for No: ")
                temp = input()[0]
                continue # Go to the next loop iteration
            
            # --- Dead Code/Wrong Logic Removal ---
            # The following lines were causing major issues and are now irrelevant due to fixed PIN logic:
            # if (passw != 4758) : print("You have entered wrong password.....Try again!")
            # if((temp < 100) == False) : break
    

if __name__=="__main__":
    BankGame.main([])