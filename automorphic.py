# Function to check if a number is automorphic
def check_automorphic():
    # --- Input Validation and Setup (Added for Standardisation/Robustness) ---
    while True:
        try:
            print("Enter the number you want to check:")
            num_input = input()
            # Ensure input is a non-negative integer
            if not num_input.isdigit():
                 print("Invalid input. Please enter a whole number.")
                 continue
            
            # Store the original number for comparison and display
            original_num = int(num_input)
            
            # Automorphic logic works only for non-negative integers
            if original_num < 0:
                 print("Please enter a non-negative integer.")
                 continue

            break
        except Exception:
            # Catch unexpected errors during input
            print("An unexpected error occurred during input.")
            continue
            
    # --- Original Code Lines (Main Logic) ---

    # Re-assigning to the original variable name for the rest of the original code's logic
    num = original_num
    
    square = num * num
    flag = 0

    while(num > 0):
        if(num % 10 != square % 10):
            print("No, it is not an automorphic number.")
            flag = 1
            break

        num = num // 10
        square = square // 10

    if(flag == 0):
        print("Yes, it is an automorphic number.")

# --- Standard Entry Point ---
if __name__ == '__main__':
    check_automorphic()