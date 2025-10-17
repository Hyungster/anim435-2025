import os
import argparse
import maya.standalone
maya.standalone.initialize()
import maya.cmds as cmds

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

#Places spheres of radius 1 on all transforms containing the -n name. The main functionality.
def placeSpheres(p_name):
    p_name
    
    selection = cmds.polySphere(radius=1)
    placeholders = getAllPlaceholders(p_name)
    
    if not placeholders:
        print(f"No transforms named '{p_name}' found.")
        
    elif selection:
        duplicateds = []
        for p in placeholders:
            position = cmds.xform(p, query=True, translation=True, worldSpace=True)
            duplicateds.append(duplicateSelectedTo(selection[0], position))
            
        group = cmds.createNode('transform', name='DuplicatedObjects')

        for d in duplicateds:
            cmds.parent(d, group, relative=False)
        
        print(f"Duplicated into '{group}'.")
        
    else:
        print("No object selected.")
    
#Returns all transforms in the scene containing 'name' in name.
#Params:
    #name = string to check for in transforms' names
def getAllPlaceholders(name='placeholder'):
    transforms = cmds.ls(type='transform')
    index = 0
    while index < len(transforms):
        if name in transforms[index]:
            index += 1
        else:
            transforms.pop(index)
    print(transforms)
    return transforms
    
#Duplicates an object to a given world position and returns it.
#Params:
    #selection = object to duplicate
    #position = position to dupliate to
def duplicateSelectedTo(selection, position):
    duplicated = cmds.duplicate(selection)
    cmds.xform(duplicated, translation=position, worldSpace=True)
    return duplicated


#main
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', help="Name of the groups to place the spheres on.")
parser.add_argument('-p', '--path', help="the maya scene to place the spheres in.")
args = parser.parse_args()

print("Sphere Placer initialized.")

path = args.path
placeholder_name = args.name

while (not isMayaBinaryScene(path)):
    path = input("Input the path to the maya scene file you want the spheres to be placed in:")
    if (not isMayaBinaryScene(path)):
        print("Path not valid.")

if (not args.name):
    input("Which transforms should the spheres be placed on?")

cmds.file(path, open=True)

placeSpheres(placeholder_name)
maya.cmds.file(save=True)

print(f"Placed spheres at transforms '{placeholder_name}' and saved.")