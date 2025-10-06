from tkinter import *
from tkinter import messagebox
import sys # Added for cleaner exit

def reset_entry():
    """Clears the Age, Height, and Weight input fields."""
    age_tf.delete(0,'end')
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')

def calculate_bmi():
    """
    Handles input validation, calculates BMI, and displays the result.
    """
    try:
        # --- 1. Input Validation and Conversion ---
        # Get weight and height strings
        kg_str = weight_tf.get().strip()
        height_str = height_tf.get().strip()
        
        # Check for empty fields
        if not kg_str or not height_str:
            messagebox.showerror('Input Error', 'Height and Weight fields cannot be empty!')
            return

        # Convert to float (more flexible for non-integer inputs)
        kg = float(kg_str)
        # Height is entered in cm, convert to meters
        m_cm = float(height_str)
        m = m_cm / 100
        
        # Check for non-positive values (cannot divide by zero height)
        if kg <= 0 or m <= 0:
            messagebox.showerror('Input Error', 'Weight and Height must be positive numbers.')
            return

        # --- 2. Calculation (Original Logic Retained) ---
        bmi = kg / (m * m)
        bmi = round(bmi, 1)
        
        # --- 3. Display Result ---
        bmi_index(bmi)

    except ValueError:
        # Handles cases where user enters text (non-numeric input)
        messagebox.showerror('Input Error', 'Please enter valid numerical values for Height and Weight.')
    except ZeroDivisionError:
        # Extra safety check, though prevented by 'm <= 0' check
        messagebox.showerror('Error', 'Height cannot be zero.')
    except Exception as e:
        messagebox.showerror('System Error', f'An unexpected error occurred: {e}')


def bmi_index(bmi):
    """Determines the BMI category and shows the result."""
    
    # --- Corrected BMI Range Logic ---
    # The original logic was flawed at the boundaries (e.g., if bmi was exactly 18.5)
    # The logic is simplified using chained comparisons and correct boundaries.
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi <= 24.9:
        category = "Normal" # Covers 18.5 to 24.9
    elif bmi <= 29.9:
        category = "Overweight" # Covers 25.0 to 29.9
    else: # bmi > 29.9
        category = "Obesity"
        
    messagebox.showinfo('BMI Result', f'BMI = {bmi} is {category}')


# --- GUI Setup ---
ws = Tk()
ws.title('BMI Calculator')
ws.geometry('400x350') # Slightly increased height for better spacing
ws.config(bg='#686e70')

var = IntVar()

frame = Frame(
    ws,
    padx=15, 
    pady=15,
    relief=RIDGE # Added a slight border for separation
)
frame.pack(expand=True)

# Age Label and Entry
age_lb = Label(frame, text="Enter Age (2 - 120):", font=('Arial', 10))
age_lb.grid(row=1, column=1, sticky=W, padx=5, pady=5)

age_tf = Entry(frame)
age_tf.grid(row=1, column=2, pady=5)

# Gender Label and Radiobuttons
gen_lb = Label(frame, text='Select Gender:', font=('Arial', 10))
gen_lb.grid(row=2, column=1, sticky=W, padx=5, pady=5)

frame2 = Frame(frame)
frame2.grid(row=2, column=2, pady=5, sticky=W)

male_rb = Radiobutton(frame2, text = 'Male', variable = var, value = 1)
male_rb.pack(side=LEFT, padx=5)

female_rb = Radiobutton(frame2, text = 'Female', variable = var, value = 2)
female_rb.pack(side=LEFT, padx=5)


# Height Label and Entry
height_lb = Label(frame, text="Enter Height (cm):", font=('Arial', 10))
height_lb.grid(row=3, column=1, sticky=W, padx=5, pady=5)

height_tf = Entry(frame)
height_tf.grid(row=3, column=2, pady=5)

# Weight Label and Entry
weight_lb = Label(frame, text="Enter Weight (kg):", font=('Arial', 10))
weight_lb.grid(row=4, column=1, sticky=W, padx=5, pady=5)

weight_tf = Entry(frame)
weight_tf.grid(row=4, column=2, pady=5)


# Buttons Frame
frame3 = Frame(frame, pady=10)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Calculate BMI', # Enhanced text
    command=calculate_bmi,
    bg='#a3d900', # Added color
    padx=10
)
cal_btn.pack(side=LEFT, padx=10)

reset_btn = Button(
    frame3,
    text='Reset',
    command=reset_entry,
    bg='#ffaa00',
    padx=10
)
reset_btn.pack(side=LEFT, padx=10)

exit_btn = Button(
    frame3,
    text='Exit',
    command=lambda: ws.destroy(),
    bg='#ff4d4d',
    padx=10
)
exit_btn.pack(side=LEFT, padx=10) # Changed side to LEFT for consistent button flow

ws.mainloop()