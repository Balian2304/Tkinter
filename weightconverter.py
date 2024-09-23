import tkinter as tk
screen = tk.Tk()
screen.geometry("500x500")
screen.title("WEIGHT CONVERTER")
def function1():
    input = int(entry1.get())
    input1 = input*1000
    input2 = input*2,205
    input3 = input*35,274
    gramoutput.insert("1.0",input1)
    poundsoutput.insert("1.0",input2)
    ouncesoutput.insert("1.0",input3)
label1 = tk.Label(screen,text="Enter weight in KG",font="Arial 15 bold")
label1.place(x=20,y=20)
entry1 = tk.Entry(screen)
entry1.place(x=160,y=20)
convertbutton = tk.Button(screen,text="CONVERT", font="Arial 15 bold",command=function1)
convertbutton.place(x=320,y=20)
grams = tk.Label(screen,text="Grams",font="Arial 15 bold")
pounds = tk.Label(screen,text="Pounds",font="Arial 15 bold")
ounces = tk.Label(screen,text="Ounces",font="Arial 15 bold")
grams.place(x=60,y=120)
pounds.place(x=160,y=120)
ounces.place(x=260,y=120)
gramoutput = tk.Text(screen,height=1,width=20)
poundsoutput = tk.Text(screen,height=1,width=20)
ouncesoutput = tk.Text(screen,height=1,width=20)
gramoutput.place(x=20,y=240)
poundsoutput.place(x=120,y=240)
ouncesoutput.place(x=220,y=240)

screen.mainloop()