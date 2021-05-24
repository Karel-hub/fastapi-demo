from dataclasses import dataclass
from typing import Optional

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
    year: int
    value: float

