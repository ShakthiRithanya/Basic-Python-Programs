def print_rangoli(size):
    # 'a' (97) + size - 1 -> This is the starting character code.
    chars = [chr(97 + i) for i in range(size)]
    
    # Total width of the Rangoli (same as center line length)
    # The center line has: (size * 2 - 1) characters and (size * 2 - 2) hyphens
    # Total width = (size * 2 - 1) + (size * 2 - 2) = 4 * size - 3
    # A cleaner way: each char takes 2 positions (char + dash). Total length is (4*size - 3)
    width = size * 4 - 3 
    
    lines = []
    
    for i in range(size):
        # The characters in the current row: e.g., for size=5, i=0: 'e', i=1: 'e-d', i=2: 'e-d-c'
        # chars[size - 1 - i] gives the starting character (e.g., 'a' for i=4, 'b' for i=3...)
        current_chars = chars[size - 1 - i:]
        
        # Create the full pattern for the current row: e-d-c-d-e
        pattern = '-'.join(current_chars + current_chars[:-1][::-1])
        
        # Center the pattern using string formatting (width is pre-calculated)
        line = pattern.center(width, '-')
        lines.append(line)
        
    # 1. Print the top half (excluding the center line, which is at lines[-1])
    # lines[-1:0:-1] means from last element, up to index 1 (exclusive), in reverse order
    # lines[-2::-1] - From second to last, going backward to the start.
    print('\n'.join(lines[:-1][::-1]))
    
    # 2. Print the top half + the center line
    print('\n'.join(lines))
    
    # Note: If we use lines[:-1][::-1] for top, we should use lines[::-1] for bottom,
    # and lines[1:] for the first half print.
    # The most common approach is to generate all lines:
    # final_rangoli = lines[:-1] + lines[::-1]
    
    # Let's simplify and use the common logic for visual correctness:
    final_rangoli = lines[:-1][::-1] + lines # Combines the top reversed half with the main list
    print('\n'.join(final_rangoli))


# Final Refined and Simple Logic (As requested by the problem statement for printing)
def print_rangoli(size):
    """Prints the rangoli pattern for a given size."""
    # Start char list: ['a', 'b', 'c', ...]
    chars = [chr(97 + i) for i in range(size)]
    width = size * 4 - 3 
    lines = []
    
    # Generate Top Half and Center Line
    for i in range(size):
        # Current row chars (e.g., size 3: ['c'], ['c', 'b'], ['c', 'b', 'a'])
        current_row_chars = chars[size - 1 - i:] 
        
        # Create the full pattern (e.g., 'c', 'c-b-c', 'c-b-a-b-c')
        # [::-1] reverses the list. [:-1] removes the last element.
        pattern_chars = current_row_chars + current_row_chars[:-1][::-1]
        pattern = '-'.join(pattern_chars)
        
        # Center the pattern
        line = pattern.center(width, '-')
        lines.append(line)
    
    # Print the top half (lines 0 to size-2)
    # lines[-2::-1] means start from second to last line, reverse to the start.
    print('\n'.join(lines[-2::-1])) 

    # Print the bottom half (lines 0 to size-1, which includes the center line)
    print('\n'.join(lines))

if __name__ == '__main__':
    # size = int(input("Enter size: ")) # Changed for demonstration
    size = 5
    print_rangoli(size)