import os
import json

class Directory_Structure_Creator:
    def __init__(self,file_path, paths = None):
        self.file_path = file_path
        self.paths = paths

    def parse_File(self):
        Routs = []
        with open(self.file_path,"r") as file:
            while True:
                Content = file.readline().split("\n")[0]
                if "-" in Content:
                    Start = Content.split("-")[0].split(":")[-1]
                    End = Content.split("-")[-1]
                    if Start.isnumeric() and End.isnumeric():
                        for i in range(int(Start),int(End)+1):
                            Routs.append("/".join(Content.split(" > ")).replace(f":{Start}-{End}",f" {i}"))
                else:
                    Routs.append("/".join(Content.split(" > ")))
                if not Content:
                    break
        Routs.pop(-1)
        self.paths = Routs
        return Routs
        
    def create_structure(self, Paths = None):
        List = self.paths
        if Paths is not None:
            List = Paths
        for Path in List:
            if not os.path.exists(Path):
                os.makedirs(Path)
        # else:
        #     for Path in Paths:
        #         if not os.path.exists(Path):
        #             os.makedirs(Path)
        print(f"Folder structute created in : {os.getcwd()}")

    @staticmethod
    def export_JSON(Paths, JSON_filepath):
        with open(JSON_filepath, 'w') as file:
            file.write(json.dumps(Paths))
    
    # Alternative Constructors
    @classmethod
    def from_JSON(cls, JSON_filepath):
        with open(JSON_filepath, 'r') as file:
            Data = json.load(file)
        return cls(JSON_filepath,Data)

Obj = Structure_Creator("Structure Modified.txt")
Parsed_Data = Obj.parseFile()
# Obj.create_structure()
# print(Parsed_Data)

# Structure_Creator.export_JSON(Parsed_Data,"Structure Modified.json")
Obj2 = Structure_Creator.from_JSON("Structure Modified.json")
Obj2.create_structure()

print(type(Obj2))
print(type(Obj2.file_path))
print(type(Obj2.paths))