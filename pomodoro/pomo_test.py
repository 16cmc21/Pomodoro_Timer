import tkinter as tk
from tkinter import messagebox
from winsound import *


def parse_input_study(entry):
    global p
    global initial_p
    global state
    state = False
    if (entry != ''):
        p = int(entry)*60
        initial_p = p
    
def parse_input_break(entry):
    global b
    global initial_b
    global state
    state = False
    if (entry != ''):
        b = int(entry)*60
        initial_b = b
        
def message(title, inputInfo): #should always use style 0 in this case
    win = tk.Toplevel()
    win.wm_title(title)
    
    l = tk.Label(win, text=inputInfo)
    l.grid(row=0, column=0)
    
    b = tk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)

def timer():
    global countdown
    global p
    global b
    global initial_p
    global initial_b
    global state
    if(state):
        if(p!=0):
            pmins, psecs = divmod(p, 60)
            countdown[0]=pmins
            countdown[1]=psecs
            timeString = pattern.format(countdown[0], countdown[1])
            timeText.configure(text=timeString)
            p -= 1
            if(p==0 and b!=0):
                #Playsound("file_name", SND_FILENAME) #still need to add actual file name needs to be wav file
                messagebox.showwarning("Break Time", "Time to take a break")
        elif(b!=0):
            bmins, bsecs = divmod(b, 60)
            countdown[0]=bmins
            countdown[1]=bsecs
            timeString=pattern.format(countdown[0], countdown[1])
            timeText.configure(text=timeString)
            b -= 1
            if(p==0 and b==0):
                #Playsound("file name", SND_FILENAME) #still need to add actual file name needs to be wav file
                messagebox.showwarning("Break Time Over", "Lets get back to work")
    if(b==0 and p==0):
        p = initial_p
        b = initial_b
    root.after(1000, timer)

def start():
    global state
    global initial_p
    global initial_b
    if(initial_b != 0 and initial_p != 0):
        state = True

def pause():
    global state
    state = False
    
def quickstart():
    global p
    global initial_p
    global b
    global initial_b
    global state
    p = 25*60
    initial_p = p
    b = 5*60
    initial_b = b
    state = True
    
    
    
initial_p = 0
initial_b = 0
p = 0
b = 0
state = False

root = tk.Tk()
root.title("Tomato Timer")

canvas = tk.Canvas(root, height=350, width=500)
canvas.pack()

background_image = tk.PhotoImage(file='bg.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

countdown = [0,0]
pattern = '{:02d}:{:02d}'

timeText = tk.Label(root, bg='#cbd3d3', text="00:00", font=("Helvetica", 100))
timeText.place(relx=0.5, rely=0.32, relwidth=0.70, relheight=0.40, anchor='n')

frame = tk.Frame(root, bg='#cbd3d3', bd=4)
frame.place(relx=0.5, rely=0.01, relwidth=0.8, relheight=0.15, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button1 = tk.Button(frame, text="Study Time", font=40, command=lambda: parse_input_study(entry.get()))
button1.place(relx=0.7, relheight=1, relwidth=0.3)

frame2 = tk.Frame(root, bg='#cbd3d3', bd=4)
frame2.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.15, anchor='n')

entry2 = tk.Entry(frame2, font=40)
entry2.place(relwidth=0.65, relheight=1)

button2 = tk.Button(frame2, text="Break Time", font=40, command=lambda: parse_input_break(entry2.get()))
button2.place(relx=0.7, relheight=1, relwidth=0.3)

button5 = tk.Button(root, text="Pomodoro Time", font=40, command=lambda: quickstart())
button5.pack()

button3 = tk.Button(root, text="Begin Studying", font=40, command=lambda: start())
button3.pack()

button4 = tk.Button(root, text="Pause", font=40, command=lambda: pause())
button4.pack()

timer()
root.mainloop()