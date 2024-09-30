import tkinter as tk
import random
screen = tk.Tk()
screen.geometry("700x700")
screen.title("Rock Paper Scissors")
all_options = ["Rock","Paper","Scissors"]
options = tk.Label(screen,text="Your Options:",font="Arial 15 bold")
options.place(x=0,y=100)
score = 0
def game(userchoice):
  global score
  cpuchoice = random.choice(all_options)
  if userchoice == cpuchoice:
    playerselected.config(text="You selected: " + userchoice)  
    cpuselected.config(text="CPU selected: "+ cpuchoice)
  elif cpuchoice == "Rock" and userchoice == "Scissors" or cpuchoice == "Scissors" and userchoice == "Paper" or cpuchoice == "Paper" and userchoice == "Rock":
    playerselected.config(text="You selected: " + userchoice)
    cpuselected.config(text="CPU selected: "+ cpuchoice)
    score -= 1
  elif cpuchoice == "Rock" and userchoice == "Paper" or cpuchoice == "Paper" and userchoice == "Scissors" or cpuchoice == "Scissors" and userchoice == "Rock":
    playerselected.config(text="You selected: " + userchoice)
    cpuselected.config(text="CPU selected: "+ cpuchoice)
    score += 1
  scoretext.config(text="Score: " + str(score))
rockbutton = tk.Button(screen,text="Rock",font="Arial 15 bold",bg="pink",command=lambda : game("Rock"))
paperbutton = tk.Button(screen,text="Paper",font="Arial 15 bold",bg="gray",command=lambda : game("Paper"))
scissorsbutton = tk.Button(screen,text="Scissors",font="Arial 15 bold",bg="blue",command=lambda : game("Scissors"))
rockbutton.place(x=200,y=100)
paperbutton.place(x=300,y=100)
scissorsbutton.place(x=400,y=100)
scoretext = tk.Label(screen,text="Score: " + str(score),font="Arial 10 bold")
scoretext.place(x=0,y=200)
playerselected = tk.Label(screen,text="You selected: ",font="Arial 10 bold")
playerselected.place(x=0,y=300)
cpuselected = tk.Label(screen,text="CPU selected: ",font="Arial 10 bold")
cpuselected.place(x=0,y=400)
screen.mainloop()