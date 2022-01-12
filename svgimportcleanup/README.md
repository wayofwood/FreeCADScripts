# SVG Import Cleanup

When importing a SVG file a number of cleanup steps are necessary
in order to use the file with the V-Carve operation from the Path
workbench. 

The manual method is described here:

https://wiki.freecadweb.org/Path_Vcarve

## How to use the script

When you want to use the script import the SVG file into an empty 
FreeCAD file without any other objects present in the file. 

After importing the "holes" of parent shapes are imported as 
individual objects (like the smaller star in the image below):

![SVG shapes after import](https://wayofwood.com/wp-content/uploads/2022/01/Bildschirmfoto-vom-2022-01-12-14-32-52.png)

After running the macro the smaller objects are cut from the larger
ones:

![SVG shapes after running the macro](https://wayofwood.com/wp-content/uploads/2022/01/Bildschirmfoto-vom-2022-01-12-14-36-05.png)