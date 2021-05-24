from dataclasses import asdict
from extract import extract_countries


# Populate data
countries = extract_countries()

country_keys = list(countries.keys())
country_values = list(countries.values())

print("end")