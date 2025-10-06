import math # Import the math module for the accurate value of PI

def find_area(radius):
    """
    Calculates the area of a circle using the formula A = π * r^2.
    """
    # Use math.pi for maximum precision
    return math.pi * (radius ** 2)
    
def main():
    """Gets the radius input from the user and calculates the area."""
    while True:
        try:
            # Get radius input
            radius_str = input("Enter the radius of the circle: ")
            
            # Convert input to a float (allowing decimals)
            r = float(radius_str)
            
            # Validation: Radius must be a positive number
            if r <= 0:
                print("Radius must be a positive number. Please try again.")
                continue # Go back to the start of the loop
            
            break # Exit the loop if input is valid
            
        except ValueError:
            # Handle cases where input is not a valid number (e.g., 'hello')
            print("Invalid input. Please enter a numerical value for the radius.")
    
    # Calculate and print the area
    area = find_area(r)
    print(f"\nThe area of a circle with radius {r} is: {area:.2f}")

if __name__ == '__main__':
    main()