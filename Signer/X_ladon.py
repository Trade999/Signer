import time
from .Ladon import Ladon
def x_ladon(unix=None, license_id=1611921764, aid=1233):
  if not unix: unix = int(time.time())
  return { "x-ladon": Ladon.encrypt(unix, license_id, aid)}
  