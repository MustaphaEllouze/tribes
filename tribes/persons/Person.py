"""Gestion de la structure de données centrale du module"""

# -------------------------------- IMPORTS ------------------------------------

from dataclasses import dataclass, field

from tribes.utils import (
    CappedFloat_0_1, 
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

# -------------------------------- CLASSE -------------------------------------
@dataclass
class Person :
    """Représente une personne. Structure de donnée centrale du module."""

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
    skills              : list[SkillEnum]

    # Liste des travaux endossés par la personne 
    job                 : list[JobEnum]

    # Liste des problèmes médicaux de la personne 
    medical_condition   : list[MedicalConditionEnum]

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
