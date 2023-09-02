from dataclasses import dataclass

from tribes.utils import CappedFloat

from tribes.persons import (
    SkillEnum, 
    GenderEnum,
    MedicalConditionEnum,
    JobEnum,
    HierarchyEnum,
    Personality,
    Race,
    Height,
)

@dataclass
class Person :
    name                : str 
    age                 : int       
    height              : Height     
    weight              : float     
    deceased            : bool
    hunger              : CappedFloat
    thirst              : CappedFloat
    happiness           : CappedFloat
    fertility           : CappedFloat
    reputation          : CappedFloat
    race                : Race
    gender              : GenderEnum
    hierarchy           : HierarchyEnum
    personality_traits  : Personality
    skills              : list[SkillEnum]
    job                 : list[JobEnum]
    medical_condition   : list[MedicalConditionEnum]