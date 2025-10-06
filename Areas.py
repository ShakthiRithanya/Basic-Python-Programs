# Program to calculate the areas of 2D shapes
import math

# --- Area Calculation Functions (with math.pi) ---

def square(side):
    """Calculates the area of a square."""
    return side ** 2

def rectangle(length, breadth):
    """Calculates the area of a rectangle."""
    return length * breadth

def triangle(side1, side2, side3):
    """Calculates the area of a triangle using Heron's formula."""
    # Check for the triangle inequality theorem (a + b > c)
    if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
        # A triangle with these sides cannot exist
        raise ValueError("Invalid side lengths: Sum of any two sides must be greater than the third side.")
    
    s = (side1 + side2 + side3) / 2
    # Area = sqrt(s * (s-a) * (s-b) * (s-c))
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area

def circle(radius):
    """Calculates the area of a circle using the precise math.pi."""
    # Using math.pi for better accuracy than 3.14
    return math.pi * (radius ** 2)

# --- Helper Function for Robust Input ---

def get_positive_float_input(prompt):
    """Handles input to ensure it's a positive number."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be positive. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

# --- Main Program Logic ---

def main():
    """Main function to handle shape selection and calculation."""
    print("Choose the shape you want to calculate area of:")
    
    while True:
        print("\nAvailable shapes: Square, Rectangle, Triangle, Circle")
        shape = input('>> ').lower().strip() # .strip() removes accidental spaces

        if shape == "square":
            side = get_positive_float_input("Enter the value of the side: ")
            final_area = square(side)
            break

        elif shape == "rectangle":
            length = get_positive_float_input("Enter the value of length: ")
            breadth = get_positive_float_input("Enter the value of breadth: ")
            final_area = rectangle(length, breadth)
            break

        elif shape == "triangle":
            print("\nEnter the side lengths (must form a valid triangle):")
            side1 = get_positive_float_input("1st side: ")
            side2 = get_positive_float_input("2nd side: ")
            side3 = get_positive_float_input("3rd side: ")
            
            try:
                final_area = triangle(side1, side2, side3)
                break
            except ValueError as e:
                print(f"Error: {e}")
                continue # Go back to shape selection if triangle is invalid

        elif shape == "circle":
            radius = get_positive_float_input("Enter the value of the radius: ")
            final_area = circle(radius)
            break

        else:
            print("❌ Invalid selection. Please choose one of the four shapes.")

    # Final Output
    print("-" * 30)
    print(f"The area of the selected {shape.capitalize()} is: {final_area:.2f}")

if __name__ == '__main__':
    main()