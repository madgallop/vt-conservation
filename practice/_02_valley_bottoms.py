#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  name:        _02_valley_bottoms.py
#  purpose:     Resample a high resolution DEM, classify landforms with geomorphons, 
#               and isolate valley bottoms.
#
#  author:      Jeff Howarth
#  update:      04/07/2023
#  license:     Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
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

dem = "/Volumes/drosera/data/midd/ee/DEM_1m.tif"   # path points to data inputs

# ------------------------------------------------------------------------------
# IMPLEMENT
# ------------------------------------------------------------------------------

# Resample high resolution DEM to decrease resolution.

wbt.resample(
 inputs = dem, 
 output = temp+"_01_resample.tif", 
 cell_size = 3, 
#  base=dem, 
 method = "cc"
 )

# Classify landforms from DEM with geomorphons. 
# See WBT manual for parameter definitions.

wbt.geomorphons(
    dem = dem, 
    output = temp+"_02_landforms.tif", 
    search=50, 
    threshold=0.0, 
    fdist=0, 
    forms=True      
    )

# Reclassify landforms to isolate valley bottoms. 

 wbt.greater_than(
  input1 = temp+"_02_landforms.tif", 
  input2 = 9,
  output = out+"valley_bottoms.tif",
  incl_equals=True
)

#  # reduce noise by taking majority class within 50 feet

#     wbt.majority_filter(i = "_01.tif", output = data_repo+"_lowlands.tif",filterx=11,filtery=11)
