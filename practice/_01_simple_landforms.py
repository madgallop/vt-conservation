#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  name:     simple_landforms.py
#  purpose:  Classify landforms from a DEM.
#
#  author:   Jeff Howarth
#  update:   04/07/2023
#  license:  Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# import tools from WBT module

import sys
sys.path.insert(1, '/Users/jhowarth/tools')     # path points to my WBT directory
from WBT.whitebox_tools import WhiteboxTools

# declare a name for the tools

wbt = WhiteboxTools()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Working directories
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

out = "/Volumes/drosera/data/midd/wb_layers/"    # path points to folder for storing good outputs
temp = "/Volumes/drosera/data/midd/wb_temp/"     # path points to a folder for storing intermediary outputs

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Required datasets:
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Imported datasets

dem = "/Volumes/drosera/data/midd/ee/DEM_10m.tif"   # path points to data inputs

# ------------------------------------------------------------------------------
# IMPLEMENT
# ------------------------------------------------------------------------------

# Classify landforms from DEM with geomorphons. 
# See WBT manual for parameter definitions.

wbt.geomorphons(
    dem = dem, 
    output = out+"_landforms.tif", 
    search=50, 
    threshold=0.0, 
    fdist=0, 
    forms=True      
    )