from datetime import datetime
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
        print(f"Folder structute created in : {os.getcwd()}")

    @staticmethod
    def export_JSON(Paths, JSON_filepath):
        with open(JSON_filepath, 'w') as file:
            file.write(json.dumps(Paths))
    
    # Alternate Constructors
    @classmethod
    def from_JSON(cls, JSON_filepath):
        with open(JSON_filepath, 'r') as file:
            Data = json.load(file)
        return cls(JSON_filepath,Data)
    
    def save(self):
        filepath, extension = os.path.splitext(self.file_path)
        with open(self.file_path, 'r') as file:
            if extension == ".json":
                Content = json.load(file)
            elif extension == ".txt":
                Content = file.read()

        now = datetime.now()

        Metadata = {
            "Date and time" : now.strftime("%Y-%m-%d %H:%M:%S"),
            "Structure descriptor file path" : self.file_path,
            "Structure descriptor file content" : Content,
            "Paths" : self.paths
        }

        save_as = f"{filepath} Metadata.json"
        Directory_Structure_Creator.export_JSON(Metadata,save_as)
        print(f"State saved to {save_as}")

Obj = Directory_Structure_Creator("Structure Modified.txt")
Parsed_Data = Obj.parse_File()
# Obj.create_structure()
# print(Parsed_Data)
Obj.save()

# Directory_Structure_Creator.export_JSON(Parsed_Data,"Structure Modified.json")
# Obj2 = Directory_Structure_Creator.from_JSON("Structure Modified.json")
# Obj2.create_structure()
# Obj2.save()

# print(type(Obj2))
# print(Obj2.file_path)
# print(Obj2.paths)