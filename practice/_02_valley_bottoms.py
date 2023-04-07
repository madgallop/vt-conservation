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

# Define personal storage root.
# This is the path where you will store inputs and outputs from this workflow.
# For example, my root points to the directory (folder) of s23 in GEOG0310 
# on an external drive named drosera. 

root = "/Volumes/drosera/GEOG0310/s23"

# Set up separate directories to store temporary and keeper outputs. 

temp = root+"/wb_temp/"     
keep = root+"/wb_layers/"   

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Required datasets:
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Point to directory where you hold input data. 

dem =root+"/ee/DEM_10m.tif"  

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

# Threshold landform class to isolate valley bottoms. 

 wbt.greater_than(
  input1 = temp+"_02_landforms.tif", 
  input2 = 9,
  output = keep+"valley_bottoms.tif",
  incl_equals=True
)

 # Reduce noise by taking majority class within neighborhood.

  wbt.majority_filter(
  i = "valley_bottoms.tif",
  output = keep+"valley_bottoms_majority.tif",
  filterx=11,
  filtery=11
  )