from core import settings, logger
from httpx import Client
from models import jobdata
from . import cuckoo


QUERY_URL = f"https://api.cloudflare.com/client/v4/accounts/{settings.CLOUDFLARE_ACCOUNT_ID}/d1/database/{settings.CLOUDFLARE_DATABASE_ID}/query"
AUTH_HEADERS = {"Authorization": f"Bearer {settings.CLOUDFLARE_API_KEY}"}


def initialize_tables() -> bool:
  """
  Initialize the tables (If not exist)
  """
  sql = """
  CREATE TABLE IF NOT EXISTS jobs_list (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_role TEXT,
    url TEXT UNIQUE NOT NULL,
    company TEXT NOT NULL,
    added_at DATETIME DEFAULT CURRENT_TIMESTAMP
  );

  CREATE INDEX IF NOT EXISTS idx_added_at ON jobs_list(added_at);
  """

  with Client() as client:
    response = client.post(url=QUERY_URL, headers=AUTH_HEADERS, json={"sql": sql})

  logger.LOGGER.debug(response.json())
  return response.json()["success"]


def store_jobs(jobs: list[jobdata.JobData]) -> bool:
  """
  Store the list of jobs in the tables

  :param jobs: The list of the jobs
  :type jobs: list[jobdata.JobData]
  :return: Returns True if the process success, otherwise failed
  :rtype: bool
  """
  result = []

  for job in jobs:
    if cuckoo.CUCKOOFILTER.exist(job.url):
      continue

    sql = "INSERT OR IGNORE INTO jobs_list (job_role, url, company) VALUES (?, ?, ?)"
    params = [job.title, job.url, job.company]

    with Client() as client:
      response = client.post(
        url=QUERY_URL, headers=AUTH_HEADERS, json={"sql": sql, "params": params}
      )

    try:
      resp = response.json()

      if resp["success"]:
        cuckoo.CUCKOOFILTER.add(job.url)

      result.append(resp["success"])
    except Exception as e:
      logger.LOGGER.debug(str(e))
      result.append(False)

  cuckoo.CUCKOOFILTER.save()
  return all(result)
