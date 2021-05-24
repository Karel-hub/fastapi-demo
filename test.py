from extract import extract_countries, extract_records


# Populate data
countries = extract_countries()

country_keys = list(countries.keys())
country_values = list(countries.values())

records = extract_records()

print("end")