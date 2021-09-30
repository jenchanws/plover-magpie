
# magpielib (feel free to pick your own name!)

def stroke_to_shav(stroke: str) -> str:
  """
  Returns the Shavian equivalent of a single steno stroke.

  >>> stroke_to_shav("𐑑𐑐𐑣𐑧𐑑")
  "𐑯𐑧𐑑"
  """
  if stroke == "#𐑓𐑩":
    return "𐑓𐑩{^}"
  elif stroke == "𐑑𐑐𐑣𐑧𐑑":
    return "𐑯𐑧𐑑"
  elif stroke == "𐑒𐑢𐑮-𐑚𐑜𐑕":
    return "{^}𐑦𐑒𐑕"

  # Replace this with your conversion logic, maybe from mainbriefs.json ?


def steno_to_shav(steno: Tuple[str]) -> str:
  """
  Given the strokes in 'steno', returns the Shavian string corresponding to all
  of the strokes combined.

  >>> st = ("#𐑓𐑩", "𐑑𐑐𐑣𐑧𐑑", "𐑒𐑢𐑮-𐑚𐑜𐑕")
  >>> steno_to_shav(st)
  "𐑓𐑩𐑯𐑧𐑑𐑦𐑒𐑕"
  """
  pass


def shav_to_latin(shav: str) -> str:
  """
  Converts the Shavian string 'shav' to Latin.

  >>> shav_to_latin("𐑓𐑩𐑯𐑧𐑑𐑦𐑒𐑕")
  "phonetics"
  """
  
  # Insert your readlex logic here


# latin_dict.py
from magpielib import shav_to_latin, steno_to_shav

def lookup(steno: Tuple[str]) -> str:
  try:
    shav_to_latin(steno_to_shav(steno))
  except:
    raise KeyError


# shavian_dict.py
import magpielib

def lookup(steno: Tuple[str]) -> str:
  try:
    steno_to_shav(steno)
  except:
    raise KeyError

