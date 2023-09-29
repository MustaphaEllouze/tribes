from enum import Enum

from tribes.utils import (
    PositiveFloat,
)

class FormatAge(Enum):
    YEARS  = 'years'
    MONTHS = 'months'
    DAYS   = 'days'

YEARS_TO_MONTHS = 12
YEARS_TO_DAYS   = 365

class Age(PositiveFloat):
    """in years"""

    def __str__(self, format:str=FormatAge.YEARS.value):
        
        match format :
            
            case FormatAge.DAYS.value :
                return f'{self.get_age_in_days()} days'
            
            case FormatAge.MONTHS.value :
                months, days = self.get_age_in_months_days()
                return f'{months} months {days} days'
            
            case FormatAge.YEARS.value :
                years, months, days = self.get_age_in_ymd()
                return f'{years} years {months} months {days} days'


    def get_age_in_ymd(self)->tuple[int, int, int]:
        total_age = self.value
        years = int(self.value)
        months = int((total_age-years)*YEARS_TO_MONTHS)
        days = int((total_age-years-months/YEARS_TO_MONTHS)*YEARS_TO_DAYS)

        return years, months, days

    def get_age_in_months_days(self)->tuple[int, int]:
        total_age = self.value
        months = int(total_age*YEARS_TO_MONTHS)
        days = int((total_age-months/YEARS_TO_MONTHS)*YEARS_TO_DAYS)

        return months, days

    def get_age_in_days(self)->int :
        return int(self.value*YEARS_TO_DAYS)

    def add_age(self, age : float = 0.0):
        self.value += age
    
    def add_age_in_months(self, age : float = 0.0):
        self.value += age/12
    
    def add_age_in_days(self, age : float = 0.0):
        self.value += age/365