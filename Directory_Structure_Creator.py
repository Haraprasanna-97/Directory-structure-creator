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
        
    def create_structure(self, Paths = None, destination_folder_path = os.getcwd()):
        List = self.paths
        if Paths is not None:
            List = Paths
        for Path in List:
            if not os.path.exists(os.path.join(destination_folder_path, Path)):
                os.makedirs(os.path.join(destination_folder_path, Path))
        return f"Folder structute created in : {destination_folder_path}"

    @staticmethod
    def export_JSON(Paths, JSON_filepath):
        print(f"From export_JSON {JSON_filepath}")
        with open(JSON_filepath, 'w') as file:
            file.write(json.dumps(Paths))

    @staticmethod
    def export_folder(source_folder_path = os.getcwd(), destination_folder_path = os.getcwd()):
        Paths = []
        for path, subdirs, files in os.walk(source_folder_path):
            for subdir in subdirs:
                Paths.append(os.path.join(os.path.basename(source_folder_path),path[len(source_folder_path) + 1:], subdir))

        folder_name = os.path.basename(source_folder_path)
        save_as = os.path.join(destination_folder_path,f"Structure of {folder_name} folder.json")
        Directory_Structure_Creator.export_JSON(Paths, save_as)
        return f"Folder details saved to {save_as}"

    def save(self, destination_folder_path = os.getcwd()):
        print(f"Inside save func destination_folder_path = {destination_folder_path}")
        filepath, extension = os.path.splitext(self.file_path)
        print(f"Inside save func filepath = {filepath}")
        with open(self.file_path, 'r') as file:
            if extension == ".json":
                Content = json.load(file)
            elif extension == ".txt":
                Content = file.read()

        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")

        Metadata = {
            "Date and time" : date_time,
            "Structure descriptor file path" : self.file_path,
            "Structure descriptor file content" : Content,
            "Paths" : self.paths
        }

        save_as = os.path.join(destination_folder_path, f"{os.path.basename(filepath)} Metadata.json")
        Directory_Structure_Creator.export_JSON(Metadata,save_as)
        print(f"Metadata saved to {save_as}")
    
    # Alternate Constructors
    @classmethod
    def from_JSON(cls, JSON_filepath):
        with open(JSON_filepath, 'r') as file:
            Data = json.load(file)
        return cls(JSON_filepath,Data)
    
    @classmethod
    def from_Metadata(cls,Metadata_file):
        print(f"Metadata file : {Metadata_file}")
        with open(Metadata_file, 'r') as file:
            metadata = json.load(file)
        file_path = metadata["Structure descriptor file path"]
        paths = metadata["Paths"]
        return cls(file_path, paths)

    # Magic methods
    def __str__(self):
        return f"""
        STRUCTURE DETAILS
        File path : {self.file_path}
        Paths : {self.paths}
        """

# Obj = Directory_Structure_Creator(f"{os.getcwd()}\\Structure Modified.txt")
# Obj = Directory_Structure_Creator("Structure Modified.txt")
# Parsed_Data = Obj.parse_File()
# Obj.create_structure()
# print(Parsed_Data)
# Obj.save()

# Directory_Structure_Creator.export_JSON(Parsed_Data,"Structure Modified.json")

# Obj2 = Directory_Structure_Creator.from_JSON("Structure Modified.json")
# Obj2.create_structure()
# Obj2.save()

# print(type(Obj2))
# print(Obj2.file_path)
# print(Obj2.paths)

# Obj3 = Directory_Structure_Creator.from_Metadata(f"{os.getcwd()}\\Structure Modified Metadata.json")

# Obj3 = Directory_Structure_Creator.from_Metadata("Structure Modified Metadata.json")
# Obj3.create_structure()
# print(Obj)
# Obj3 = Directory_Structure_Creator.from_Metadata("Structure Modified Metadata.json")
# print(Obj3)
# Directory_Structure_Creator.export_folder("C:\\Users\\harap\\Music\\Gana")
# Directory_Structure_Creator.export_folder()
# print(Obj3)
    
# Obj4 = Directory_Structure_Creator.from_JSON("Structure of Directory structure creator folder.json")
# print(Obj4)
# Obj4.create_structure()

# Final_Obj = Directory_Structure_Creator.from_JSON("Structure of Gana folder.json")
# print(Obj4)
# Final_Obj.create_structure()