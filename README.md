## VT Conservation    

A collection of geographic data workflows for teaching and doing conservation planning using examples from Vermont, USA.   

### Practice workflows

The practice workflows are python scripts that implement [WhiteboxTools Open Core][wb1]. For technical documentation, please refer to the [WhiteboxTools manual][wb2].

| Script    | Description   |
| :--       | :---          |
| [_01_simple_landforms.py][01] | Classify landforms with geomorphons. | 
| [_02_valley_bottoms.py][02]   | Classify landforms with geomorphons, threshold to isolate valley bottoms, smooth with neighborhood majority filter. | 

### Data repository  

You can access data for the practice scripts [here][data].  

| Dataset   | Description   | 
| :---      | :---          |
| DEM_10m_midd.tif  | 10m 3DEP for Middlebury, Vermont.  |
| LCHP_1m_midd.tif  | 1m Vermont Land Cover dataset with agriculture, roads, and building zones for Middlebury, Vermont. | 


To use this data in the practice scripts, you will need to:  

1. Create four sub-directories in a root directory on a drive as shown below. The three directories should be named:

    * inputs
    * keeps
    * projects 
    * temps 

![directory](assets/directory_.png) 

2. Download the required datasets and place them in the inputs folder.  

3. In the practice script, update the root variable so that it provides the path to your root folder. For example:  

```python
root = "/Volumes/drosera/GEOG0310/s23"
```

In the above example, the root variable points to the s23 folder in GEOG0310 on an external hardrive named drosera. 

### Contact 

Jeff Howarth  
Associate Professor of Geography  
Middlebury College  


[data]: https://drive.google.com/drive/folders/1H_9ShSYgT1qYIMOfpEarzISFqd3OnGSu?usp=sharing

[wb1]: https://www.whiteboxgeo.com/geospatial-software/

[wb2]: https://www.whiteboxgeo.com/manual/wbt_book/available_tools/index.html

[01]: practice/_01_simple_landforms.py 
[02]: practice/_02_valley_bottoms.py


