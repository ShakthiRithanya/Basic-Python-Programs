# anagram is where both the strings have each characters of the same frequency
# danger and garden is an example of an anagram

from collections import Counter
import string # To handle case sensitivity and punctuation

def is_anagram(s1, s2, case_sensitive=False, ignore_spaces=True):
    """
    Checks if two strings are anagrams of each other.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.
        case_sensitive (bool): If True, 'A' and 'a' are different. Default is False.
        ignore_spaces (bool): If True, spaces and punctuation are ignored. Default is True.

    Returns:
        bool: True if they are anagrams, False otherwise.
    """
    
    # --- Pre-processing for robust comparison ---
    
    if not case_sensitive:
        s1 = s1.lower()
        s2 = s2.lower()
        
    if ignore_spaces:
        # Filter out spaces and punctuation for a standard anagram check
        s1 = ''.join(char for char in s1 if char.isalpha())
        s2 = ''.join(char for char in s2 if char.isalpha())

    # 1. Length Check (Essential and Fast Pre-check)
    if len(s1) != len(s2):
        return False
    
    # 2. Character Frequency Check using Counter (The most Pythonic way)
    # Counter(s1) creates a dictionary like {'d': 1, 'a': 1, 'n': 1, ...}
    return Counter(s1) == Counter(s2)

    # Note: Your original logic (using dictionaries) is also correct and works fine!
    # return sorted(s1) == sorted(s2) # This is O(n log n), but a good alternative
    
# --- Main Execution Block ---

print("--- Anagram Checker ---")
# Stripping leading/trailing spaces for cleaner input
s1 = input("Enter the first word or phrase: ").strip()
s2 = input("Enter the second word or phrase: ").strip()

# We often want to ignore case and spaces for phrase anagrams (e.g., "Madam Curie" vs "Me Cried Au")
if is_anagram(s1, s2): 
    print(f"\n✅ '{s1}' and '{s2}' ARE Anagrams!")
else:
    print(f"\n❌ '{s1}' and '{s2}' are NOT Anagrams.")