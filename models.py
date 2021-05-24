from dataclasses import dataclass

@dataclass
class Country:
    id: str
    short_name: str

@dataclass
class Indicator:
    id: str
    description: str

@dataclass
class Records:
    id: str    
    country_id:str
    indicator_id:str
    year: str
    value: int

