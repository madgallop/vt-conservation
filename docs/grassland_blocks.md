## Grassland habitat blocks

### Purpose 

The grassland habitat block model identifies regions that meet four criteria recommended by the Vermont ANR Fish and Wildlife Department for grassland bird habitat.  

### Map layers

In the Grassland Habitat map (link):
1. The “2016 open habitat” layer shows grass, shrub, water, or agriculture classes isolated from the other land cover classes.
2. The “Insulated grasslands” layer shows regions of open habitat that are at least 50 meters from either structural elements (tree canopy, building) or developed land (roads, pavement).  
3. The “Grassland habitat blocks” layer shows insulated grasslands that meet area and shape criteria.
4. The “Grassland habitat with protections for agriculture” shows grassland habitat blocks with protections for agriculture. 

### Methodology
The model involves four steps: 
1. Isolate open habitat based on land cover (grass, shrub, water, and agricultural fields).
2. Determine regions of open habitat that are at least 50 meters from some type of structure (e.g. tree canopy, buildings) or developed surface (e.g. road, pavement).
3. Select regions that are at least 20 acres in area.
4. Select regions with large interiors based on shape (with a perimeter/area ratio less than 1.5). 

For land cover, we used the base layer and agricultural supplement from the 2016 Vermont High Resolution (0.5 meter) Land Cover Dataset. To prepare the data, we combined the base layer with the agricultural supplemental layer. For agriculture, we did not distinguish between pasture, haying, and cropland. When combining the agricultural layer and base layer, we replaced any grass/shrub or bare class in the base layer with an agricultural class, but preserved the tree canopy and water class in the base layer, even when they overlapped with the agricultural layer. This method preserves water features, hedge rows, and shade trees in agricultural areas, while distinguishing active clearings from old fields. 

We implemented the model with a custom script implemented with Google Earth Engine. Please contact Jeff Howarth (jhowarth@middlebury.edu) to request a copy of the script.  

### Known limitations

The model uses a land cover dataset that describes conditions in 2016. As a result, it identifies places that met the criteria for grassland habitat at this time, but does not capture changes that have occurred since 2016.  

The map layer identifies potential grassland habitat based on spatial criteria. These grasslands do not necessarily function as grassland habitat for bird populations, because farming practices may disrupt nesting and impact fledgling success.  

At least two steps in the model are influenced by analysis scale decisions. First, we used a modal filter with a circle kernel to remove artifacts from outliers in the high-resolution land cover dataset (for example, to remove a single tree canopy pixel in a field of grass or agriculture). Second, we defined the pixel scale of the image to group contiguous pixels of the same class into regions. We tested the model’s sensitivity to scale parameters and settled on 2.5 meters for both kernel circle diameter and pixel scale grouping.  

The model may be conservative, producing some false negatives, because scattered trees or bare ground affect the size and shape of regions insulated from structural elements. We elected to use a relatively small filter to reduce noise in order to preserve hedgerows, roads, and other features that have been reported to reduce habitat quality for grassland birds.   

### Next steps

Field studies should be conducted to help evaluate how these grassland habitat blocks currently function and what measures could be taken to improve their function as habitat for bird populations. This should include surveys in the breeding season to document the presence of grassland bird species. This should also include surveys to document and monitor the timing of agricultural activities. 

As new land cover datasets become available in the future, the model should be used to monitor habitat fragmentation and to document types of land cover conversions that cause the habitat fragmentation (e.g. commercial development, housing development, renewable energy development, etc). 
  
### Credits

Prepared by Jeff Howarth. Associate Professor of Geography, Middlebury College

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.

Last updated: 3/21/2023