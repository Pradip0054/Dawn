from playwright.sync_api import Browser
from core import settings
from models import JobData


JPMORGAN_CAREERS = "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/jobs?lastSelectedFacet=POSTING_DATES&location=India&locationId=300000000289360&locationLevel=country&mode=location&selectedCategoriesFacet=300000086152753&selectedPostingDatesFacet=7"


def match(sentence: str) -> bool:
  return len(settings.KEYWORDS.extract_keywords(sentence.lower())) != 0


def scrap_jpmorgan(browser: Browser) -> list[JobData]:
  result = []

  page = browser.new_page()
  page.goto(JPMORGAN_CAREERS, wait_until="load", timeout=60000)
  page.wait_for_selector("#panel-list", state="visible")

  jobs = page.locator("#panel-list")
  for job in jobs.locator('li[data-qa="searchResultItem"]').all():
    url = job.locator("a").get_attribute("href")
    if url is None:
      continue

    clean_url = url.split("?")[0]
    title = (
      job.locator("search-result-item-header")
      .first.locator('span[data-bind="text: job.title"]')
      .first.inner_text()
    )

    if match(title):
      result.append(JobData(title=title, url=clean_url, company="JPMorgan"))

  return result
