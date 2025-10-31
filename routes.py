from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from models import URLItem
import string, random

router = APIRouter()

# Temporary in-memory database
url_db = {}

# Function to generate random short code
def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@router.post("/shorten")
def shorten_url(item: URLItem):
    short_code = generate_short_code()
    url_db[short_code] = item.original_url
    short_url = f"http://127.0.0.1:8000/{short_code}"
    return {"short_url": short_url, "original_url": item.original_url}

@router.get("/{short_code}")
def redirect_url(short_code: str):
    if short_code in url_db:
        return RedirectResponse(url_db[short_code])
    raise HTTPException(status_code=404, detail="Short URL not found")
