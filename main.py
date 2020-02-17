# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
window = Tk()         # Create the application window
window.title("Welcome to Fernando's Window")
# Add a label with the text "Hello"
lbl = Label(window, text="Hello! You clicked the green little run button didnt you!",font=("Arial Bold", 20))

score = 0

def addToScore():
  message = txt.get()
  if message == "Jon":
    lbl['text'] = "go away"
  else:
    lbl['text'] = "hello"

# Add a label with the text "Hello"
lbl = Label(window, text=score, font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

firstLabel = Label(window, text="This is called a Label by the way!", font=("Arial Bold", 10)) # Create the label
firstLabel.grid(column=0, row=1)   

secondLabel = Label(window, text = "You may now close this window since there is nothing else to do.", font=("Arial Bold", 10)) # Create the label
secondLabel.grid(column=0, row=2)              

thirdLabel = Label(window, text = "If you did click the green run button, agree to it below!") # Create the label
thirdLabel.grid(column=0, row=8)    

from tkinter.ttk import Progressbar
 
bar = Progressbar(window, length=200)

bar['value'] = 70
from tkinter import *
 
from tkinter.ttk import Progressbar
 
from tkinter import ttk
 
window.geometry('725x300')
 
style = ttk.Style()
 
style.theme_use('default')
 
style.configure("black.Horizontal.TProgressbar", background='black')
 
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
 
bar['value'] = 70
 
bar.grid(column=0, row=10)

from tkinter import Menu
 
menu = Menu(window)
 
new_item = Menu(menu, tearoff=0)

new_item.add_command(label='New')
new_item.add_separator()
 
new_item.add_command(label='Edit')

new_item.add_separator()

new_item.add_command(label='Print')

 
menu.add_cascade(label='File', menu=new_item)
 
window.config(menu=menu)
 
 



from tkinter import *
 
from tkinter import messagebox
 
def clicked():
 
    messagebox.showinfo('Admit Page', 'Ha, I knew it!')
 
btn = Button(window,text='Admit', command=clicked)
 
btn.grid(column=0,row=9)

# latest_tutorial.py



window.mainloop()     # Keep the window open