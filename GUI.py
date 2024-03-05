import os
from tkinter import messagebox
from Directory_Structure_Creator import Directory_Structure_Creator
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

Obj = None
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
    create_folder_destination_label.config(text="no destination folder selected")
    Choose_destination_folder_button.config(text="Choose folder")
    Remove_destiination_folder_button.grid_forget()
    Export_folder_button.grid_forget()

def exportFolder():
    message = Directory_Structure_Creator.export_folder(source_folder_Path.get(),destination_folder_Path.get())
    messagebox.showinfo("Message", message)

def createFolderStructure():
    global obj
    message = None
    filepath, extension = os.path.splitext(souruce_file_path.get())
    if extension == ".txt":
        obj = Directory_Structure_Creator(souruce_file_path.get())
        obj.parse_File()
        message = obj.create_structure(destination_folder_path=destination_folder_Path.get())
    elif extension == ".json":
        if filepath.endswith("Metadata"):
            obj = Directory_Structure_Creator.from_Metadata(souruce_file_path.get())
            message = obj.create_structure(destination_folder_path=destination_folder_Path.get())
        else:
            obj = Directory_Structure_Creator.from_JSON(souruce_file_path.get())
            message = obj.create_structure(destination_folder_path=destination_folder_Path.get())
    messagebox.showinfo("Message",message=message)
    Save_folder_structure_button.grid(row=2, column=1)

def saveFolderStructure():
    saveas_window = Tk()
    saveas_window.title("Save as")
    save_location = StringVar(ExtractFolderFrame)

    def set_save_location():
        save_location.set(filedialog.askdirectory())
        Save_destination_folder_label.config(text=f"Path to folder : {save_location.get()}")
        Save_destination_folder_button.config(text="Change folder")
        Remove_Save_destination_folder_button.grid(row=0, column=2)
        Save_button.grid(row=0, column=3)
        print(save_location.get())
    
    def remove_save_location():
        save_location.set("")
        Save_destination_folder_label.config(text="No save location chosen")
        Save_destination_folder_button.config(text=f"Change folder")
        Remove_Save_destination_folder_button.grid_forget()
        Save_button.grid_forget()
        # print(save_location.get())
    
    def save():
        global obj
        obj.save(destination_folder_path=save_location.get())

    Save_destination_folder_label = Label(saveas_window,text="No save location chosen")
    Save_destination_folder_label.grid(row=0, column=0)
    Save_destination_folder_button = Button(saveas_window,text="Choose folder", command=set_save_location)
    Save_destination_folder_button.grid(row=0, column=1)
    Remove_Save_destination_folder_button = Button(saveas_window,text="Remove folder", command=remove_save_location)
    Save_button = Button(saveas_window,text="save", command=save)

    saveas_window.mainloop()

def setSourceFile():
    souruce_file_path.set(filedialog.askopenfilename())
    if souruce_file_path.get() != "":
        source_file_label.config(text=f"Path to source file : {souruce_file_path.get()}")
        Choose_source_file_button.config(text="Change file")
        Remove_source_file_button.grid(row=0, column=2)
    else:
        source_file_label.config(text="no source file selected")
        Choose_source_file_button.config(text="Choose source file")

def setTargetFolder():
    destination_folder_Path.set(filedialog.askdirectory())
    if destination_folder_Path.get() != "":
        create_folder_destination_label.config(text=f"Path to destination folder : {destination_folder_Path.get()}")
        CreateFolder_Choose_destination_folder_button.config(text="Change folder")
        CreateFolder_Remove_destiination_folder_button.grid(row=1, column=2)
        Create_folder_structure_button.grid(row=2, column=0)
        # Save_folder_structure_button.grid(row=2, column=1)
    else:
        create_folder_destination_label.config(text="no destination folder selected")
        CreateFolder_Choose_destination_folder_button.config(text="Choose folder")

def removeSourceFile():
    souruce_file_path.set("")
    source_file_label.config(text="no source file selected")
    Choose_source_file_button.config(text="Choose file")
    Remove_source_file_button.grid_forget()
    Export_folder_button.grid_forget()

def removeTargetFolder():
    destination_folder_Path.set("")
    create_folder_destination_label.config(text="no destination folder selected")
    CreateFolder_Choose_destination_folder_button.config(text="Choose folder")
    CreateFolder_Remove_destiination_folder_button.grid_forget()
    Create_folder_structure_button.grid_forget()
    Save_folder_structure_button.grid_forget()

root = Tk()
root.title("Directory structure creator")
tabControl = ttk.Notebook(root)

ExtractFolderFrame = Frame(tabControl)
CreateFolderFrame = Frame(tabControl)

source_folder_Path = StringVar(ExtractFolderFrame)
destination_folder_Path = StringVar(ExtractFolderFrame)
souruce_file_path = StringVar(CreateFolderFrame)

source_folder_label = Label(ExtractFolderFrame, text="No source folder selected")
source_folder_label.grid(row=0,column=0)
source_file_label = Label(CreateFolderFrame, text="No structure file selected")
source_file_label.grid(row=0,column=0)
destination_folder_label = Label(ExtractFolderFrame, text="No destination folder selected")
destination_folder_label.grid(row=1,column=0)
create_folder_destination_label = Label(CreateFolderFrame, text="No destination folder selected")
create_folder_destination_label.grid(row=1,column=0)
Choose_source_folder_button = Button(ExtractFolderFrame,text="Choose folder", command=setSourceFolder)
Choose_source_folder_button.grid(row=0,column=1)
Choose_source_file_button = Button(CreateFolderFrame,text="Choose file", command=setSourceFile)
Choose_source_file_button.grid(row=0,column=1)
Choose_destination_folder_button = Button(ExtractFolderFrame,text="Choose folder", command=setDestinationFolder)
Choose_destination_folder_button.grid(row=1,column=1)
CreateFolder_Choose_destination_folder_button = Button(CreateFolderFrame,text="Choose folder", command=setTargetFolder)
CreateFolder_Choose_destination_folder_button.grid(row=1,column=1)

Remove_source_folder_button = Button(ExtractFolderFrame,text="Remove folder", command=removeSourceFolder)
Remove_source_file_button = Button(CreateFolderFrame,text="Remove file", command=removeSourceFile)
Remove_destiination_folder_button = Button(ExtractFolderFrame,text="Remove folder", command=removeDestinationFolder)
CreateFolder_Remove_destiination_folder_button = Button(CreateFolderFrame,text="Remove folder", command=removeTargetFolder)

Export_folder_button = Button(ExtractFolderFrame,text="Export folder", command=exportFolder)
Create_folder_structure_button = Button(CreateFolderFrame,text="Create folder structure", command=createFolderStructure)
Save_folder_structure_button = Button(CreateFolderFrame,text="Save folder structure", command=saveFolderStructure)

tabControl.add(ExtractFolderFrame, text = "Extract folder")
tabControl.add(CreateFolderFrame, text = "Create foldor structure")
tabControl.pack()

root.mainloop()