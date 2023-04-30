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

# valleys = keeps+"_0204_valley_bottoms_smoothed_objects.tif"  
# blocks = temps+"_0343_forested_habitat_blocks.tif"

valleys = keeps+"_0214_valleys_not_developed_clumps.tif"  
blocks = keeps+"_0356_forested_habitat_blocks_gte_XX_acres_objects.tif"

# ==============================================================================
# WORKFLOW
# ==============================================================================

# ------------------------------------------------------------------------------
# Align images: must be same extent and cell size. 
# ------------------------------------------------------------------------------

# Resample blocks to match valley cell size. 

wbt.resample(
    inputs = blocks, 
    output = temps+"_0401_resample.tif", 
    cell_size = None, 
    base = valleys, 
    method = "nn"
)

# ------------------------------------------------------------------------------
# Erase valleys where they overlap blocks. 
# ------------------------------------------------------------------------------

# Convert blocks into an inverse binary. 

wbt.equal_to(
    input1 = temps+"_0401_resample.tif", 
    input2 = 0, 
    output = temps+"_0411_inverse_binary.tif", 
)

# Erase blocks from valley bottoms.  

wbt.multiply(
    input1 = temps+"_0411_inverse_binary.tif", 
    input2 = valleys, 
    output = temps+"_0412_valleys_not_blocks.tif", 
)

# Re-clump valley bottoms to identify individual objects. 

wbt.clump(
    i = temps+"_0412_valleys_not_blocks.tif", 
    output = temps+"_0413_valleys_not_blocks_clumps.tif", 
    diag=True, 
    zero_back=True
)

# ------------------------------------------------------------------------------
# Identify and remove islands. 
# ------------------------------------------------------------------------------

# Grow valley bottom edge by one pixel.

wbt.maximum_filter(
    i = temps+"_0413_valleys_not_blocks_clumps.tif", 
    output = temps+"_0414_valleys_not_blocks_clumps_extra_edge.tif", 
    filterx=3, 
    filtery=3
)

# Mask background.

wbt.set_nodata_value(
    i = temps+"_0414_valleys_not_blocks_clumps_extra_edge.tif", 
    output = temps+"_0415_valleys_not_blocks_extra_edge_clumps_bg_masked.tif", 
    back_value=0.0,
)

# Test for overlap between valley bottoms and habitat blocks.

wbt.zonal_statistics(
    i = temps+"_0401_resample.tif", 
    features = temps+"_0415_valleys_not_blocks_extra_edge_clumps_bg_masked.tif", 
    output = temps+"_0416_test_overlap.tif", 
    stat = "max", 
    out_table = None
)

# Mask islands.  

wbt.set_nodata_value(
    i = temps+"_0416_test_overlap.tif", 
    output = temps+"_0417_not_islands.tif", 
    back_value=0.0, 
)

# Re-clump valley bottoms without islands to identify individual objects. 

wbt.clump(
    i = temps+"_0417_not_islands.tif", 
    output = temps+"_0418_not_island_clumps.tif", 
    diag=True, 
    zero_back=True
)

# ------------------------------------------------------------------------------
# Select corridors. 
# ------------------------------------------------------------------------------

# Set background of blocks to no data. 

wbt.set_nodata_value(
    i = temps+"/_0401_resample.tif", 
    output = temps+"_0421_resample_blocks_mask_bg.tif", 
    back_value=0.0, 
)

# Test for min of overlap.

wbt.zonal_statistics(
    i = temps+"_0421_resample_blocks_mask_bg.tif", 
    features = temps+"_0418_not_island_clumps.tif", 
    output=temps+"_0422_valley_blocks_overlap_min.tif", 
    stat="min", 
    out_table=None, 
)

# Test for max of overlap.

wbt.zonal_statistics(
    i = temps+"_0421_resample_blocks_mask_bg.tif", 
    features = temps+"_0418_not_island_clumps.tif", 
    output=temps+"_0423_valley_blocks_overlap_max.tif", 
    stat="max", 
    out_table=None, 
)

# Bridges (tombolos) will have unequal min and max values, 
# while piers (spits) will have equal min and max values. 

wbt.not_equal_to(
    input1 = temps+"_0423_valley_blocks_overlap_max.tif", 
    input2 = temps+"_0422_valley_blocks_overlap_min.tif", 
    output = temps+"_0424_valley_corridors_test.tif", 
)

# Unmask background values. 

wbt.convert_nodata_to_zero(
    i = temps+"_0424_valley_corridors_test.tif", 
    output = temps+"_0425_valley_corridors_test_bg_0.tif"
)

# Select valley bottom corridors. 

wbt.zonal_statistics(
    i = temps+"_0425_valley_corridors_test_bg_0.tif", 
    features = temps+"_0414_valleys_not_blocks_clumps_extra_edge.tif", 
    output=keeps+"_0426_valley_corridors_not_developed_blocks_gte_XX_acres.tif", 
    stat="max", 
    out_table=None
)