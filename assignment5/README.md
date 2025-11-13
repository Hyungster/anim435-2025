# Custom File Hierarchy Maker

## Overview

This script creates and opens a new Maya scene in a subfolder of \assetname\assettype. If the file already exists, opens the file instead.

## Usage

Set the following environment variables in the shell:

```shell
export ROOT = "path to the folder you want this file to save in"
export ASSETNAME = "name of the asset being worked on"
export ASSETTYPE = "type of this asset being worked on"
```
Then execute this script:

```shell
$ mayapy /path-to/assignment5.py
```

```shell
#example usage in shell
export ROOT = "/c/Users/hyung/Desktop/TestFolder"
export ASSETNAME = "Monster"
export ASSETTYPE = "Model"
cd /path-to-script
mayapy assignment5.py
```