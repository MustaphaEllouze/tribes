from dataclasses import dataclass

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
    Height,
    Weight,
    Age,
)

@dataclass
class Person :
    name                : str 
    age                 : Age       
    height              : Height     
    weight              : Weight     
    deceased            : bool
    hunger              : CappedFloat_0_1
    thirst              : CappedFloat_0_1
    happiness           : CappedFloat_0_1
    fertility           : CappedFloat_0_1
    reputation          : CappedFloat_0_1
    race                : Race
    gender              : GenderEnum
    hierarchy           : HierarchyEnum
    skills              : list[SkillEnum]
    job                 : list[JobEnum]
    medical_condition   : list[MedicalConditionEnum]
    personality_traits  : Personality = Personality.random_personnality()