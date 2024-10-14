import tkinter as tk
import tkinter.ttk

screen = tk.Tk()
screen.geometry("500x500")
screen.title("PIZZA ORDER")

pizzas = ["Magherita", "Funghi", "Hawaï", "BBQ Chicken", "Neapolitan", "New York"]
label1 = tk.Label(screen, text="Welcome to Pizza Hut", font="Arial 18 bold")
label1.place(x=150, y=75)
label2 = tk.Label(screen, text="Select your fav pizza:", font="Arial 14 bold")
label2.place(x=30, y=140)
label3 = tk.Label(screen, text="Enter quantity:", font="Arial 14 bold")
label3.place(x=30, y=200)

options = tkinter.ttk.Combobox(screen)
options["values"] = pizzas
options.place(x=180, y=140)

amount = tkinter.ttk.Combobox(screen)
quantity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
amount["values"] = quantity
amount.place(x=150, y=200)

selectedoption = tk.IntVar()

buttonS = tk.Radiobutton(screen, text="S", variable=selectedoption, value=10)
buttonM = tk.Radiobutton(screen, text="M", variable=selectedoption, value=20)
buttonL = tk.Radiobutton(screen, text="L", variable=selectedoption, value=30)

buttonS.place(x=450, y=140)
buttonM.place(x=450, y=160)
buttonL.place(x=450, y=180)

output = tk.Label(screen)

def generateoutput():
    global size  
    chosensize = selectedoption.get()
    
    if chosensize == 10:
        size = "Small"
    elif chosensize == 20:
        size = "Medium"
    elif chosensize == 30:
        size = "Large"
    else:
        size = "No size selected"
    
    try:
        amountselected = int(amount.get())
    except ValueError:
        amountselected = 0 
    if amountselected == 1:
        string = "Pizza"
    else:
        string = "Pizzas"
    
    pizzaselected = options.get()  
    if not pizzaselected:
        pizzaselected = "No pizza selected"
    order = f"You ordered {amountselected} {size} {pizzaselected} {string}."
    output.config(text=order)
    output.place(x=150, y=350)


orderbutton = tk.Button(screen, text="Order", command=generateoutput)
orderbutton.place(x=200, y=295)

screen.mainloop()
