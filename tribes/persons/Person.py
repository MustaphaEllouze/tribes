from dataclasses import dataclass, field

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


def default_hunger()->CappedFloat_0_1:
    return CappedFloat_0_1(1.0)

def default_thirst()->CappedFloat_0_1:
    return CappedFloat_0_1(1.0)

def default_happiness()->CappedFloat_0_1:
    return CappedFloat_0_1(1.0)

def default_fertility()->CappedFloat_0_1:
    return CappedFloat_0_1(0.0)

def default_reputation()->CappedFloat_0_1:
    return CappedFloat_0_1(1.0)

@dataclass
class Person :
    name                : str 
    age                 : Age       
    height              : Height     
    weight              : Weight     
    race                : Race
    gender              : GenderEnum
    hierarchy           : HierarchyEnum
    skills              : list[SkillEnum]
    job                 : list[JobEnum]
    medical_condition   : list[MedicalConditionEnum]
    personality_traits  : Personality = Personality.random_personnality()
    deceased            : bool = False
    hunger              : CappedFloat_0_1   = field(default_factory=default_hunger)
    thirst              : CappedFloat_0_1   = field(default_factory=default_thirst)
    happiness           : CappedFloat_0_1   = field(default_factory=default_happiness)
    fertility           : CappedFloat_0_1   = field(default_factory=default_fertility)
    reputation          : CappedFloat_0_1   = field(default_factory=default_reputation)
