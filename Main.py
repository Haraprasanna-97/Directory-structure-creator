import os

def parseFile(file_path):
    Routs = []
    with open(file_path,"r") as file:
        while True:
            Content = file.readline().split("\n")[0]
            Routs.append("/".join(Content.split(" > ")))
            if not Content:
                break
    Routs.pop(-1)
    return Routs
    
def create_structure(Paths):
    for Path in Paths:
        if not os.path.exists(Path):
            os.makedirs(Path)
    print(f"Folder structute created in : {os.getcwd()}")
        
Parsed_Data = parseFile("Structure.txt")
create_structure(Parsed_Data)