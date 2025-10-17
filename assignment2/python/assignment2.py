import maya.cmds as cmds
from functools import partial

#main button function
def onButtonPress(*args):
    p_name = cmds.textField(placeholder_name, query=True, text=True)
    
    if p_name == '':
        print("Please type a name to search for.")
        return
    
    selection = cmds.ls(selection=True)
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
win = cmds.window("Duplicate to Placeholders")
layout = cmds.columnLayout()
btn = cmds.button(label="Duplicate", command=partial(onButtonPress), parent=layout)
placeholder_name = cmds.textField(placeholderText="placeholder")
cmds.showWindow(win)