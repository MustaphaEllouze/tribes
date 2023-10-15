"""Gestion de la structure de données centrale du module"""

# -------------------------------- IMPORTS ------------------------------------

from dataclasses import dataclass, field
from enum import Enum
from typing import Iterable

from tribes.utils import (
    CappedFloat_0_1, 
    PositiveFloat,
)

from tribes.persons import (
    SkillEnum, 
    GenderEnum,
    MedicalConditionEnum,
    JobEnum,
    HierarchyEnum,
    Personality,
    Race,
)

from tribes.utils import (
    Age, 
    Height, 
    Weight,
)

# ---------------------------- UTILS FUNCTIONS --------------------------------

def default_hunger()->CappedFloat_0_1:
    """Default factory pour hunger"""
    return CappedFloat_0_1(1.0)

def default_thirst()->CappedFloat_0_1:
    """Default factory pour thirst"""
    return CappedFloat_0_1(1.0)

def default_happiness()->CappedFloat_0_1:
    """Default factory pour happiness"""
    return CappedFloat_0_1(1.0)

def default_fertility()->CappedFloat_0_1:
    """Default factory pour fertility"""
    return CappedFloat_0_1(0.0)

def default_reputation()->CappedFloat_0_1:
    """Default factory pour reputation"""
    return CappedFloat_0_1(1.0)


# ---------------------------- UTILS FUNCTIONS --------------------------------
class HeightUnits(Enum):
    M  = 'm'
    CM = 'cm'
    MM = 'mm'
class MassUnits(Enum):
    KG  = 'kg'
    G  = 'g'

# -------------------------------- CLASSE -------------------------------------
@dataclass
class Person :
    """Représente une personne. Structure de donnée centrale du module."""

    # -------------------------------------------------------------------------
    # Nom de la personne 
    name                : str 

    # Age de la personne 
    age                 : Age     

    # Taille de la personne   
    height              : Height     

    # Poids de la personne 
    weight              : Weight     

    # Race de la personne 
    race                : Race

    # Genre de la personne 
    gender              : GenderEnum

    # Position hiérarchique de la personne 
    hierarchy           : HierarchyEnum

    # Liste des compétences connues par la personne
    skills              : Iterable[SkillEnum]

    # Liste des travaux endossés par la personne 
    job                 : Iterable[JobEnum]

    # Liste des problèmes médicaux de la personne 
    medical_condition   : Iterable[MedicalConditionEnum]

    # Personnalité de la personne
    personality_traits  : Personality = Personality.random_personnality()

    # Détermine si la personne est décédée
    deceased            : bool = False

    # Faim de la personne
    hunger              : CappedFloat_0_1   = field(
                                            default_factory=default_hunger)
    
    # Soif de la personne
    thirst              : CappedFloat_0_1   = field(
                                            default_factory=default_thirst)
    
    # Joie de la personne
    happiness           : CappedFloat_0_1   = field(
                                            default_factory=default_happiness)
    
    # Fertilité de la personne
    fertility           : CappedFloat_0_1   = field(
                                            default_factory=default_fertility)
    
    # Réputation de la personne 
    reputation          : CappedFloat_0_1   = field(
                                            default_factory=default_reputation)
    
    # -------------------------------------------------------------------------

    def grow_older(
            self, 
            age : float | int,
    )->None:
        _add_age = PositiveFloat(value=age).cast_to_number()
        self.age.add_time(time=_add_age)
    
    def grow(
            self, 
            height_rate : float | int, 
            units : str = HeightUnits.M.value,
    )->None :
        raise NotImplementedError()
    
    def shrink(
            self, 
            height_rate : float | int, 
            units : str = HeightUnits.M.value,
    )->None :
        raise NotImplementedError()
    
    def gain_weight(
            self, 
            mass_rate : float | int, 
            units : str = HeightUnits.M.value,
    )->None :
        raise NotImplementedError()
    
    def lose_weight(
            self, 
            mass_rate : float | int, 
            units : str = HeightUnits.M.value,
    )->None :
        raise NotImplementedError()
    

    def set_hierarchy(
            self,
            hierarchy_level,
    )->None :
        raise NotImplementedError()
    
    def raise_in_hierarchy(
            self, 
            number_of_levels,
    )->None:
        raise NotImplementedError()
    
    def fall_in_hierarchy(
            self, 
            number_of_levels,
    )->None:
        raise NotImplementedError()
    
    def add_skill(
            self, 
            a_skill : SkillEnum,
    )->None:
        raise NotImplementedError()
    
    def add_skills(
            self, 
            list_of_skills : Iterable[SkillEnum],
    )->None:
        raise NotImplementedError()
    
    def remove_skill(
            self, 
            a_skill : SkillEnum,
    )->None:
        raise NotImplementedError()
    
    def remove_skills(
            self, 
            list_of_skills : Iterable[SkillEnum],
    )->None:
        raise NotImplementedError()
    

    def add_job(
            self, 
            a_job : JobEnum,
    )->None:
        raise NotImplementedError()
    
    def add_jobs(
            self, 
            list_of_jobs : Iterable[JobEnum],
    )->None:
        raise NotImplementedError()
    
    def remove_job(
            self, 
            a_job : JobEnum,
    )->None:
        raise NotImplementedError()
    
    def remove_jobs(
            self, 
            list_of_jobs : Iterable[JobEnum],
    )->None:
        raise NotImplementedError()
    
    def add_condition(
            self, 
            a_condition : MedicalConditionEnum,
    )->None:
        raise NotImplementedError()
    
    def add_conditions(
            self, 
            list_of_conditions : Iterable[MedicalConditionEnum],
    )->None:
        raise NotImplementedError()
    
    def remove_condition(
            self, 
            a_condition : MedicalConditionEnum,
    )->None:
        raise NotImplementedError()
    
    def remove_conditions(
            self, 
            list_of_conditions : Iterable[MedicalConditionEnum],
    )->None:
        raise NotImplementedError()
    
    def change_personnality(
            self, 
            personnality : Personality,
    )->None:
        raise NotImplementedError()

    def kill(
            self,
    )->None:
        raise NotImplementedError()
    
    def change_hunger(
            self, 
            rate : float | int,
    )->None :
        raise NotImplementedError()
    
    def change_thirst(
            self, 
            rate : float | int,
    )->None :
        raise NotImplementedError()
    
    def change_happiness(
            self, 
            rate : float | int,
    )->None :
        raise NotImplementedError()
    
    def change_fertility(
            self, 
            rate : float | int,
    )->None :
        raise NotImplementedError()
    
    def change_reputation(
            self, 
            rate : float | int,
    )->None :
        raise NotImplementedError()
    
