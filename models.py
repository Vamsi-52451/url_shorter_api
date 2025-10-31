from pydantic import BaseModel, HttpUrl

class URLItem(BaseModel):
    original_url: HttpUrl
