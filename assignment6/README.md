# Custom File Hierarchy Maker

## Overview

This script creates and opens a new Maya scene in a subfolder of /assetname/assettype. If the file already exists, opens the file instead. 

Check the log.txt in /assignment6/bin for logs.

Creates a .json metadata file with the name of the asset type in the same directory as the Maya scene file.

## Usage

Set the following environment variables in the shell:

```shell
export ROOT = "path to the folder you want this file to save in"
export ASSETNAME = "name of the asset being worked on"
export ASSETTYPE = "type of this asset being worked on"
```
Then execute this script:

```shell
$ mayapy /path-to/assignment6.py
```

```shell
#example usage in shell
export ROOT = "/c/Users/hyung/Desktop/TestFolder"
export ASSETNAME = "Monster"
export ASSETTYPE = "Model"
cd /path-to-script
mayapy assignment6.py
```