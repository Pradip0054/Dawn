from playwright.sync_api import sync_playwright
import companies
from core import logger, debug, settings
from db.decorators import database_conn


@database_conn
def start_scrapping():
  """
  Start the scrapping service
  """
  with sync_playwright() as play:
    browser = play.chromium.launch(headless=True)

    for website in companies.WEBSITES:
      logger.LOGGER.info("Scrapping Company: %s", website.name)
      result = website.helper(browser)
      logger.LOGGER.debug("Found URLs: %s", result)

      if not debug.DEBUG:
        from db import database

        database.store_jobs(result)

    browser.close()


if __name__ == "__main__":
  print("Debug Mode: " + ("On" if debug.DEBUG else "Off"), flush=True)
  logger.LOGGER.debug(
    "Keywords to Look for: %s", settings.KEYWORDS.get_all_keywords().keys()
  )
  start_scrapping()
