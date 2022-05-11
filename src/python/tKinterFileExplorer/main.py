# Decription : File Explorer popup built on tkinter
# Author : Sebastiano Giannelli Viscardi
# Data : 2022 - 05 - 01
# Status : WIP, functioning

from tkinter import *
from tkinter import filedialog

def openFiles():
    files = filedialog.askopenfilenames(initialdir = "/",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
    file_explorer_label.config("File Opened : " + files)

# Main window creation
main_window = Tk()

# Configuration of the main window
main_window.title("File Explorer")
main_window.geometry("300x100")
main_window.resizable(False,False)
main_window.configure(background = "white")

# Label creation and config
file_explorer_label = Label(main_window,text = "File Explorer",font = ("Arial",20),bg = "white")

explore_button = Button(main_window,text = "Explore",command = openFiles,bg = "white")

exit_button = Button(main_window,text = "Exit",command = main_window.destroy,bg = "white")

# Widgets arranged on grid
file_explorer_label.grid(row = 0,column = 1)
explore_button.grid(row = 1,column = 1)
exit_button.grid(row = 2,column = 1)
