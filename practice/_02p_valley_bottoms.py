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
lc = starts+"LCHP_1m_Midd.tif"

# ==============================================================================
# IMPLEMENT
# ==============================================================================

# ------------------------------------------------------------------------------
# Extract lowlands from DEM.
# ------------------------------------------------------------------------------

# Classify landforms from DEM with geomorphons. 
# See WBT manual for parameter definitions.


# Threshold landform class to isolate valley bottoms. 
 


# Remove noise by taking majority class within neighborhood kernel filter.



# Clump valley bottoms into distinct objects. 



# ------------------------------------------------------------------------------
# Remove developed land cover from valley bottoms. 
# ------------------------------------------------------------------------------

# Resample lc to match valley cell size. 



# Reclassify lc to make developed land eraser.



# Erase developed land from valley bottoms.  



# Re-clump undeveloped lowlands to identify individual objects. 



# ------------------------------------------------------------------------------
# Make copies of output with background masked and background 0.
# ------------------------------------------------------------------------------

# Mask background.



# Convert background to zero. 

