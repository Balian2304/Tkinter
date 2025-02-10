import tkinter as tk
from tkinter import ttk  

screen = tk.Tk()
screen.title("CALCULATOR")
screen.geometry("500x500")

number1 = tk.Entry(screen)
number1.place(x=5, y=150)

factor = ttk.Combobox(screen, values=["+", "-", "*", "/"], state="readonly")  
factor.place(x=200, y=150)

number2 = tk.Entry(screen)
number2.place(x=400, y=150)


def calculate(event):
    firstnumber = float(number1.get())
    secondnumber = float(number2.get())
    usedfactor = factor.get()
    
    if usedfactor == "+":
        result = firstnumber + secondnumber
    elif usedfactor == "-":
        result = firstnumber - secondnumber
    elif usedfactor == "*":
        result = firstnumber * secondnumber
    elif usedfactor == "/":
        if secondnumber != 0:
            result = firstnumber / secondnumber
        else:
            result = "Error: Division by zero"
    
    result_label.config(text=f"Result: {result}")

number2.bind("<Return>",calculate)
number1.bind("<Return>",calculate)
calculatebutton = tk.Button(screen, text="Calculate!", command=calculate)
calculatebutton.place(x=200, y=300)

result_label = tk.Label(screen, text="Result: ")
result_label.place(x=200, y=350)

screen.mainloop()
