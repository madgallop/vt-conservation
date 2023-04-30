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

wbt.resample(
    inputs = lc, 
    output = temps+"_0501_resample_lc.tif", 
    cell_size = None, 
    base = links, 
    method = "nn"
)

# Reclassify friction values from land cover classes. 

wbt.reclass(
    i = temps+"_0501_resample_lc.tif", 
    output = temps+"_0502_friction.tif", 
    reclass_vals = "1;1;3;2;5;3;5;4;10;5;10;6;10;7;10;8;10;9;10;10", 
    assign_mode=True
)

# ------------------------------------------------------------------------------
# Create source layer from blocks. 
# ------------------------------------------------------------------------------

# Unmask the background (convert nodata to zero).

wbt.convert_nodata_to_zero(
    i = blocks, 
    output = temps+"_0511_blocks_bg0.tif"
)

# Resample to mama. 

wbt.resample(
    inputs = temps+"_0511_blocks_bg0.tif", 
    output = temps+"_0512_resample_blocks.tif", 
    cell_size = None, 
    base = links, 
    method = "nn"
)

# ------------------------------------------------------------------------------
# Calculate cost distance
# ------------------------------------------------------------------------------ 

wbt.cost_distance(
    source = temps+"_0512_resample_blocks.tif", 
    cost = temps+"_0502_friction.tif", 
    out_accum = keeps+"_0521_cost_accumulation.tif", 
    out_backlink = keeps+"_0522_cost_backlink.tif", 
)

# ------------------------------------------------------------------------------
# Constrain friction to valley bottom corridors. 
# ------------------------------------------------------------------------------ 

# Mask the background. 

wbt.set_nodata_value(
    i = links, 
    output = temps+"_0532_lowlands_binary_bg_masked.tif", 
    back_value=0.0, 
)

# Mask not-valley background from friction layer. 

wbt.multiply(
    input1 = temps+"_0502_friction.tif", 
    input2 = temps+"_0532_lowlands_binary_bg_masked.tif", 
    output = temps+"_0533_friction_valleys_only.tif", 
)

# Calculate cost distance. 

wbt.cost_distance(
    source = temps+"_0512_resample_blocks.tif", 
    cost = temps+"_0533_friction_valleys_only.tif", 
    out_accum = keeps+"_0534_cost_accumulation_valleys_only.tif", 
    out_backlink = keeps+"_0535_cost_backlink_valleys_only.tif", 
)
