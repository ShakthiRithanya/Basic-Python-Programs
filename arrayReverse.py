# Simple swapping of array elements using two pointer method

def reverse_array(arr):
    """
    Reverses the elements of a list in-place using the two-pointer method.
    """
    start = 0
    end = len(arr) - 1

    # Loop continues until the start pointer meets or crosses the end pointer.
    while start < end:
        # Pythonic swap: Swapping without a temporary variable.
        # This is more readable and efficient in Python.
        arr[start], arr[end] = arr[end], arr[start]
        
        # Move pointers inward
        start += 1
        end -= 1

# --- User Input and Execution ---

def get_input_and_reverse():
    """Handles user input, calls the reverse function, and prints results."""
    
    # 1. Get number of elements with validation
    while True:
        try:
            n = int(input("Enter the number of elements: "))
            if n < 0:
                 print("Please enter a non-negative number.")
                 continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            
    # 2. Get array elements with validation
    arr = []
    print("Enter the elements one by one:")
    for i in range(n):
        while True:
            try:
                element = int(input(f"Element {i+1}/{n}: "))
                arr.append(element)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # 3. Process and Print
    print("\n--- Processing ---")
    print("Array before reversing:", arr)
    
    reverse_array(arr)
    
    print("Array after reversing:", arr)

# Standard entry point for a Python script
if __name__ == '__main__':
    get_input_and_reverse()