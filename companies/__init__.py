from models.website import Website
from . import zoho, jpmorgan, oracle, ibm


WEBSITES: list[Website] = []
WEBSITES.append(Website(name="Zoho", helper=zoho.scrap_zoho))
WEBSITES.append(Website(name="JPMorgan", helper=jpmorgan.scrap_jpmorgan))
WEBSITES.append(Website(name="Oracle", helper=oracle.scrap_oracle))
WEBSITES.append(Website(name="IBM", helper=ibm.scrap_ibm))
