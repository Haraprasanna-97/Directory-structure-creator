import argparse
parser = argparse.ArgumentParser()
from os import path
from Directory_Structure_Creator import Directory_Structure_Creator

parser.add_argument("structurefile", help="Specify the location of the file where the folder structure is described")
parser.add_argument("dest",help="Specify the folder where the structure is to be created")
parser.add_argument("--saveas", help="Specify the folder where the metadatais to be saved")

args = parser.parse_args()

Structure_File = path.abspath(args.structurefile)
Folder = path.abspath(args.dest)

Filepath, extention = path.splitext(Structure_File)
if extention == ".json":
    if Filepath.endswith("Metadata"):
        Creator = Directory_Structure_Creator.from_Metadata(Structure_File)
        Creator.create_structure()
        print(Creator)
    else:
        Creator = Directory_Structure_Creator.from_JSON(Structure_File)
        Creator.create_structure()
        print(Creator)
        if args.saveas:
            Metadeta_location = path.abspath(args.saveas)
            Creator.save(Metadeta_location)
elif extention == ".txt":
    Creator = Directory_Structure_Creator(Structure_File)
    Creator.create_structure()
    if args.saveas:
        Metadeta_location = path.abspath(args.saveas)
        Creator.save(Metadeta_location)