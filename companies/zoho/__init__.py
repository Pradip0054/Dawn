from playwright.sync_api import Browser
from core import settings
from models import JobData


ZOHO_CAREERS = "https://careers.zohocorp.com/jobs/Careers"


def match(sentence: str) -> bool:
  return len(settings.KEYWORDS.extract_keywords(sentence.lower())) != 0


def scrap_zoho(browser: Browser) -> list[JobData]:
  result = []
  page = browser.new_page()
  page.goto(ZOHO_CAREERS)

  job_list = page.locator(".jobcard-container").first
  settings.KEYWORDS

  for item in job_list.locator("h3").all():
    url = item.locator("a").get_attribute("href")
    title = item.inner_text()

    if url is None:
      continue

    if match(title):
      result.append(JobData(title=title, url=url))

  return result
