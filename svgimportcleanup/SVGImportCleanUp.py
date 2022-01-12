# ***************************************************************************
# *   Copyright (c) 2022 WayofWood <code@wayofwood.com>                     *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is taking the shapes imported from a SVG file and        *
# *   converts these into faces that can then be used for the V-carve       *
# *   operation from the FreeCAD path workbench.                            *
# *                                                                         *
# *   The method is based on the procedure described here:                  *
# *                                                                         *
# *   https://wiki.freecadweb.org/Path_Vcarve                               *
# *                                                                         *
# ***************************************************************************

import FreeCAD as App
import Draft

# ***************************************************************************
# First convert all wires to faces. Iterate over all objects in the document
# so make sure that you only have the SVG file imported
# ***************************************************************************
objects = App.ActiveDocument.Objects
for object in objects:
	print("Name:{}\t Label: {}\t ".format(object.Name,object.Label ) )
	print("  => Faces:{}".format(len(object.Shape.Faces)))
	faces = len(object.Shape.Faces)
	if (faces == 0):
		oldname = object.Name
		add_list, delete_list = Draft.upgrade(object, delete=True)
		add_list[0].Label = oldname
	else:
		oldname = object.Name
		add_list, delete_list = Draft.downgrade(object, delete=True)
		add_list1, delete_list1 = Draft.upgrade(add_list[0], delete=True)
		add_list1[0].Label = oldname
App.ActiveDocument.recompute()

# ***************************************************************************
# Put objects with the same name in a group. SVG import names the paths from
# the same shape so that they start with the same string (e.g. path1001 and 
# path1001001 belong to the same shape. 
#
# We then remove all the shapes from the list that do not overlap as we are
# looking for "holes" to be substracted afterwards.
# ***************************************************************************
objects = App.ActiveDocument.Objects
basenames = {}

for object in objects:
	print("Name:{}\t Label: {}\t ".format(object.Name,object.Label ) )
	name = object.Label
	basenames[name] = [ object ]

	if (len(object.Shape.Faces) > 0):
		face = object.Shape.Faces[0]
		for subobject in objects:
			thisname = subobject.Label
			# Add objects with the same name
			if (thisname.startswith(name) and thisname != name):
				print ("Candidate for adding: {} to list {}".format(thisname, name))
				isinside=True
				# Test if all the points of the shape are within object - otherwise dismiss
				for vertex in subobject.Shape.Vertexes:
					if (face.isInside(vertex.Point, 0.000001, True) == False):
						isinside = False
				if (isinside):		
					basenames[name].append( subobject )
					print (" ==> Added")
				# Test reverse (shorter name contained in longer name)
				else:
					isinside = True
					if (len(subobject.Shape.Faces) > 0):
						face = subobject.Shape.Faces[0]
						for vertex in object.Shape.Vertexes:
							if (face.isInside(vertex.Point, 0.000001, True) == False):
								isinside = False
						if (isinside):		
							basenames[name].append( subobject )
							print (" ==> Added")
					
# ***************************************************************************
# Cut away the smaller parts from the larger ones: Sort the shapes so that 
# the one with the largest area is places first and then others are 
# substracted from the largest one. 
# ***************************************************************************
for group in basenames:
	list= sorted(basenames[group], key=lambda x: x.Shape.Faces[0].Area, reverse=True)
	if (len(list) > 1):
		Draft.downgrade(list, False)
		for o in list:
			o.Visibility = False

App.ActiveDocument.recompute()