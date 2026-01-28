from probables import CuckooFilter
import os
from core import logger, settings
import httpx
import base64
import gzip
from typing import Any


class Cuckoo:
  KV_URI = f"https://api.cloudflare.com/client/v4/accounts/{settings.CLOUDFLARE_ACCOUNT_ID}/storage/kv/namespaces/{settings.CLOUDFLARE_KV_NAMESPACE}/bulk"
  AUTH_HEADERS = {"Authorization": f"Bearer {settings.CLOUDFLARE_API_KEY}"}

  def __init__(self, obj: CuckooFilter, filename="job_filter.bin"):
    self._save_path = filename
    if os.path.exists(self._save_path):
      logger.LOGGER.info("Loaded CuckooFilter from Saved Path")
      self._filter: CuckooFilter = CuckooFilter(filepath=self._save_path)
    else:
      logger.LOGGER.info("Initialize a new CuckooFilter")
      self._filter: CuckooFilter = obj

  def save(self):
    self._filter.export(self._save_path)

  def load(self):
    logger.LOGGER.debug("Loaded CuckooFilter from Saved Path")
    self._filter: CuckooFilter = CuckooFilter(filepath=self._save_path)

  def upload(self) -> bool:
    with open(self._save_path, "rb") as f:
      compressed_data = gzip.compress(f.read())
      encoded_data = base64.b64encode(compressed_data).decode()
      with httpx.Client() as client:
        response = client.put(
          url=self.KV_URI,
          headers=self.AUTH_HEADERS,
          json=[{"key": "CuckooFilter", "value": encoded_data}],
        )

      try:
        return response.json()["success"]
      except Exception as e:
        logger.LOGGER.debug(e)
        return False

  def download(self) -> bool:
    with open(self._save_path, "wb") as f:
      with httpx.Client() as client:
        response = client.post(
          url=f"{self.KV_URI}/get",
          headers=self.AUTH_HEADERS,
          json={"keys": ["CuckooFilter"]},
        )

      try:
        if not response.json()["success"]:
          return False

        keys: dict[str, str] = response.json()["result"]["values"]
        decoded_data = base64.b64decode(keys["CuckooFilter"])
        uncompressed_data = gzip.decompress(decoded_data)
        f.write(uncompressed_data)
        return True

      except Exception as e:
        logger.LOGGER.debug(e)
        return False

  def add(self, item: Any):
    self._filter.add(item)

  def exist(self, item: Any) -> bool:
    return self._filter.check(item)


CUCKOOFILTER = Cuckoo(CuckooFilter(capacity=100000, max_swaps=500))
