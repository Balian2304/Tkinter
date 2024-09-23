import tkinter as tk
import calendar
screen = tk.Tk()
screen.geometry("500x500")
screen.title("CALENDAR")

def showcalendar():
  screen2 = tk.Tk()
  screen2.geometry("600x700")
  screen2.title("CALENDAR")
  year = int(entry1.get())
  calendardata = calendar.calendar(year)
  text = tk.Text(screen2,height=600,width=550)
  text.insert("1.0",calendardata)
  text.place(x=20,y=20)
  screen2.mainloop()
  
def exit():
  screen.destroy()
  
label1 = tk.Label(screen, text="HELLO!", font="Arial 55 bold")

calendar1 = tk.Label(screen, text="CALENDAR", font="Arial 55 bold",bg="gray")
calendar1.place(x=50,y=0)


yearentry = tk.Label(screen,text="ENTER YEAR:",font="Arial 25 bold",bg="green")
yearentry.place(x=150,y=150)

entry1 = tk.Entry(screen)
entry1.place(x=200, y=200) 

button1 = tk.Button(screen, text="Show Calendar", font="Arial 16 bold",bg="red",command=showcalendar)
button1.place(x=180, y=220)

exitbutton = tk.Button(screen, text="Exit", font="Arial 14 bold",bg="red",command=exit)

exitbutton.place(x=240, y=300)

screen.mainloop()

