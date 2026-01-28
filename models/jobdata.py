from pydantic import BaseModel


class JobData(BaseModel):
  title: str
  url: str
  company: str
