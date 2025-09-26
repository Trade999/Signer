import time, hashlib
from .X_Gorgon import generate_gorgon
from .X_ladon import x_ladon
from .X_Argus import Argus

def signature(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int = 2, platform: int = 19, unix: int = None):
  x_ss_stub = hashlib.md5(payload.encode('utf-8')).hexdigest() if payload != None else None
  if not unix: unix = int(time.time())
  headers = generate_gorgon(params, payload, cookie)
  headers.update(x_ladon())
  xargus = {
    "x-argus": Argus.get_sign(
      params,
      x_ss_stub,
      unix,
      platform=platform,
      aid=aid,
      license_id=license_id,
      sec_device_id=sec_device_id,
      sdk_version=sdk_version_str,
      sdk_version_int=sdk_version,
    )
  }
  headers.update(xargus)
  return headers