from . import environ
from flashtext import KeywordProcessor
from . import debug


KEYWORDS = KeywordProcessor()
if not environ.ENV.exist("KEYWORDS"):
  raise EnvironmentError("KEYWORDS Environment is not set")

for keyword in str(environ.ENV.get("KEYWORDS")).split(","):
  KEYWORDS.add_keyword(keyword.strip())

if not debug.DEBUG:
  if not environ.ENV.exist("CLOUDFLARE_API_KEY"):
    raise EnvironmentError("CLOUDFLARE_API_KEY Environment is not set")
  CLOUDFLARE_API_KEY = str(environ.ENV.get("CLOUDFLARE_API_KEY"))

  if not environ.ENV.exist("CLOUDFLARE_ACCOUNT_ID"):
    raise EnvironmentError("CLOUDFLARE_ACCOUNT_ID Environment is not set")
  CLOUDFLARE_ACCOUNT_ID = str(environ.ENV.get("CLOUDFLARE_ACCOUNT_ID"))

  if not environ.ENV.exist("CLOUDFLARE_DATABASE_ID"):
    raise EnvironmentError("CLOUDFLARE_DATABASE_ID Environment is not set")
  CLOUDFLARE_DATABASE_ID = str(environ.ENV.get("CLOUDFLARE_DATABASE_ID"))

  if not environ.ENV.exist("CLOUDFLARE_KV_NAMESPACE"):
    raise EnvironmentError("CLOUDFLARE_KV_NAMESPACE Environment is not set")
  CLOUDFLARE_KV_NAMESPACE = str(environ.ENV.get("CLOUDFLARE_KV_NAMESPACE"))
