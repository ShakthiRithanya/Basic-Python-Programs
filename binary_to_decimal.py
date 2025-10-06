def bin_to_dec(n:int)->int:
    # Original core logic: Converts the input integer to a string, 
    # then interprets that string as a base 2 number for decimal conversion.
    return int(str(n),2)
    

def run_conversion():
    # --- Robust Input and Execution ---
    while True:
        try:
            # ORIGINAL LINE (Integrated with error handling): Read input as integer.
            num_input_str = input('Enter a number (base 2): ')
            num = int(num_input_str)
            
            # The core logic is executed, which will raise ValueError if non-binary digits are present.
            decimal_value = bin_to_dec(num)
            
            # --- ORIGINAL OUTPUT LINE ---
            print("It's value in base 10 is",decimal_value)
            
            break # Exit loop on success
            
        except ValueError:
            # This catches two issues:
            # 1. User enters non-numeric text (input -> int fails).
            # 2. User enters a non-binary number (e.g., 123) which fails inside bin_to_dec.
            print("Invalid input. Please enter a sequence of 0s and 1s only (e.g., 1011).")
        except Exception as e:
             # Catch any other unexpected errors
             print(f"An unexpected error occurred: {e}")
             continue
             
# --- Standard Entry Point ---
if __name__ == '__main__':
    run_conversion()