from dataclasses import asdict
from typing import Optional
from fastapi import FastAPI

from extract import extract_countries

app = FastAPI()

# Populate data
countries = extract_countries()

@app.get("/")
def read_root():
    return {"Hello": "Karel"}

@app.get("/countries")
def read_countries():
    return [asdict(country) for country in countries]


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
