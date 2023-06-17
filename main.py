from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from resources.key_generating_service import generate_short_url
from fastapi.responses import RedirectResponse
from temp_db import url_store

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/shorten")
async def shorten_url(url_request: str):
    short_url = generate_short_url()
    url_store[short_url] = url_request
    return {"short_url": short_url}

@app.get("/{short_url}")
async def redirect_to_original_url(short_url: str):
    if short_url in url_store:
        original_url = url_store[short_url]
        return RedirectResponse(url=original_url)
    else:
        raise HTTPException(status_code=404, detail="Short URL not found")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)