# Description : Mark sheet to list grades and overall average
# Author : Sebastiano GV
# Date : 2022-05-01
# Status : WIP, non functioning

from tkinter import *

master_window = Tk()

# Window Config
master_window.title("Mark Sheet")
master_window.geometry("300x100")
master_window.resizable(False,False)
master_window.configure(background = "white")

def display():
    inp = Entry(master_window,text = "How many Courses are you taking?").grid(row = 0,column = 1)
    for i in range(int(inp.get())):
        letter_to_credit = {"A":4,"B":3,"C":2,"D":1,"E":0}
        total_grade=0
        inp = Entry(master_window, text = "Letter Grade".grid(row = i+1,column = 0))
        total_grade += letter_to_credit[inp.get()]
        Label(master_window,text = total_grade).grid(row = i,column = 1)
        total_grade+=letter_to_credit[inp.get()]

button1 = Button(master_window,text = "Display",command = display).grid(row = 0,column = 0)