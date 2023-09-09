from dataclasses import dataclass

from tribes.persons import (
    Height,
    Weight,
)

from tribes.utils import (
    CappedFloat_0_1,
    PositiveFloat,
    FloatSuperiorTo_1,
)

@dataclass
class Race :
    male_height           : Height
    female_height         : Height
    
    male_weight           : Weight
    female_weight         : Weight
    
    male_lifespan         : PositiveFloat
    female_lifespan       : PositiveFloat
    
    sex_mature_age_male   : PositiveFloat
    sex_mature_age_female : PositiveFloat

    mature_age_male       : PositiveFloat
    mature_age_female     : PositiveFloat

    gestation_time        : PositiveFloat
    number_of_children    : FloatSuperiorTo_1

    reproductive_rate     : CappedFloat_0_1
    
    carnivorous_rate      : CappedFloat_0_1
    herbivorous_rate      : CappedFloat_0_1
    insectivorous_rate    : CappedFloat_0_1

    muscle_ratio          : CappedFloat_0_1
    bone_ratio            : CappedFloat_0_1
    organs_ratio          : CappedFloat_0_1

    metabolic_rate        : CappedFloat_0_1

    heart_rate            : PositiveFloat