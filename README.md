# Description

This aplication creates a directory structure as described in text file

# Requrement

You need to have Python programming language to run this applicatiom . This is a temporary solution

# How to use

1. Place the `main.py` file in the folder you want to create a directory structure in.
2. Create a text file in the same folder. The name of this taext file must be `Structure.txt`. This text file defines the paths in your directory structure.
3. Open the terminal in the same folder where you want to create a directory structure in and run the following command.

```
python Main.py
```

## How to describe folder structuture ?

### Text file

To describe a folder structure, use the following format

```
[Root folder Name] > [Sub-Folder name] > [Sub-Sub-Folder name] ....
```

1. The above format is for each line of your text file.
2. There should be a root folder on each line
3. It is otional to have sub-folders in the root folder
4. There is no limit in the number of root folders and sub folders you can have
5. To define a sequence of folders such as `Sub folder 1, Sub folder 2 ... Sub folder n` inside a single folder,  use the following format
   ```
   [Folder Name]:[Sequence start number]-[Sequence end number]
   ```

Folowing is an example of a structure file

```
A > B > C
A > D
A > E > F
G
```

In the above example,

* A and G are root folders
* B, D and E are sub-foldera under A
* C is a sub-folder under B, and F is a sub-folder under aE, hense C and E are sub-sub folder

### JSON file

To describe folder structure, use the following format

```json
[
    "A/B/C",
    "A/D/D/g",
    "A/D/D/g/H",
    "A/E/F",
    "G"
]
```

In the above example,

* there is a list of comma separated paths enclosed within square brackets (`[]`)
* The path is structured as

```
[Root folder Name]/[Sub-Folder name]/[Sub-Sub-Folder name] ....
```

* The folder name can have of one or more words sepsrated by spareted by space
* The folder names are separeted by slash `/`

### Using Graphical User Interface (GUI)

* You can export a folder structure as a JSON file. You can alao create a folder structure by specifying the structure file and the destination where the fokder structure needs to be created
* To access the GUI run the following command
  ```
  python GUI.py
  ```

### Using terninal app

* By using the terminal app, you can create a folder structure specifing structure file
* To run the terminal app, use the command

  ```
  python Termnal app.py <Options>
  ```

## Structure file key for text file

| Symbol | Meaning             | Uaage example | Usage meaning                                        |
| :----: | ------------------- | ------------- | ---------------------------------------------------- |
|   >   | Inside              | A > B         | Folder B is inside folder A                         |
|   :   | Sequence of folders | A:1-4         | Define a set of folders such as A 1, A 2, A 3, A 4 |

## Functions of Directory_Structure_Creator class

| Function           | Description                                                                                                                                           |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| parse_file()       | Reads the structure file given as input and creates a list of roures                                                                                  |
| create_structure() | Creates the actual directory structure by using either the list of paths generated by parseFile() function or the list of paths passed as argument |
| export_JSON()      | Exports the list of paths as a json file                                                                                                              |
| export_folder()    | Exports a folder structure as JSON File                                                                                                               |
| from_JSON()        | Reads a json file and creates an object of the Directory_Structure_Creator class which can be used layter to create the directory structure          |
| from_Metadata()    | Reads a metadata file and creates an object of the Directory_Structure_Creator class which can be used layter to create the directory structure      |
| save()             | Saves the metadata of the current object as a JSON file                                                                                               |

## Options for terminal app

| Option        | Optiomal / Required | Descrioption                                                             |
| ------------- | ------------------- | ------------------------------------------------------------------------ |
| -h, --help    | Optonal             | Show the help text                                                       |
| --saveas      | Optional            | Specify the folder where the metadatais to be save                       |
| structurefile | Required            | Specify the location of the file where the folder structure is described |
| dest          | Required            | Specify the folder where the structure is to be created                  |
