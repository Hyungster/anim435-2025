# Easy Camera Presets

## Overview

This script creates a UI that can create cameras from a preset .csv file. Select an appropriately formatted .csv file and select a preset.

## Usage

Copy and paste the python script into the Maya script editor. Run the script.

Click on the '...' button to select a preset file.

Select a preset from the dropdown. Press 'Create Cam' button.

## Preset File Format

A preset .csv file should be formatted as following:

camera,horizontal aperture (mm),vertical aperture (mm),focal length (mm)

For example:

```
ARRI Alexa 65,54.12,25.58,50.0
Blackmagic Ursa 4k,21.12,11.88,32.0
RED Weapon Dragon 6k,30.70,15.80,35.0
Sony Venice,36.0,19.4,70.0
James Webb Space Telescope,6500.0,6500.0,131400.0
```