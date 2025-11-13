import os
import maya.utils as utils
import maya.cmds as cmds
import maya.standalone

import logging
logger = logging.getLogger(__name__)

FORMAT = "[%(asctime)s][%(filename)s][%(lineno)d][%(levelname)s] %(msg)s"
logging.basicConfig(filename='log.txt',
                    level=logging.INFO, 
                    format=FORMAT)

 


#Checks if the given path is a maya binary scene file.
#Params:
    #path = path to check
#Returns a boolean indicating whether the path is a maya binary scene file.
def isMayaBinaryScene(path):
    if (not path): 
        logger.warning('The path given to check is void. Please make sure the environmental variables ' \
        'ROOT, ASSETNAME, and ASSETTYPE are assigned in the shell.')
        return False
    name, extension = os.path.splitext(path)
    return (os.path.isfile(path) and extension == ".mb")

    

#main
maya.standalone.initialize()

#get the environment variables
root_folder = os.getenv("ROOT")
asset_name = os.getenv("ASSETNAME")
asset_type = os.getenv("ASSETTYPE")

should_quit = False

if (not root_folder):
    logger.error("The environment variable ROOT is void. Please set it in shell. Terminating.")
    should_quit = True
if (not asset_name):
    logger.error("The environment variable ASSETNAME is void. Please set it in shell. Terminating.")
    should_quit = True
if (not asset_type):
    logger.error("The environment variable ASSETTYPE is void. Please set it in shell. Terminating.")
    should_quit = True
if (should_quit):
    quit()

asset_name = asset_name.lower()
asset_type = asset_type.lower()


#put together the paths
#full_path = rf"{root_folder}\{asset_name}\{asset_type}.mb"
full_path = os.path.join(root_folder, asset_name, asset_type + ".mb")
asset_path = os.path.join(root_folder, asset_name)

#make the folder if it doesn't exist
os.makedirs(asset_path, exist_ok=True)

#make and open or just open the file
if (isMayaBinaryScene(full_path)):
    logger.info("Maya file already exists. Opening in Maya.")
    os.system(rf"maya -file {full_path}")
else:
    logger.info("Maya file not found. Creating a new scene.")
    cmds.file(new=True)
    cmds.file(rename=full_path)
    cmds.file(save=True)
    os.system(rf"maya -file {full_path}")