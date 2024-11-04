import tkinter as tk
import tkinter.messagebox 
import tkinter.filedialog

screen = tk.Tk()
screen.geometry("500x500")
screen.title("Phone Book")

myaddressbook = {}
name = tk.Label(screen, text="Name", font="Arial 15 bold")
addressbook = tk.Label(screen, text="My addressbook", font="Arial 15 bold")
nameentry = tk.Entry()
address = tk.Label(screen, text="Address", font="Arial 15 bold")
addressentry = tk.Entry()
mobile = tk.Label(screen, text="Mobile", font="Arial 15 bold")
mobileentry = tk.Entry()
email = tk.Label(screen, text="Email", font="Arial 15 bold")
emailentry = tk.Entry()
birthday = tk.Label(screen, text="Birthday", font="Arial 15 bold")
birthdayentry = tk.Entry()
result = tk.Listbox(screen)

def edit():
    selectedindex = result.curselection()
    selectedname = result.get(selectedindex)
    selected = myaddressbook[selectedname]
    addressentry.insert(0,selected[0])
    mobileentry.insert(0,selected[1])
    emailentry.insert(0,selected[2])
    birthdayentry.insert(0,selected[3])
    nameentry.insert(0,selectedname)

def delete():
    selecteditem = result.curselection()
    for i in reversed(selecteditem):
        name_to_delete = result.get(i)
        del myaddressbook[name_to_delete]
        result.delete(i)

def updatelistbox():
   result.delete(0,tk.END)
   for name in myaddressbook.keys():
       result.insert(tk.END,name)

def update():
    global myaddressbook
    n = nameentry.get()
    if n == "":
        tk.messagebox.showinfo("", "Name cannot be empty!")
        return
    a = addressentry.get()
    b = birthdayentry.get()
    m = mobileentry.get()
    e = emailentry.get()
    myaddressbook[n] = [a, m, e, b]
    nameentry.delete(0,tk.END)
    birthdayentry.delete(0,tk.END)
    mobileentry.delete(0,tk.END)
    emailentry.delete(0,tk.END)
    addressentry.delete(0,tk.END)

    updatelistbox()

def open():
    global myaddressbook
    file1 = tkinter.filedialog.askopenfile()
    if file1 is not None:
        myaddressbook = eval(file1.read())
        print(myaddressbook)
        updatelistbox()
def show():
    selected = result.curselection()
    if selected:
        n = result.get(selected[0])
        contact_info = myaddressbook.get(n)
        if contact_info:
            a, m, e, b = contact_info
            tk.messagebox.showinfo(
                "Contact Details", 
                f"Name: {n}\nAddress: {a}\nMobile: {m}\nEmail: {e}\nBirthday: {b}"
            )
    else:
        tk.messagebox.showinfo("Error", "Please select a contact to view.")

def save():
    file1 = tkinter.filedialog.asksaveasfile()
    if file1 is not None:
        print(myaddressbook,file=file1)
        result.delete(0,tk.END)
        myaddressbook.clear()
showbutton = tk.Button(screen, text="Show", command=show)
editbutton = tk.Button(screen, text="Edit", command=edit)
deletebutton = tk.Button(screen, text="Delete", command=delete)
updatebutton = tk.Button(screen, text="Update", command=update)
savebutton = tk.Button(screen, text="Save", command=save)
openbutton = tk.Button(screen,text="Open",command=open)
name.grid(row=3, column=3)
nameentry.grid(row=3, column=4)
address.grid(row=4, column=3)
addressentry.grid(row=4, column=4)
mobile.grid(row=5, column=3)
mobileentry.grid(row=5, column=4)
email.grid(row=6, column=3)
emailentry.grid(row=6, column=4)
birthday.grid(row=7, column=3)
birthdayentry.grid(row=7, column=4)
result.grid(row=3, rowspan=5, column=1, columnspan=2)
showbutton.grid(row=1, column=3)
openbutton.grid(row=1,column=4)
editbutton.grid(row=9, column=1)
deletebutton.grid(row=9, column=2)
updatebutton.grid(row=9, column=4)
savebutton.grid(row=10, column=3)
addressbook.grid(row=1, column=2)

screen.mainloop()
