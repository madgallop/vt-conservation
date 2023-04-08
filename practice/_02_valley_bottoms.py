#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  name:        _02_valley_bottoms.py
#  purpose:     Classify landforms with geomorphons and isolate valley bottoms.
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

temps = root+"/temps/"     
keeps = root+"/keeps/"   

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Required datasets:
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Point to directory where you hold input data. 

dem =root+"/inputs/DEM_10m.tif"  

# ------------------------------------------------------------------------------
# IMPLEMENT
# ------------------------------------------------------------------------------

# Classify landforms from DEM with geomorphons. 
# See WBT manual for parameter definitions.

wbt.geomorphons(
    dem = dem, 
    output = temps+"_0201_landforms.tif", 
    search=100,              # Adjust search distance based on site terrain and data resolution.
    threshold=0.0,          
    fdist=0,               
    forms=True      
    )

# Threshold landform class to isolate valley bottoms. 
 
wbt.greater_than(
  input1 = temps+"_0201_landforms.tif", 
  input2 = 9,
  output = temps+"_0202_valley_bottoms.tif",
  incl_equals=True
)

# Remove noise by taking majority class within 50 feet (neighborhood filter).

wbt.majority_filter(
    i = temps+"_0202_valley_bottoms.tif", 
    output = keeps+"_0203_valley_bottoms_smoothed.tif",
    filterx=5,
    filtery=5
  )