import sys
from typing import List

# --- Core Algorithm (Defined outside class for flexibility, but using the class for execution) ---
def recursive_bubble_sort_logic(arr: List[int], n: int) -> None:
    """
    The recursive core logic for Bubble Sort.
    Performs one pass of bubble sort and then recursively calls itself 
    for the remaining unsorted part (n-1).
    """
    # Base case: If the array size is 1, it's sorted.
    if n == 1:
        return
    
    swapped = False # Use a boolean flag for cleaner optimization check
    
    # One pass of bubble sort: ensures the largest element moves to the end (arr[n-1])
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            # Swap elements
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True
            
    # Optimization (Early Exit): If no two elements were swapped in the pass, the array is fully sorted.
    if not swapped:
        return
        
    # Largest element is fixed (arr[n-1]). Recur for the remaining n-1 elements.
    recursive_bubble_sort_logic(arr, n - 1)


# --- Object-Oriented Wrapper (Retaining user's class structure) ---
class BubbleSort:
    """A wrapper class to hold the array and initiate the recursive sort."""
    
    def __init__(self, array: List[int]):
        # Use an underscore for internal attributes, following convention
        self._array = array
        self._length = len(array)
 
    def __str__(self) -> str:
        # Standard Python way to display the object's state (the array)
        return " ".join([str(x) for x in self._array])
    
    def __repr__(self) -> str:
        return f"BubbleSort({self._array})"
 
    def sort(self) -> None:
        """The main method to start the recursive sort."""
        # Call the core logic using the array held by the class instance
        recursive_bubble_sort_logic(self._array, self._length)
    
    @property # Use property decorator to expose the array data cleanly
    def array(self) -> List[int]:
        return self._array
        
# ----------------------------------------------------------------------
# Driver Code (Enhanced)
def main():
    """Main execution function to demonstrate the sorting."""
    
    print("--- Recursive Bubble Sort Demonstration ---")
    
    # Test case 1
    array1 = [64, 34, 25, 12, 22, 11, 90]
    sort1 = BubbleSort(array1)
    
    print(f"Original array 1: {sort1.array}")
    sort1.sort()
    print(f"Sorted array 1:   {sort1}") # Uses the __str__ method
    
    print("-" * 35)

    # Test case 2 (Already nearly sorted for optimization test)
    array2 = [1, 5, 2, 7, 3]
    sort2 = BubbleSort(array2)

    print(f"Original array 2: {sort2.array}")
    sort2.sort()
    print(f"Sorted array 2:   {sort2}")


# ----------------------------------------------------------------------
# Tests (Retained and slightly adjusted for cleaner access)
def test_result_in_order():
    """Pytest case to ensure the resulting array is sorted."""
    array = [64, 34, 25, 12, 22, 11, 90]
    sort = BubbleSort(array)       
    sort.sort() # Use the standardized method name
    
    # Check if the array is sorted correctly
    for i in range(sort._length - 1): # Accessing length directly via protected attribute
        assert sort.array[i] <= sort.array[i+1] # Use <= for better robustness
 
 
if __name__ == "__main__":
    main()