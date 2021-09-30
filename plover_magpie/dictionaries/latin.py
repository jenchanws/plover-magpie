from magpielib import shav_to_latin, steno_to_shav

def lookup(steno: Tuple[str]) -> str:
  try:
    shav_to_latin(steno_to_shav(steno))
  except:
    raise KeyError
