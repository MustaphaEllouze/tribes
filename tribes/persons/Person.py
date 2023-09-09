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
)

@dataclass
class Person :
    name                : str 
    age                 : PositiveFloat       
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
    personality_traits  : Personality
    skills              : list[SkillEnum]
    job                 : list[JobEnum]
    medical_condition   : list[MedicalConditionEnum]