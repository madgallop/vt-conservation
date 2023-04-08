## Wetlands

### Purpose 
This image compiles the best available information in the state of Vermont for the location of Class I and Class II wetlands, their respective setbacks, and advisory regions, or locations with a high likelihood of wetland presence based on data produced through manual interpretation of imagery and through modeling.  

### Bands 
The image consists of a set of bands, like a collection of individual layers, where each band represents a different description of a place. Storing information as bands allows us to describe more than one attribute of a location.  

### VSWI Wetlands Class Layer 
The Vermont State Wetlands Inventory (VSWI) Class layer shows jurisdictional wetlands of the State of Vermont. It is based on the VSWI Wetlands Class Layer, which identifies Class I and Class II wetlands as well as setback zones for Class I wetlands.  

| pixel value   | definition |
| :---:         | :---       |
| 1             | Class I    |
| 2| Class I setback |
| 3 | Class II |


###  Class II setback 

This band shows setbacks from Class II wetlands. To make this, we isolated Class II wetlands from the State Jurisdiction band and then buffered by 50 ft.  

| pixel value | definition |
| :---:         | :---       |
| 1 |   Class II setback |

### Advisory regions

“Advisory regions” are wetlands mapped through manual interpretation of data or through computational modeling, but without extensive field verification. We compiled separate bands from three different sources. 

* VSWI Wetlands Advisory  
* Arrowwood Environmental
* The North Atlantic Vernal Pool Data Cooperative  

For the first two sources, each band records the presence or absence of all wetlands. For the third source, we reclassified the original values as shown in the table below, with new values representing presence (1) or absence (0).  

| Definition | original  value | new value |
| :---         | :---:       | :---:       |
Connected wetlands | 0 | 1 |
| Large water bodies | 1 | 0 |
| Non habitat | 2 | 0 |
| Other potential habitat | 3 | 0 |
| Potential Vernal Pools - Highest classification Value | 4 | 1 |
| Potential Vernal Pools - Low Classification Value | 5 | 0 |
| Potential Vernal Pools - Medium classification Value | 6 | 1 |
| Potential Vernal Pools - Obscured by Conifers | 7 | 0 |

We then produced a single “advisory compilation” band that represents the union of the three sources, where each pixel represents either the presence or absence of an advisory region from one or more sources. We did not model setbacks for any advisory regions, because these wetlands have not been verified in the field and their jurisdictional status (class) is not known.  

### Wetlands compilation
The final “wetlands compilation” band brings together the information in the other bands as follows: 

| pixel value | class |
| :---:       | :---: |
| 1 | Class 1 |
| 2 | Class 1 buffer |
| 3 | Class 2 |
| 4 | Class 2 buffer |
| 5 | Advisory region (union) |

### Script

We used Google Earth Engine to compile the image. Please contact Jeff Howarth (jhowarth@middlebury.edu) to request a copy of the script.  

### Known limitations
The VSWI Class I and II boundaries and setbacks shown in the image are “official” designations but may not correspond perfectly with actual conditions on the ground. The mapped features signal when a review by the State will be required.  

The advisory regions have a high likelihood of wetland presence, based on interpretation of data by experts and based on modeling. In Middlebury, the wetlands in the VSWI Advisory layer were produced by George Springston for the Town of Middlebury (completed in 2001). As stated in Springston’s executive summary of his final report to the town:  

>Aerial photo interpretation has been used to produce improved wetland maps for the Town of Middlebury. Custom 1:12,000 color infrared aerial photographs were flown for the project. Wetlands were delineated on the photos using a stereoscope and the results were transferred onto 1:10,000 scale base maps. The wetlands were then digitized and converted into an ArcInfo Geographic Information System coverage.
The wetland maps and digital products produced in this project are the result of limited field work, careful photo interpretation, and consultation of the best available sources of additional information. These maps are intended to indicate approximate wetland boundaries at no larger than 1:5,000 scale for planning purposes only. They are not intended to be substitutes for on-the-ground wetland delineations by trained wetland experts. Appropriate local, state, or federal officials should be contacted to determine if any wetland regulations apply.” (source: page 17)  

In 2018, the Town of Middlebury contracted Arrowwood Environmental, LLC to map wetlands in town (source). This consultant relied primarily on the interpretation of aerial imagery and maps with little field verification (source). The overwhelming majority of the mapped features were not verified in the field (Table 1).  

| Value | Definition | # mapped features | %  mapped features | 
| :---: |  :--- |  :---: |  :---: |   
| Y | Field visit | 12 | 1% |
| D | Drive-by visit | 93 | 9% |
| N or blank | Not field verified | 971 | 90% |

*Table 1. Field verification in Arrowwood data product (2021). The number and percent of wetland features with “Y”, “D”, and either “N” or blank values in the  “FIELDVISIT” column of the Arrowwood wetland data product.*

In addition, the Arrowwood contract only required wetlands to be mapped within the Town of Middlebury. As a result, the majority of wetlands that are found on the edge of town were only mapped to the town boundary.  

### Recommendations

It would be prudent for the Planning Commission and Development Review Board to require wetland field surveys by ANR-approved scientists for development proposals that overlap with regions shown in the advisory compilation layer. 

### Credits

Prepared by Jeff Howarth. Associate Professor of Geography, Middlebury College

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.

Last updated: 3/21/2023
