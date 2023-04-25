#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  name:        _05_corridor_friction.py
#  purpose:     Identify friction and cost distance between habitat blocks.
#
#  author:      Jeff Howarth
#  update:      04/24/2023
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
# Links are the valley corridors that connect two or more habitat blocks. 

links = keeps+"_0426_valley_corridors_not_developed_blocks_gte_XX_acres.tif" 
blocks = keeps+"_0356_forested_habitat_blocks_gte_XX_acres_objects.tif"
lc = root+"/inputs/LCHP_1m_midd.tif"  

# ==============================================================================
# WORKFLOW
# ==============================================================================

# ------------------------------------------------------------------------------
# Create friction surface from land cover.  
# ------------------------------------------------------------------------------

# Resample land cover to match a mama raster. 



# Reclassify friction values from land cover classes. 



# ------------------------------------------------------------------------------
# Create source layer from blocks.
# ------------------------------------------------------------------------------

# Unmask the background (convert nodata to zero).



# Resample to mama. 



# ------------------------------------------------------------------------------
# Calculate cost distance
# ------------------------------------------------------------------------------ 


# ------------------------------------------------------------------------------
# Constrain friction to valley bottom corridors. 
# ------------------------------------------------------------------------------ 

# Mask the background of links. 


# Erase not-valley background from friction layer. 



# Calculate cost distance. 


