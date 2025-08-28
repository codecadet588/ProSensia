# task7_gpa_calculator.py


import tkinter as tk
#Function to calculate GPA
def calculate_gpa():
    try:
        sub1 = float(entry1.get())
        sub2 = float(entry2.get())
        sub3 = float(entry3.get())
        sub4 = float(entry4.get())

        gpa = (sub1 + sub2 + sub3 + sub4) / 4

   
        result_label.config(text=f"Your GPA is: {gpa:.2f}")
    except ValueError:
        # Handle invalid input
        result_label.config(text="Please enter valid numbers only."
                            
# Tkinter GUI Setup
# ------------------------------

# Create the main window
root = tk.Tk()
root.title("Simple GPA Calculator")
root.geometry("300x300")

# Heading Label
heading = tk.Label(root, text="GPA Calculator", font=("Arial", 14, "bold"))
heading.pack(pady=10)

# Labels and Entry fields for 4 subjects
tk.Label(root, text="Subject 1 Marks:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Subject 2 Marks:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Subject 3 Marks:").pack()
entry3 = tk.Entry(root)
entry3.pack()

tk.Label(root, text="Subject 4 Marks:").pack()
entry4 = tk.Entry(root)
entry4.pack()

# Button to calculate GPA
calc_button = tk.Button(root, text="Calculate GPA", command=calculate_gpa)
calc_button.pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

# Run the application loop
root.mainloop()
