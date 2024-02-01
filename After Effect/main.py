import win32com.client # For Windows only, this is a package to interface with COM objects

# Create a new After Effects application object
ae = win32com.client.Dispatch("AfterEffects.Application")

# Create a new composition
comp = ae.Projects.AddComp("My Comp", 1920, 1080, 1.0, 10.0, 30)

# Add a new text layer to the composition
text_layer = comp.layers.AddText("Hello, world!")

# Set some properties of the text layer
text_layer.property("Source Text").setValue("Hello, world!")
text_layer.property("Position").setValue([960, 540])

# Save the project file
ae.Projects.Save()





import gc
# Recursively expand slist's objects
# into olist, using seen to track
# already processed objects.
def _getr(slist, olist, seen):
  for e in slist:
    if id(e) in seen:
      continue
    seen[id(e)] = None
    olist.append(e)
    tl = gc.get_referents(e)
    if tl:
      _getr(tl, olist, seen)

# The public function.
def get_all_objects():
  """Return a list of all live Python
  objects, not including the list itself."""
  gcl = gc.get_objects()
  olist = []
  seen = {}
  # Just in case:
  seen[id(gcl)] = None
  seen[id(olist)] = None
  seen[id(seen)] = None
  # _getr does the real work.
  _getr(gcl, olist, seen)
  return olist


import numpy as np
import gc

a = np.random.rand(100)
objects = get_all_objects()
print(any[x is a for x in objects])
# will return True, the np.ndarray is found!