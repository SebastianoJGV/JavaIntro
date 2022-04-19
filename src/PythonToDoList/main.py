from tkinter import *
from tkinter import messagebox
#Main window, along with size and title

def addTask():
    #adds task to list
    task = manualEntry.get()#Get manual input
    if task == "":#Safety check
        messagebox.showinfo("Error", "Please enter a task")
    else:#insert new task at end of list
        mainlist.insert(END, task)
        manualEntry.delete(0, END)

def delTask():
    mainlist.delete(ANCHOR)#delete the selected item



ws = Tk()
ws.geometry('500x450+500+200')
ws.title('ToDoList')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)#frame size not adjustable

frame=Frame(ws)
frame.pack(pady=10)


#This listbox will list all taks in the todolist
mainlist=Listbox(frame, 
    width=25, #width of the listbox
    height=8, #height of the listbox
    bg='#223441', #background color
    fg='#ffffff', #foreground color
    font=('Arial', 12), #font size
    bd=0, #border width
    highlightthickness=0)#Highlighting of selected content

mainlist.pack(side=LEFT, fill=BOTH)#Left aligned in frame, fill will fill blank space

#Dummy tasks used to test software
dummyTasks=[
    'Chaos Gates',
    'Abyss Raids',
    'Unas tasks',
    'Rapport',
    'Arkesia Race'
    ]

#Add items to end of list in window
for item in dummyTasks:
    mainlist.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)#TodoList content is left alinged, scroll bar is right aligned

mainlist.config(yscrollcommand=sb.set)#sets scrollbar to yscrollcommand
sb.config(command=mainlist.yview)#chanes y view of listbox

#Manual input of tasks
manualEntry=Entry(frame,
    font=('Arial', 12)
    )

#Pack geometry with padding of 20
manualEntry.pack(pady=20)

#Seperate frames for buttons
buttonFrame=Frame(ws)
buttonFrame.pack(pady=20)


#Button to add task to list
addButton=Button(
    buttonFrame,
    text='Add Task',
    font=('Arial', 12),
    bg='#223441',
    padx=10,
    pady=10,
    command=addTask #Function, adds content to listbox
)
addButton.pack(fill=BOTH, expand=True, side=LEFT)

delButton=Button(
    buttonFrame,
    text='Delete Task',
    font=('Arial', 12),
    bg='#223441',
    padx=10,
    pady=10,
    command=delTask #Function, deletes content to listbox
)
delButton.pack(fill=BOTH, expand=True, side=RIGHT)

ws.mainloop