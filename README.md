## VT Conservation Docs  

A collection of geographic data workflows for teaching and doing conservation planning.   

### Data 

The data called by the scripts can be accessed [here](https://drive.google.com/drive/folders/1H_9ShSYgT1qYIMOfpEarzISFqd3OnGSu?usp=sharing). 

You will need to:  

1. Download the dataset.  
2. Place it in a local folder.
3. Update the script so that the input data variable points to your local path.

### Practice

The practice workflows are python scripts that implement tools with [WhiteboxTools Open Core][01]. For technical documentation on the tools, please refer to the [WhiteboxTools manual][02].

| Script    | Description   |
| :--       | :---          |
| [_01_simple_landforms.py][11] | Classify landforms from a 10m DEM with geomorphons. | 
| [_02_valley_bottoms.py][12]   | Resample a high resolution DEM, classify landforms with geomorphons, and threshold to isolate valley bottoms. | 

[01]: https://www.whiteboxgeo.com/geospatial-software/
[02]: https://www.whiteboxgeo.com/manual/wbt_book/available_tools/index.html

[11]: practice/_01_simple_landforms.py 
[12]: practice/_02_valley_bottoms.py

