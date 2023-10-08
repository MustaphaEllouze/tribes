"""Gestion de l'âge des personnes"""

# -------------------------------- IMPORTS ------------------------------------
from enum import Enum

from tribes.utils import (
    Time, FormatTime
)

# --------------------------------- CLASSE ------------------------------------
class Age:
    """Représente l'âge de quelque chose."""

    def __init__(
        self, 
        value:float|int,
    )->None:
        self.__encapsulated_time = Time(value=value)
    
    @property
    def value(self, )->float:
        return self.__encapsulated_time.value

    def to_str(
        self, 
        format:str=FormatTime.YEARS.value,
    )->str:
        """Renvoie une représentation en chaîne de caractères. Différents
        formats sont possibles.

        Args:
            format (str, optional): Format d'impression. Defaults to 'years'.

        Returns:
            str: Représentation en chaîne de caractères.
        """
        return self.__encapsulated_time.to_str(format=format)

    def __str__(self) -> str:
        return self.to_str(format=FormatTime.YEARS.value)
    
    def add_time(
        self, 
        time:float=0.0,
    )->None:
        """
        Ajoute du temps, en années

        Args:
            time (float, optional): Temps à rajouter. Defaults to 0.0.
        """
        self.__encapsulated_time.add_time(time=time)
    
    def add_time_in_months(
        self, 
        time:float=0.0,
    )->None:
        """
        Ajoute du temps, en mois

        Args:
            time (float, optional): Temps à rajouter. Defaults to 0.0.
        """
        self.__encapsulated_time.add_time_in_months(time=time)
    
    def add_time_in_days(
        self, 
        time:float=0.0,
    )->None:
        """
        Ajoute du temps, en jours

        Args:
            time (float, optional): Temps à rajouter. Defaults to 0.0.
        """
        self.__encapsulated_time.add_time_in_days(time=time)

    