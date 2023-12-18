import os
def create_structure(file_path):
    Paths = []
    Content = None
    with open(file_path,"r") as file:
        Content = file.read().split("\n")
    
    for text in Content:
        Paths.append(text.split(" > "))

    for Path in Paths:
        Route = "/".join(Path)
        if not os.path.exists(Route):
            os.makedirs(Route)
    print(f"Folder structute created in : {os.getcwd()}")
        
create_structure("Structure.txt")