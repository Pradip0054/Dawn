from core import debug, logger


def database_conn(func):
  def wrapper():
    if not debug.DEBUG:
      from . import database, cuckoo

      database.initialize_tables()

      logger.LOGGER.info("Trying to load CuckooFilter from Cloudflare KV...")
      if cuckoo.CUCKOOFILTER.download():
        cuckoo.CUCKOOFILTER.load()
        logger.LOGGER.info("CuckooFilter Loaded")
      else:
        logger.LOGGER.info("Cuckoo Filter Loading Failed, Using Default Cuckoo Filter")

    func()

    if not debug.DEBUG:
      logger.LOGGER.info(
        "Cuckoo Filter Upload: %s",
        "Success" if cuckoo.CUCKOOFILTER.upload() else "Failed",
      )

  return wrapper
