from tribes.utils import (
    PositiveFloat,
)

NB_FLOATING = 3

class Weight(PositiveFloat):
    """In kg"""
    
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