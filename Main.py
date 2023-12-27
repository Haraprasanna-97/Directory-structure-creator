import os

def parseFile(file_path):
    Routs = []
    with open(file_path,"r") as file:
        while True:
            Content = file.readline().split("\n")[0]
            if "-" in Content:
                Start = Content.split("-")[0].split(":")[-1]
                End = Content.split("-")[-1]
                # print(Start,End)
                if Start.isnumeric() and End.isnumeric():
                    for i in range(int(Start),int(End)+1):
                        # print(i)
                        Routs.append("/".join(Content.split(" > ")).replace(f":{Start}-{End}",f" {i}"))
            else:
                Routs.append("/".join(Content.split(" > ")))
            if not Content:
                break
    Routs.pop(-1)
    return Routs
    # print(Routs)
    
def create_structure(Paths):
    for Path in Paths:
        if not os.path.exists(Path):
            os.makedirs(Path)
    print(f"Folder structute created in : {os.getcwd()}")
        
Parsed_Data = parseFile("Structure.txt")
create_structure(Parsed_Data)