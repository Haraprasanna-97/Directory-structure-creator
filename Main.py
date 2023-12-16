import os
def create_structure(file_path):
    Paths = []
    Content = None
    with open(file_path,"r") as file:
        Content = file.read().split("\n")
    
    for text in Content:
        Paths.append(text.split())

    for Path in Paths:
        print("/".join(Path))
        os.makedirs("/".join(Path))
        
create_structure("Structure.txt")