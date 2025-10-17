# Sphere On Placeholders Tool

## Overview

This script places polyspheres at the positions of placeholder groups. The spheres are parented under a new group for organization. This may be useful for a set modeling scenario where some pieces are meant to go in predetermined locations.


## Usage

```python
sphere-on-placeholders
    -p <path> #the maya scene to place spheres in
    -n <name> #the name of the transforms to place spheres on

mayapy assignment3.py --path 'example-path.mb' --name 'door'
```