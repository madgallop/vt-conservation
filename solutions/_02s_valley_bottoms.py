#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  name:        _02_valley_bottoms.py
#  purpose:     Classify landforms with geomorphons and isolate valley bottoms.
#
#  author:      Jeff Howarth
#  update:      04/20/2023
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
starts = root+"/inputs/" 

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Required datasets:
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Point to directory where you hold input data. 
# The 'midd' DEM is relatively small and good for testing. 

dem = starts+"DEM_10m_midd.tif"  
lf = keeps+"_0101_landforms.tif"
lc = starts+"LCHP_1m_Midd.tif"

# ==============================================================================
# WORKFLOW
# ==============================================================================

# ------------------------------------------------------------------------------
# Extract lowlands from DEM.
# ------------------------------------------------------------------------------

# Threshold landform class to isolate valley bottoms. 
 
wbt.greater_than(
  input1 = lf, 
  input2 = 7,
  output = temps+"_0202_valley_bottoms.tif",
  incl_equals=True
)

# Remove noise by taking majority class within neighborhood kernel filter.

wbt.majority_filter(
    i = temps+"_0202_valley_bottoms.tif", 
    output = temps+"_0203_valley_bottoms_smoothed.tif",
    filterx=5,
    filtery=5
  )

# Clump valley bottoms into distinct objects. 

wbt.clump(
    i = temps+"_0203_valley_bottoms_smoothed.tif", 
    output = keeps+"_0204_valley_bottoms_smoothed_objects.tif", 
    diag=True, 
    zero_back=True
)

# ------------------------------------------------------------------------------
# Remove developed land cover from valley bottoms. 
# ------------------------------------------------------------------------------

# Resample lc to match valley cell size. 

wbt.resample(
    inputs = lc, 
    output = temps+"_0211_resample_lc.tif", 
    cell_size = None, 
    base = dem, 
    method = "nn"
)

# Reclassify lc to make developed land eraser.

wbt.reclass(
    i = temps+"_0211_resample_lc.tif", 
    output = temps+"_0212_dev_eraser.tif", 
    reclass_vals = "1;1;1;2;1;3;1;4;0;5;0;6;0;7;0;8;0;9;0;10", 
    assign_mode=True
)

# Erase developed land from valley bottoms.  

wbt.multiply(
    input1 = temps+"_0212_dev_eraser.tif", 
    input2 = keeps+"_0204_valley_bottoms_smoothed_objects.tif", 
    output = temps+"_0213_valleys_not_developed.tif", 
)

# Re-clump undeveloped lowlands to identify individual objects. 

wbt.clump(
    i = temps+"_0213_valleys_not_developed.tif", 
    output = keeps+"_0214_valleys_not_developed_clumps.tif", 
    diag=True, 
    zero_back=True
)

# Mask background.

wbt.set_nodata_value(
    i = keeps+"_0214_valleys_not_developed_clumps.tif", 
    output = keeps+"_0215_valleys_not_developed_clumps_bg_masked.tif", 
    back_value=0.0,
)
