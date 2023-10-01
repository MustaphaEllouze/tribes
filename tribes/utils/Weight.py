"""Gestion du poids"""

# -------------------------------- IMPORTS ------------------------------------
from tribes.utils import (
    PositiveFloat,
)

# --------------------------------- UTILS ------------------------------------
NB_FLOATING = 3

# --------------------------------- CLASSE ------------------------------------
class Weight:
    """Représentation d'un poids, en kg"""
    
    def __init__(
        self, 
        value:int|float,
    ) -> None:
        """
        Args:
            value (int | float): Poids en kg
        """
        self.__encapsulated_value = PositiveFloat(value=value)
    
    @property
    def value(self, )->float :
        return self.__encapsulated_value.get_value()

    def __str__(self, ):
        return f'{round(self.value, ndigits=NB_FLOATING)}kg'

    def add_mass(
        self, 
        mass_rate : float = 0.0,
    )->None:
        """Rajoute de la masse, en kilo

        Args:
            mass_rate (float, optional): Masse à ajouter, en kilo.
            Defaults to 0.0.
        """
        self.__encapsulated_value += mass_rate
    
    def add_mass_in_g(
        self, 
        mass_rate : float = 0.0,
    )->None:
        """Rajoute de la masse, en grammes

        Args:
            mass_rate (float, optional): Masse à ajouter, en grammes.
            Defaults to 0.0.
        """
        self.__encapsulated_value += mass_rate/1000
    
    def remove_mass(
        self, 
        mass_rate : float = 0.0,
    )->None:
        """Enlève de la masse, en kilo

        Args:
            mass_rate (float, optional): Masse à enlever en kilo. 
            Defaults to 0.0.
        """
        self.add_mass(mass_rate=-mass_rate)
    
    def remove_mass_in_g(
        self, 
        mass_rate : float = 0.0,
    )->None:
        """Enlève de la masse, en grammes

        Args:
            mass_rate (float, optional): Masse à enlever, en grammes.
            Defaults to 0.0.
        """
        self.add_mass_in_g(mass_rate=-mass_rate)