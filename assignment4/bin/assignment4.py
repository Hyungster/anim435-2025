import os
import maya.cmds as cmds
import maya.standalone

#Checks if the given path is a maya binary scene file.
#Params:
    #path = path to check
#Returns a boolean indicating whether the path is a maya binary scene file.
def isMayaBinaryScene(path):
    if (not path): 
        print("None type received.")
        return False
    name, extension = os.path.splitext(path)
    return (os.path.isfile(path) and extension == ".mb")

#main
maya.standalone.initialize()

#get the environment variables
root_folder = os.getenv("ROOT")
asset_type = os.getenv("ASSETTYPE").lower()
asset_name = os.getenv("ASSETNAME").lower()

#put together the paths
full_path = rf"{root_folder}\{asset_name}\{asset_type}.mb"
asset_path = rf"{root_folder}\{asset_name}"

#make the folder if it doesn't exist
os.makedirs(asset_path, exist_ok=True)

#make and open or just open the file
if (isMayaBinaryScene(full_path)):
    os.system(rf"maya -file {full_path}")
else:
    cmds.file(new=True)
    cmds.file(rename=full_path)
    cmds.file(save=True)
    os.system(rf"maya -file {full_path}")