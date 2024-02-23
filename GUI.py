from tkinter import messagebox
from Directory_Structure_Creator import Directory_Structure_Creator
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

def setSourceFolder():
    source_folder_Path.set(filedialog.askdirectory())
    if source_folder_Path.get() != "":
        source_folder_label.config(text=f"Path to source folder : {source_folder_Path.get()}")
        Choose_source_folder_button.config(text="Change folder")
        Remove_source_folder_button.grid(row=0, column=2)
    else:
        source_folder_label.config(text="no source folder selected")
        Choose_source_folder_button.config(text="Choose folder")

def setDestinationFolder():
    destination_folder_Path.set(filedialog.askdirectory())
    if destination_folder_Path.get() != "":
        destination_folder_label.config(text=f"Path to destination folder : {destination_folder_Path.get()}")
        Choose_destination_folder_button.config(text="Change folder")
        Remove_destiination_folder_button.grid(row=1, column=2)
        Export_folder_button.grid(row=2, column=0)
    else:
        source_folder_label.config(text="no destination folder selected")
        Choose_destination_folder_button.config(text="Choose folder")

def removeSourceFolder():
    source_folder_Path.set("")
    source_folder_label.config(text="no source folder selected")
    Choose_destination_folder_button.config(text="Choose folder")
    Remove_source_folder_button.grid_forget()
    Export_folder_button.grid_forget()

def removeDestinationFolder():
    destination_folder_Path.set("")
    destination_folder_label.config(text="no destination folder selected")
    Choose_destination_folder_button.config(text="Choose folder")
    Remove_destiination_folder_button.grid_forget()
    Export_folder_button.grid_forget()

def exporFolder():
    message = Directory_Structure_Creator.export_folder(source_folder_Path.get(),destination_folder_Path.get())
    messagebox.showinfo("Message", message)
    
root = Tk()
tabControl = ttk.Notebook(root)

ExtractFolderFrame = Frame(tabControl)

source_folder_Path = StringVar(ExtractFolderFrame)
destination_folder_Path = StringVar(ExtractFolderFrame)

source_folder_label = Label(ExtractFolderFrame, text="No source folder selected")
source_folder_label.grid(row=0,column=0)
destination_folder_label = Label(ExtractFolderFrame, text="No destination folder selected")
destination_folder_label.grid(row=1,column=0)
Choose_source_folder_button = Button(ExtractFolderFrame,text="Choose folder", command=setSourceFolder)
Choose_source_folder_button.grid(row=0,column=1)
Choose_destination_folder_button = Button(ExtractFolderFrame,text="Choose folder", command=setDestinationFolder)
Choose_destination_folder_button.grid(row=1,column=1)

Remove_source_folder_button = Button(ExtractFolderFrame,text="Remove folder", command=removeSourceFolder)
Remove_destiination_folder_button = Button(ExtractFolderFrame,text="Remove folder", command=removeDestinationFolder)
Export_folder_button = Button(ExtractFolderFrame,text="Export folder", command=exporFolder)

tabControl.add(ExtractFolderFrame, text = "Extract folder")
tabControl.pack()

root.mainloop()