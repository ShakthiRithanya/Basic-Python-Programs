# Program to generate terms of an Arithmetic Progression (AP)

print("Arithmetic Progression Generator")
print("-=" * 25)

# --- 1. Read first term and common difference ---
try:
    first_term = int(input("First term: "))
    common_difference = int(input("Common difference: "))
except ValueError:
    print("Invalid input. Please enter whole numbers for terms.")
    exit()

# Initial setup
current_term = first_term
terms_to_show = 10  # Initial 10 terms
total_terms_shown = 0

# --- 2. Main Loop ---
while terms_to_show != 0:
    
    # Calculate the ending term count for the current batch
    end_count = total_terms_shown + terms_to_show
    
    # --- 2. Show the terms ---
    # We loop from the number of terms already shown up to the new end_count
    while total_terms_shown < end_count:
        print(f"{current_term}", end=" --> ")
        current_term += common_difference
        total_terms_shown += 1 # Increment the count of terms shown

    print("PAUSE.\n")

    # --- 3. Ask user for more terms ---
    try:
        # Prompt user and set terms_to_show for the next iteration
        terms_to_show = int(input(f"How many terms you want to show more (Total shown: {total_terms_shown})? "))
    except ValueError:
        print("Invalid input. Assuming 0 more terms.")
        terms_to_show = 0
        
# --- 4. Finish the program ---
print(f"\n\nArithmetic Progression was finished with {total_terms_shown} terms shown.")