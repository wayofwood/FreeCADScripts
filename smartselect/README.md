# Smart Selection helper tool

Especially for CNC work it is sometimes necessary to select several 
edges or shapes based on certain criteria. 

The macro is quite simple: Just select an edge or a face and then run 
the macro. You will then see the following UI:

[UI of the Macro](https://wayofwood.com/wp-content/uploads/2022/01/Bildschirmfoto-vom-2022-01-12-14-50-08.png)

The precision parameter is a percentage that two areas or the length
of two edges can differ so that they are still considered equal. 
Normally this parameter should work fine. If you want to differentiate
areas with very similar size decrease the precision. 

If the "Same Object" box is selected only faces or edges in the same
object are selected. You normally want to check this box when working
with the Path workbench as there is a copy of the object within the 
Job and the original one and you normally only want to select faces
from one of the two. 

"Same Length/Area" means that only items with the same size are 
selected. Use this feature if you want to select for example all the
pockets of an object with the same size. 

"Same Z/X/Y" will only select objects that have the same X, Y or Z
variable as the selected one. Especially Z is helpful if there are 
similar shapes at the top and the bootom of an object. 