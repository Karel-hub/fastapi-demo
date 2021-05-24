from dataclasses import asdict
from fastapi import FastAPI

from extract import extract_countries, extract_records

app = FastAPI()

# Populate data
countries = extract_countries()
records = extract_records()

@app.get("/")
def read_root():
    return {"Hello": "Karel"}

@app.get("/countries")
def list_countries():
    return [asdict(country) for country in countries.values()]


@app.get("/country/{item_id}")
def get_country(item_id: str):
    return countries[item_id]

@app.get("/record/{item_id}")
def get_record(item_id: int):
    return records[item_id]
    
@app.get("/record/{country_id}/{year}")
def find_record(country_id: str, year: int):
    """
    Find record from country ID and year
    """

    for r in records.values():
        if r.country_id == country_id and r.year == year:
            return r

    return None
