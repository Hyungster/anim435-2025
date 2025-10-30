import maya.cmds as cmds
import os
import csv

#Holds the camera options in a (string, float[]) dictionary.
camera_presets = {}

#Pops up a file dialog to get a .csv file.
#Returns: 
#   a string path of the selected .csv file
def get_preset_path():
    path = cmds.fileDialog2(fileFilter="*.csv", dialogStyle=2, fileMode=1, okCaption="Accept")
    path = "".join(path)
    cmds.text(text_csv_path, edit=True, label=path)
    return path

#Reads the .csv file from the given path. Parses the results into a (string, float[]) dictionary.
#Params:
#   filepath: string path to the .csv file 
def parse_preset_csv(filepath):
    if (not os.path.isfile(filepath)):
        cmds.text(path_validity, edit=True, label="The given .csv filepath is not valid.")
        return
    else:
        cmds.text(path_validity, edit=True, label="The given .csv filepath is valid.")
        
    #clear presets
    global camera_presets 
    camera_presets = {}

    with open(filepath, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if (not len(row) == 4):
                continue
            parse_preset_row(row)
    
    csvfile.close()

#Receives an array of strings and tries to append them to camera_presets as (string, float[]) pair.
#Params:
#   row: string[4] read from a single row in the .csv file in parse_preset_csv
def parse_preset_row(row):
    camera_name = ""
    camera_params = []

    for i in range(4):
        if (i == 0):
            camera_name = row[0]
        else:
            try:
                value = float(row[i])
                camera_params.append(value)
            except(ValueError):
                return
    global camera_presets
    camera_presets[camera_name] = camera_params

#Adds a camera preset option to camera_presets.
#Params:
#   option: a string name of the camera preset
def add_option(option):
    cmds.menuItem(label=option, parent=preset_options)

#Deletes all menuItem UI from the optionMenu.
def clear_options():
    menuItems = cmds.optionMenu(preset_options, q=True, itemListLong=True)
    if menuItems:
        cmds.deleteUI(menuItems)

#Encasing function for getting preset file path, parsing it, and generating options UI.
def get_presets(*args):
    path = get_preset_path()
    parse_preset_csv(path)
    clear_options()
    for preset in camera_presets:
        add_option(preset)

#Creates a camera based on the currently selected option. Returns if there is no valid option.
def create_cam(*args):
    menuItems = cmds.optionMenu(preset_options, q=True, itemListLong=True)
    if not menuItems:
        return

    cam_name = cmds.optionMenu(preset_options, query=True, value=True)
    print("Camera nane: " + cam_name)
    values = camera_presets[cam_name]
    print(values)
    
    cam = cmds.camera(name=cam_name)
    cmds.setAttr(f'{cam[1]}.horizontalFilmAperture', milimeters_to_inches(values[0]))
    cmds.setAttr(f'{cam[1]}.verticalFilmAperture', milimeters_to_inches(values[1]))
    cmds.setAttr(f'{cam[1]}.focalLength', milimeters_to_inches(values[2]))

def milimeters_to_inches(value):
    return value * 0.0393701

# Easy Camera Preset UI layout
# ----------------------------
# 1 [Path:] [selected path] [file dialogue button]
# 2 [path valid feedback text]
# 3 [Preset:] [Dropdown for options] [create camera button]

win = cmds.window("Easy Camera Preset", height=100, width=500)

#primary column
column = cmds.columnLayout(adjustableColumn=True)

#1, path to the .csv file
row_csv_path = cmds.rowLayout(numberOfColumns=3, parent=column)
cmds.text(label="Preset .csv:")
text_csv_path = cmds.text(label="select your .csv file -->", width=400, backgroundColor=[0.2, 0.2, 0.2])
button_csv_path = cmds.button(label="...", command=get_presets)

#2, feedback on .csv path validity
path_validity = cmds.text(label="", parent=column)

#3, pick and use camera preset
row_preset = cmds.rowLayout(numberOfColumns=3, parent=column)
preset_options = cmds.optionMenu(label="Camera Preset:")
button_create_cam = cmds.button(label="Create Cam", command=create_cam)

cmds.showWindow(win)