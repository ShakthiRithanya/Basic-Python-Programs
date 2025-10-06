def binary_search(arr: list[int], target: int) -> int:
    """
    Performs binary search for the target value in a sorted array.
    
    Args:
        arr: The list of integers to search (must be sorted).
        target: The value to find in the array.
        
    Returns:
        The index of the target element if found, otherwise returns -1.
    """
    # Initialize the pointers for the search range
    low = 0
    high = len(arr) - 1
    
    # Continue searching as long as the low pointer is less than or equal to the high pointer
    while low <= high:
        # Calculate the middle index
        # mid = (low + high) // 2 is safer than mid = low + (high - low) // 2 
        # for very large arrays in other languages, but for standard Python, the first is simpler.
        mid = (low + high) // 2
        
        # Check if the target is present at the middle
        if arr[mid] == target:
            return mid
        
        # If the target is greater than the middle element, ignore the left half
        elif arr[mid] < target:
            low = mid + 1
            
        # If the target is smaller than the middle element, ignore the right half
        else: # arr[mid] > target
            high = mid - 1
            
    # If the element is not found after the loop finishes
    return -1

# --- Example Usage (Standard Entry Point) ---

if __name__ == '__main__':
    # NOTE: Binary Search ONLY works on a sorted array!
    sorted_data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    
    # 1. Successful search case
    key_found = 23
    index_found = binary_search(sorted_data, key_found)
    
    print(f"Array: {sorted_data}")
    
    if index_found != -1:
        print(f"✅ Target {key_found} found at index: {index_found}")
    else:
        print(f"❌ Target {key_found} not found.")
        
    # 2. Unsuccessful search case
    key_not_found = 42
    index_not_found = binary_search(sorted_data, key_not_found)
    
    if index_not_found != -1:
        print(f"✅ Target {key_not_found} found at index: {index_not_found}")
    else:
        print(f"❌ Target {key_not_found} not found.")