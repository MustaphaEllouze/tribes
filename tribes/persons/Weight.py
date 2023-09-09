from dataclasses import dataclass

from tribes.utils import (
    PositiveFloat,
)

NB_FLOATING = 3

@dataclass
class Weight:
    """In kg"""
    weight : float

    def __post_init__(
            self,
    ):
        self.value_container = PositiveFloat(value=self.weight)

    @property
    def value(self):
        return self.value_container.value
    
    @value.setter
    def value(self, a_value : float):
        self.value_container.value = a_value
    
    def __str__(self, ):
        return f'{round(self.value, ndigits=NB_FLOATING)}kg'

    def add_mass(self, mass_rate : float = 0.0):
        self.value += mass_rate
    
    def add_mass_in_g(self, mass_rate : float = 0.0):
        self.value += mass_rate/1000
    
    def remove_mass(self, mass_rate : float = 0.0):
        self.add_mass(mass_rate=-mass_rate)
    
    def remove_mass_in_g(self, mass_rate : float = 0.0):
        self.add_mass_in_g(mass_rate=-mass_rate)