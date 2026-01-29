from playwright.sync_api import Browser
from core import settings
from models import JobData


IBM_CAREERS = "https://www.ibm.com/in-en/careers/search?field_keyword_08[0]=Software%20Engineering&field_keyword_08[1]=Cloud&field_keyword_18[0]=Entry%20Level&field_keyword_18[1]=Internship&field_keyword_05[0]=India&q=software%20engineer%2Cfullstack%2Cfull%20stack&sort=dcdate_desc"


def match(sentence: str) -> bool:
  return len(settings.KEYWORDS.extract_keywords(sentence.lower())) != 0


def scrap_ibm(browser: Browser) -> list[JobData]:
  result = []
  page = browser.new_page()
  page.goto(IBM_CAREERS)
  page.wait_for_selector("#ibm-hits-wrapper", state="visible")

  job_list = page.locator("#ibm-hits-wrapper")

  for item in job_list.locator(".bx--card-group__cards__col").all():
    title = item.get_attribute("aria-label")
    url = item.locator("a").first.get_attribute("href")

    if url is None or title is None:
      continue

    if match(title):
      result.append(JobData(title=title, url=url, company="IBM"))

  return result
