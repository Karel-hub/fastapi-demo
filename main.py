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
def list_countries():
    return [asdict(country) for country in countries.values()]


@app.get("/country/{item_id}")
def get_country(item_id: str):
    return countries[item_id]
