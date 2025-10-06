# Program to calculate the average of elements in a list

def calculate_average():
    # --- Input Validation for Number of Elements ---
    while True:
        try:
            # Check for valid integer input
            n_str = input("Enter the number of elements to be inserted: ")
            n = int(n_str)
            
            # Check for non-negative count
            if n < 0:
                print("The number of elements cannot be negative. Please try again.")
                continue
            
            # Check for division by zero risk
            if n == 0:
                print("Cannot calculate the average of zero elements. Please enter a number greater than 0.")
                continue
                
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for the count.")
            
    # --- Input Validation for Elements ---
    a = []
    print("Please enter the elements:")
    for i in range(0, n):
        while True:
            try:
                # Check for valid integer element input
                elem_str = input(f"Enter element {i + 1}/{n}: ")
                elem = int(elem_str)
                a.append(elem)
                break
            except ValueError:
                print("Invalid element. Please enter a whole number.")
                
    # --- Original Calculation Logic ---
    
    # Calculate average
    avg = sum(a) / n
    
    # Print the result, rounded to two decimal places
    print("Average of elements in the list", round(avg, 2))

# --- Standard Entry Point ---
if __name__ == '__main__':
    calculate_average()