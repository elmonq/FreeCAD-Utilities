""" Program to convert STEP files to STL files using FreeCAD.

In order to run the program requires the following:
1) An enviroment variable named FREECAD_BIN_PATH must be set and pointed to the bin directory of your FreeCAD install
2) Python version and bit (32/64) of FreeCAD. i.e. FreeCAD was Python 3.8 64 Bit """
import sys
import os

sys.path.append(os.environ.get('FREECAD_BIN_PATH'))


def convert_to_stl(filename_in):
  """ Converts STEP file to STL file.  File with the same name but .stl extension will be output into the same folder.
      inputs: 
        filename_in: name of file to convert 
  """
    try:
        import FreeCAD
    except ValueError:
        print('FreeCAD library not found. Please check that the FREECAD_BIN_PATH environment variable is set properly')
    else:
        import Part
        import Mesh

        # Load file into FreeCAD
        shape = Part.Shape()
        shape.read(filename_in)
        doc = App.newDocument('Doc')
        pf = doc.addObject("Part::Feature", "MyShape")
        pf.Shape = shape

        # Get export filename as input filename with extension converted to stl then export it
        filename, ext = os.path.splitext(filename_in)
        Mesh.export([pf], filename + ".stl")


if __name__ == '__main__':
    filename_in = sys.argv[1]
    if filename_in is None:
        print("No filename given to convert.  FIlename is expected as the first argument to program.")
    else:
        convert_to_stl(filename_in)
