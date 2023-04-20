#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  name:        _04_select_valley_corridors.py
#  purpose:     Identify valley corridors that connect two or more blocks.
#
#  author:      Jeff Howarth
#  update:      04/18/2023
#  license:     Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Access Whitebox tools. 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Point to directory with WBT module.
# Please note: if you have stored this script in the same directory as the WBT folder, 
# then you can comment out lines 14-15.

import sys
sys.path.insert(1, '/Users/jhowarth/tools')     # path points to my WBT directory

# Import tools from WBT module. 

from WBT.whitebox_tools import WhiteboxTools

# Declare a name for the tools.

wbt = WhiteboxTools()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Define working directories to manage outputs. 
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
#  Define the starting input data. 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Point to directory where you hold input data. 

valleys = keeps+"_0204_valley_bottoms_smoothed_objects.tif"  
blocks = temps+"_0343_forested_habitat_blocks.tif"

# ==============================================================================
# WORKFLOW
# ==============================================================================

# ------------------------------------------------------------------------------
# Align images: must be same extent and cell size. 
# ------------------------------------------------------------------------------

# Resample blocks to match valley cell size. 




# ------------------------------------------------------------------------------
# Erase valleys where they overlap blocks. 
# ------------------------------------------------------------------------------

# Convert blocks into an inverse binary. 



# Erase blocks from valley bottoms.  



# Re-clump valley bottoms to identify individual objects. 



# ------------------------------------------------------------------------------
# Identify and remove islands. 
# ------------------------------------------------------------------------------

# Grow valley bottom edge by one pixel.



# Mask background.



# Test for overlap between valley bottoms and habitat blocks.



# Mask islands.  



# Re-clump valley bottoms without islands to identify individual objects. 



# ------------------------------------------------------------------------------
# Select corridors. 
# ------------------------------------------------------------------------------

# Set background of blocks to no data. 



# Test for min of overlap.



# Test for max of overlap.



# Bridges (tombolos) will have unequal min and max values, 
# while piers (spits) will have equal min and max values. 


# Unmask background values. 



# Select valley bottom corridors. 

