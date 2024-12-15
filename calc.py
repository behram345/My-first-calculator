import tkinter as tk
from tkinter import messagebox
from math import sin, cos, tan, log, sqrt, pi, e

def evaluate_expression():
    """Evaluate the mathematical expression entered by the user."""
    try:
        expression = entry.get()
        result = eval(expression, {"__builtins__": None}, math_functions)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as ex:
        messagebox.showerror("Error", f"Invalid input: {ex}")

def append_to_expression(value):
    """Append a character or function to the expression."""
    entry.insert(tk.END, value)

def clear_entry():
    """Clear the input field."""
    entry.delete(0, tk.END)

# Define allowed mathematical functions and constants
math_functions = {
    "sin": sin,
    "cos": cos,
    "tan": tan,
    "log": log,
    "sqrt": sqrt,
    "pi": pi,
    "e": e
}

# Initialize the main application window
root = tk.Tk()
root.title("Advanced Calculator")

# Input field
entry = tk.Entry(root, width=30, font=("Arial", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons for digits and operations
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=evaluate_expression)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: append_to_expression(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Additional buttons for functions and actions
extra_buttons = [
    ("C", clear_entry, 5, 0), ("sin", "sin(", 5, 1), ("cos", "cos(", 5, 2), ("tan", "tan(", 5, 3),
    ("log", "log(", 6, 0), ("sqrt", "sqrt(", 6, 1), ("pi", "pi", 6, 2), ("e", "e", 6, 3)
]

for (text, value, row, col) in extra_buttons:
    if callable(value):
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=value)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda v=value: append_to_expression(v))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Run the application
root.mainloop()
