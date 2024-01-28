import os

class Structure_Creator:
    def __init__(self,file_path):
        self.file_path = file_path
        self.paths = None

    def parseFile(self):
        Routs = []
        with open(self.file_path,"r") as file:
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
                    # elif not Start.isnumeric():
                    #     print(Start)
                    # elif not End.isnumeric():
                    #     print(End)
                else:
                    Routs.append("/".join(Content.split(" > ")))
                if not Content:
                    break
        Routs.pop(-1)
        self.paths = Routs
        return Routs
        # print(Routs)
        
    def create_structure(self, Paths = None):
        if Paths is None:
            for Path in self.paths:
                if not os.path.exists(Path):
                    os.makedirs(Path)
        else:
            for Path in Paths:
                if not os.path.exists(Path):
                    os.makedirs(Path)
        print(f"Folder structute created in : {os.getcwd()}")

Obj = Structure_Creator("Structure.txt")
Parsed_Data = Obj.parseFile()
Obj.create_structure()
print(Parsed_Data)