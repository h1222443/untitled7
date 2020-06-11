from dataclasses import dataclass
from datetime import datetime


@dataclass
class data:
    class_ : str
    name : str
    sex :bool
    age : int
    salary : int
    time : datetime

    def __post_init__(self):
        self.symbol = f'{self.class_}.{self.name}'
