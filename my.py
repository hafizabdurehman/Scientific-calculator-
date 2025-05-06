import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    try:
        expression = entry.get()
        expression = expression.replace('π', str(math.pi))
        expression = expression.replace('e', str(math.e))
        expression = expression.replace('^', '**')
        expression = expression.replace('√', 'math.sqrt')
        expression = expression.replace('sin', 'math.sin(math.radians')
        expression = expression.replace('cos', 'math.cos(math.radians')
        expression = expression.replace('tan', 'math.tan(math.radians')

        if 'sin' in expression or 'cos' in expression or 'tan' in expression:
            expression += ')'

        result = eval(expression, {"__builtins__": None}, {
            "math": math,
            "sqrt": math.sqrt
        })
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid expression: {e}")

def clear():
    entry.delete(0, tk.END)

def button_click(char):
    entry.insert(tk.END, char)

# GUI setup
root = tk.Tk()
root.title("Scientific Calculator BY HAFIZ ABDUR REHMAN")
root.geometry("400x700")
root.configure(bg="#1f1f1f")

entry = tk.Entry(root, font=('Arial', 22), bg="#ffffff", fg="#000000", bd=10, relief="sunken", justify='right')
entry.pack(pady=30, ipady=30, ipadx=80, fill='x', padx=80)

buttons = [
    ['7', '8', '9', '/', 'C'],
    ['4', '5', '6', '*', '√'],
    ['1', '2', '3', '-', '^'],
    ['0', '.', '=', '+', 'π'],
    ['(', ')', 'sin', 'cos', 'tan'],
  
]

frame = tk.Frame(root, bg="#1f1f1f")
frame.pack(padx=18, pady=18)

# Create buttons
for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        if char == '=':
            cmd = calculate
            bg = "#00c853"
            fg = "white"
        elif char == 'C':
            cmd = clear
            bg = "#d50000"
            fg = "white"
        else:
            cmd = lambda ch=char: button_click(ch)
            bg = "#333333"
            fg = "white"

        btn = tk.Button(frame, text=char, width=5, height=3,
                        font=('Arial', 12, 'bold'), bg=bg, fg=fg,
                        command=cmd)
        btn.grid(row=r, column=c, padx=5, pady=5, sticky='nsew')

# Adjust grid weights
for i in range(len(buttons)):
    frame.grid_rowconfigure(i, weight=1)
for j in range(5):
    frame.grid_columnconfigure(j, weight=1)

root.mainloop()
