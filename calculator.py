import tkinter as tk
from functools import partial

# Function to update the display
def button_click(entry, char):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + char)

# Function to evaluate the expression
def calculate(entry):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the display
def clear(entry):
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Colorful Calculator")

# Create an entry widget for the display
entry = tk.Entry(root, width=25, borderwidth=2, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4)

# Define button colors
button_colors = {
    '1': 'lightblue', '2': 'lightgreen', '3': 'lightpink', 
    '4': 'lightyellow', '5': 'lightblue', '6': 'lightgreen',
    '7': 'lightpink', '8': 'lightyellow', '9': 'lightblue',
    '0': 'lightgreen', '+': 'lightcoral', '-': 'lightcoral',
    '*': 'lightcoral', '/': 'lightcoral', '=': 'lightseagreen',
    'C': 'lightgrey'
}

# Create buttons and place them on the grid
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    'C', '0', '=', '+'
]

row, col = 1, 0
for button in buttons:
    action = partial(button_click, entry, button) if button not in ['=', 'C'] else (partial(calculate, entry) if button == '=' else partial(clear, entry))
    tk.Button(root, text=button, padx=20, pady=20, bg=button_colors[button], command=action, font=('Arial', 18)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the application
root.mainloop()
