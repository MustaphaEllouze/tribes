"""Gestion d'une taille"""

# -------------------------------- IMPORTS ------------------------------------
from tribes.utils import (
    PositiveFloat,
)

# --------------------------------- CLASSE ------------------------------------
class Height:
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
        # Ecriture différente en fonction de la valeur de la taille (valeur 
        # seuil = 1m)
        if self.value < 1 :
            return f'{int(self.value*100)} cm'
        else:
            return f'{int(self.value)}m {int(self.value*100)%100}'

    def add_height(
        self, 
        height_rate : float = 0.0,
    )->None:
        """
        Args:
            mass_rate (height_rate, optional): Taille à ajouter, en mètres.
            Defaults to 0.0.
        """
        self.__encapsulated_value += height_rate
    
    def add_height_in_cm(
        self, 
        height_rate : float = 0.0,
    )->None:
        """
        Args:
            mass_rate (height_rate, optional): Taille à ajouter, en centimètre.
            Defaults to 0.0.
        """
        self.__encapsulated_value += height_rate/100
    
    def remove_height(
        self, 
        height_rate : float = 0.0,
    )->None:
        """
        Args:
            mass_rate (height_rate, optional): Taille à enlever, en mètres.
            Defaults to 0.0.
        """
        self.add_height(height_rate=-height_rate)
    
    def remove_height_in_cm(
        self, 
        height_rate : float = 0.0,
    )->None:
        """
        Args:
            mass_rate (height_rate, optional): Taille à enelever, en centimètre
            . Defaults to 0.0.
        """
        self.add_height_in_cm(height_rate=-height_rate)