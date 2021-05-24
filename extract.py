from dataclasses import dataclass
from models import Country, Indicator, Records
import csv

#First test reading csv line by line
countries = []
identicators = []
records = []


with open("/home/karel/fastapi-demo/data/SDGCountry.csv") as f:
    reader = csv.reader(f)
    for i, col in enumerate(reader):
        #print(i, col[0])
        country = Country(id=col[0], short_name=col[1])
        countries.append(country)


with open("/home/karel/fastapi-demo/data/SDGSeries.csv") as f:
    reader = csv.reader(f)
    for i, col in enumerate(reader):
        #print(i, col[0])
        identicator = Indicator(id=col[0], description=col[2])
        identicators.append(identicator)

with open("/home/karel/fastapi-demo/data/SDGData.csv") as f:
    reader = csv.reader(f)
    for i, col in enumerate(reader):
        
    #print(i, col[0])
        record = Records(id_rec=i, country_id=col[1], indicator_id=col[3])
        records.append(record)

print("end")


           



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
