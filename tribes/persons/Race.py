from dataclasses import dataclass

from tribes.utils import (
    Height,
    Weight,
    Age,
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
    
    male_lifespan         : Age
    female_lifespan       : Age
    
    sex_mature_age_male   : Age
    sex_mature_age_female : Age

    mature_age_male       : Age
    mature_age_female     : Age

    gestation_time        : Age
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

    def __post_init__(self):
        if self.carnivorous_rate +\
            self.herbivorous_rate +\
            self.insectivorous_rate != 1: 
            raise ValueError("carnivorous_rate"\
                            "+herbivorous_rate+insectivorous_rate"\
                            " should be equal to 1.")
        
        if self.muscle_ratio +\
            self.bone_ratio +\
            self.organs_ratio != 1: 
            raise ValueError("muscle_ratio"\
                            "+bone_ratio+organs_ratio"\
                            " should be equal to 1.")


