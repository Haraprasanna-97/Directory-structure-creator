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

In the above example

* A and G are root folders
* B, D and E are sub-foldera under A
* C is a sub-folder under B, and F is a sub-folder under aE, hense C and E are sub-sub folder

## 
    Structure file key

| Symbol | Meaning             | Uaage example | Usage meaning                                        |
| ------ | ------------------- | ------------- | ---------------------------------------------------- |
| >      | Inside              | A > B         | Folder B is inside folder A                         |
| :      | Sequence of folders | A:1-4         | Define a set of folders SUCH as A 1, A 2, A 3, A 4 |
