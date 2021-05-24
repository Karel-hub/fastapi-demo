from dataclasses import dataclass
from models import Country, Indicator, Records
import csv

#First test reading csv line by line


def extract_countries():
    print("Extracting countries...")
    countries = {}
    with open("/home/karel/fastapi-demo/data/SDGCountry.csv") as f:
        reader = csv.reader(f)
        for i, cols in enumerate(reader):
            if not i == 0:
                countries[cols[0]] = Country(id=cols[0], short_name=cols[1])

    print(f"Extracted {len(countries)} countries")
    return countries


# with open("/home/karel/fastapi-demo/data/SDGSeries.csv") as f:
# identicators = [] 
#     reader = csv.reader(f)
#     for i, col in enumerate(reader):
#         identicator = Indicator(id=col[0], description=col[2])
#         identicators.append(identicator)

def extract_records():
    with open("/home/karel/fastapi-demo/data/SDGData.csv") as f:
        records = {}
        reader = csv.reader(f)
        header_row = []
        for i, cols in enumerate(reader):
            if i == 0:
                header_row = cols
            elif i > 10:
                break
            else:
                for col_ind in range(4, 34):
                    records[i-1] = Records(
                        id=i-1,
                        country_id=cols[1],
                        indicator_id=cols[3],
                        year=int(header_row[col_ind]),
                        value=cols[col_ind]
                    )
        
        return records


test_records = extract_records()
print(test_records)

           



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
