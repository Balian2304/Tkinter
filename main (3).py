import tkinter as tk

screen = tk.Tk()
screen.geometry("500x500")
screen.title("CELSIUS TO FAHRENHEIT")

label1 = tk.Label(screen, text="CELSIUS --> FAHRENHEIT", font="Arial 25 bold")
label1.place(x=0, y=0)

label2 = tk.Label(screen, text="ENTER A VALUE", font="Arial 15 bold")
label2.place(x=0, y=100)

entry1 = tk.Entry(screen)
entry1.place(x=200, y=100)

def fahrenheit():
    try:
        value = int(entry1.get())  
        value2 = (value * 9 / 5) + 32
        label_result.config(text=f"{value} Celsius = {value2:.2f} Fahrenheit")
    except ValueError:
        label_result.config(text="Please enter a valid number")

button1 = tk.Button(screen, text="Show Fahrenheit", font="Arial 15 bold", command=fahrenheit)
button1.place(x=300, y=100)

label_result = tk.Label(screen, text="", font="Arial 15 bold")
label_result.place(x=0, y=200)

screen.mainloop()
