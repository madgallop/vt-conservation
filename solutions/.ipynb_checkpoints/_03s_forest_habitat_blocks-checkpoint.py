#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  name:        _03_forest_habitat_blocks.py
#  purpose:     Classify forest habitat blocks from land cover.
#
#  author:      Jeff Howarth
#  update:      04/08/2023
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
# The 'midd' DEM is relatively small and good for testing. 

lc = root+"/inputs/LCHP_1m_midd.tif"  

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPLEMENT
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ------------------------------------------------------------------------------
# 1. Identify clumps of recovering habitat. 
# ------------------------------------------------------------------------------

# Resample LCHP to 3 meter to speed up pilot. 

wbt.resample(
    inputs = lc, 
    output = temps+"_0301_resample.tif", 
    cell_size = 3, 
    base = None, 
    method = "nn"
)

# Make a binary where recovering habitat = 0 and not recovering habitat = 1.

wbt.reclass(
    i = temps+"_0301_resample.tif", 
    output = temps+"_0302_binary.tif", 
    reclass_vals = "0;1;0;2;0;3;1;4;1;5;1;6;1;7;1;8;1;9;1;10", 
    assign_mode=True
)

# Pass a majority filter over the binary to remove noise from random pixels.  

wbt.majority_filter(
    i = temps+"_0302_binary.tif", 
    output = temps+"_0303_majority_filter.tif", 
    filterx=5, 
    filtery=5
)

# Buffer 50 meters into recovering habitat to identify cores.  
# Because images sometimes lose their crs information, it can be safer to specific distance in cell units. 

wbt.buffer_raster(
    i = temps+"_0303_majority_filter.tif", 
    output = temps+"_0304_buffer.tif", 
    size = 17, 
    gridcells=True
)

# Invert figure and ground.  

wbt.equal_to(
    input1 = temps+"_0304_buffer.tif", 
    input2 = 0, 
    output = temps+"_0305_invert.tif"
)

# Identify clumps of core recovering habitat. 
 
wbt.clump(
    i = temps+"_0305_invert.tif", 
    output = temps+"_0306_habitat_clumps.tif", 
    diag=True, 
    zero_back=True, 
)

# ------------------------------------------------------------------------------
# 2. Identify recovering clumps with a majority of tree canopy. 
# ------------------------------------------------------------------------------

# Compute area of each core recovering habitat clump.

wbt.raster_area(
    i = temps+"_0306_habitat_clumps.tif", 
    output = temps+"_0311_habitat_area.tif", 
    out_text=False, 
    units="grid cells", 
    zero_back=True
)

# Make a binary of tree canopy. 

wbt.reclass(
    i = temps+"_0301_resample.tif", 
    output = temps+"_0312_tree_canopy_binary.tif", 
    reclass_vals = "1;1;0;2;0;3;0;4;0;5;0;6;0;7;0;8;0;9;0;10", 
    assign_mode=True
)

# Count the number of tree canopy pixels in each clump.  

wbt.zonal_statistics(
    i = temps+"_0312_tree_canopy_binary.tif", 
    features = temps+"_0306_habitat_clumps.tif", 
    output = temps+"_0313_zonal_stats.tif", 
    stat="total", 
    out_table=None, 
)

# Divide the count of tree canopy by the pixel area of each clump. 

wbt.divide(
    input1 = temps+"_0313_zonal_stats.tif", 
    input2 = temps+"_0311_habitat_area.tif", 
    output = temps+"_0314_habitat_percent_tree.tif",
)

# Replace background value with zero.

wbt.convert_nodata_to_zero(
    i = temps+"_0314_habitat_percent_tree.tif", 
    output = temps+"_0315_habitat_percent_tree_bg0.tif", 
)

# Threshold habitat blocks by percent tree canopy (> 49%). 

wbt.greater_than(
    input1 = temps+"_0315_habitat_percent_tree_bg0.tif", 
    input2 = 0.49, 
    output = temps+"_0316_habitat_majority_tree.tif", 
    incl_equals=False,
)

# ------------------------------------------------------------------------------
# 3. Identify clumps of tree canopy that overlap blocks          . 
# ------------------------------------------------------------------------------

# Clump tree canopy binary to identify stands of trees. 

wbt.clump(
    i = temps+"_0312_tree_canopy_binary.tif", 
    output = temps+"_0331_tree_canopy_clumps.tif", 
    diag=True, 
    zero_back=True, 
)

# Set background as no data. 

wbt.set_nodata_value(
    i = temps+"_0331_tree_canopy_clumps.tif", 
    output = temps+"_0333_tree_canopy_clumps_bg_nd.tif", 
    back_value=0.0, 
)


# Identify tree stands that overlap habitat blocks with majority trees. 

wbt.zonal_statistics(
    i = temps+"_0316_habitat_majority_tree.tif", 
    features = temps+"_0333_tree_canopy_clumps_bg_nd.tif", 
    output = temps+"_0334_max_habitat_tree.tif", 
    stat="maximum", 
    out_table=None, 
) 

# ------------------------------------------------------------------------------
# 4. Combine habitat blocks with majority of trees and overlapping tree stands.         . 
# ------------------------------------------------------------------------------

# Replace background value with zeros for overlapping tree stands.

wbt.convert_nodata_to_zero(
    i = temps+"_0334_max_habitat_tree.tif", 
    output = temps+"_0341_max_habitat_tree_bg0.tif", 
)

# Union the overlapping tree stands and habitat blocks. 

wbt.Or(
    input1 = temps+"_0316_habitat_majority_tree.tif", 
    input2 = temps+"_0341_max_habitat_tree_bg0.tif", 
    output = temps+"_0342_union.tif", 
)


# Identify individual forested habitat blocks. 

wbt.clump(
    i = temps+"_0342_union.tif", 
    output = temps+"_0343_forested_habitat_blocks.tif", 
    diag=True, 
    zero_back=True
)

# ------------------------------------------------------------------------------
# 5. Classify forested habitat blocks by area. 
# ------------------------------------------------------------------------------

# Set background as no data. 

wbt.set_nodata_value(
    i = temps+"_0343_forested_habitat_blocks.tif", 
    output = temps+"_0351_forested_habitat_blocks_bg_nd.tif", 
    back_value=0.0, 
)

# Compute the area of each block. 

wbt.raster_area(
    i = temps+"_0351_forested_habitat_blocks_bg_nd.tif", 
    output = temps+"_0352_forested_habitat_blocks_area.tif", 
    out_text=False, 
    units="map units", 
    zero_back=True
)

# Convert square meters to acres.

wbt.divide(
    input1 = temps+"_0352_forested_habitat_blocks_area.tif", 
    input2 = 4046.86, 
    output = keeps+"_0353_forested_habitat_blocks_acres.tif",
)