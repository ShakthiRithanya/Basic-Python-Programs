from typing import List

def to_snake_case(camel_case_name: str) -> str:
    """
    Converts a string from camelCase (e.g., userName) to snake_case (e.g., user_name).
    
    Args:
        camel_case_name: The string in camelCase format.
        
    Returns:
        The converted string in snake_case format.
    """
    snake_parts: List[str] = []
    
    for char in camel_case_name:
        if char.isupper():
            # If the character is uppercase, prepend an underscore and convert it to lowercase.
            # Avoids adding an underscore at the very beginning by checking if the list is empty.
            if snake_parts and snake_parts[-1] != '_':
                 snake_parts.append('_')
            snake_parts.append(char.lower())
        else:
            # If lowercase, just append the character.
            snake_parts.append(char)
            
    # Join all parts into a single string
    return "".join(snake_parts)

def run_conversion():
    """Handles user input and prints the result."""
    
    while True:
        # Get input from the user
        name_input = input("Enter name of variable in camelCase: ").strip()
        
        if not name_input:
            print("Input cannot be empty. Please try again.")
            continue
            
        # Execute the conversion
        snake_case_result = to_snake_case(name_input)
        
        # Display the output
        print(f"\nOriginal (camelCase): {name_input}")
        print(f"Converted (snake_case): {snake_case_result}")
        break

# --- Standard Entry Point ---
if __name__ == "__main__":
    run_conversion()