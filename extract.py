from dataclasses import dataclass
from models import Country, Indicator, Records
import csv

#First test reading csv line by line


def extract_countries():
    print("Extracting countries...")
    countries = {}
    with open("/home/karel/fastapi-demo/data/SDGCountry.csv") as f:
        reader = csv.reader(f)
        for i, col in enumerate(reader):
            countries[col[0]] = Country(id=col[0], short_name=col[1])

    print(f"Extracted {len(countries)} countries")
    return countries


# with open("/home/karel/fastapi-demo/data/SDGSeries.csv") as f:
# identicators = [] 
#     reader = csv.reader(f)
#     for i, col in enumerate(reader):
#         identicator = Indicator(id=col[0], description=col[2])
#         identicators.append(identicator)

# with open("/home/karel/fastapi-demo/data/SDGData.csv") as f:
#     reader = csv.reader(f)
#     for i, col in enumerate(reader):
#         record = Records(id_rec=i, country_id=col[1], indicator_id=col[3])
#         records.append(record)


           



# Dataclass representation
#test_dataclass = Country(id="NLD", short_name="Netherlands")
#print(test_dataclass)


# Dictionary representation
#test_dict = {
#    "id": "NLD",
#    "short_name": "Netherlands"
#}
#print(test_dict)


# Start with CSV -> Store in Data
