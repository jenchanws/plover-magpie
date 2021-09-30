from magpielib import shav_to_latin, steno_to_shav

def lookup(steno: Tuple[str]) -> str:
  try:
    steno_to_shav(steno)
  except:
    raise KeyError
