"""Gestion du temps."""

# -------------------------------- IMPORTS ------------------------------------
from enum import Enum

from tribes.utils import (
    PositiveFloat,
)

# ---------------------------------- UTILS ------------------------------------
class FormatTime(Enum):
    YEARS   = 'years'
    MONTHS  = 'months'
    DAYS    = 'days'

YEARS_TO_MONTHS = 12
YEARS_TO_DAYS   = 365

# --------------------------------- CLASSE ------------------------------------
class Time:
    """Représentation du temps. Unité = années.
    La valeur est nécessairement positive."""

    def __init__(
        self,
        value:float|int
    )->None:
        """
        Args:
            value (float | int): temps en années. Si la valeur est négative,
            elle sera prise égale à zéro.
        """
        self.__encapsulated_value = PositiveFloat(value=value)
    
    @property
    def value(self, )->float :
        return self.__encapsulated_value.get_value()

    def __get_time_in_ymd(self, )->tuple[int, int, int]:
        """Renvoie le temps en années, mois et jours.

        Returns:
            tuple[int, int, int]: années, mois, jours
        """
        
        # Âge entier
        total_time = self.value

        # Années = partie entière
        years = int(total_time)        

        # Mois = Partie entière de ce qui reste (* facteur de conversion)
        months = int((total_time-years)*YEARS_TO_MONTHS)

        # Jours = même principes
        days = int((total_time-years-months/YEARS_TO_MONTHS)*YEARS_TO_DAYS)

        # Résultat
        return years, months, days
    
    def __get_time_in_months_days(self, )->tuple[int, int]:
        """Renvoie le temps en mois et en jours.

        Returns:
            tuple[int, int]: Mois, jours.
        """

        # Âge entier
        total_time = self.value

        # Mois = Partie entière (*facteur de conversion)
        months = int(total_time*YEARS_TO_MONTHS)

        # Jours = Ce qui reste 
        days = int((total_time-months/YEARS_TO_MONTHS)*YEARS_TO_DAYS)

        # Résultat
        return months, days

    def __get_age_in_days(self, )->int:
        """Renvoie le temps en jours

        Returns:
            int: Temps en jours
        """

        return int(self.value*YEARS_TO_DAYS)

    def to_str(
        self, 
        format:str=FormatTime.YEARS.value
    )->str :
        """Renvoie une représentation en chaîne de caractères. Différents
        formats sont possibles.

        Args:
            format (str, optional): Format d'impression. Defaults to 'years'. 

        Returns:
            str: Représentation en chaîne de caractéères.
        """

        match format :

            case FormatTime.DAYS.value : 
                return f'{self.__get_age_in_days()} days'

            case FormatTime.MONTHS.value :
                months, days = self.__get_time_in_months_days()
                return f'{months} months {days} days'

            case FormatTime.YEARS.value : 
                years, months, days = self.__get_time_in_ymd()
                return f'{years} years {months} months {days} days'
            
            case _ :
                authorized_values = [
                    e.value 
                    for e in FormatTime._member_map_.values()
                ]
                raise ValueError(f'Authorized values are {authorized_values}') 

    def __str__(self):
        """Renvoie une représentation en années"""
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
        self.__encapsulated_value += time
    
    def substract_time(
        self, 
        time:float=0.0,
    )->None:
        """
        Soustrait du temps, en années
        Args:
            time (float, optional): Temps à soustraire. Defaults to 0.0.
        """
        self.__encapsulated_value -= time

    def add_time_in_months(
        self, 
        time:float=0.0,
    )->None:
        """
        Ajoute du temps, en mois

        Args:
            time (float, optional): Temps à rajouter. Defaults to 0.0.
        """
        self.__encapsulated_value += time/YEARS_TO_MONTHS
    
    def substract_time_in_months(
        self, 
        time:float=0.0,
    )->None:
        """
        Soustrait du temps, en mois
        Args:
            time (float, optional): Temps à soustraire. Defaults to 0.0.
        """
        self.__encapsulated_value -= time/YEARS_TO_MONTHS
    
    
    def add_time_in_days(
        self, 
        time:float=0.0,
    )->None:
        """
        Ajoute du temps, en jours

        Args:
            time (float, optional): Temps à rajouter. Defaults to 0.0.
        """
        self.__encapsulated_value += time/YEARS_TO_DAYS
    
    def substract_time_in_days(
        self, 
        time:float=0.0,
    )->None:
        """
        Soustrait du temps, en jours
        Args:
            time (float, optional): Temps à soustraire. Defaults to 0.0.
        """
        self.__encapsulated_value -= time/YEARS_TO_DAYS
        