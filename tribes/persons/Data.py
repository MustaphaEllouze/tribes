from tribes.utils import (
    FloatSuperiorTo_1, 
    CappedFloat_0_1, 
    PositiveFloat,
)

from tribes.persons import (
    Race, 
    Height, 
    Weight, 
    Age, 
)

# -----------------------------------------------------------
HUMAN = Race(
    male_height             =   Height(1.78),
    female_height           =   Height(1.65),
    male_weight             =   Weight(65),
    female_weight           =   Weight(55),
    male_lifespan           =   Age(75),
    female_lifespan         =   Age(82),
    sex_mature_age_male     =   Age(14),
    sex_mature_age_female   =   Age(13),
    mature_age_male         =   Age(21),
    mature_age_female       =   Age(19),
    gestation_time          =   Age(0.75),
    number_of_children      =   FloatSuperiorTo_1(1.02),
    reproductive_rate       =   CappedFloat_0_1(1.0),
    carnivorous_rate        =   CappedFloat_0_1(0.30),
    herbivorous_rate        =   CappedFloat_0_1(0.65),
    insectivorous_rate      =   CappedFloat_0_1(0.05),
    muscle_ratio            =   CappedFloat_0_1(0.25),
    bone_ratio              =   CappedFloat_0_1(0.33),
    organs_ratio            =   CappedFloat_0_1(0.42),
    metabolic_rate          =   CappedFloat_0_1(1.0),
    heart_rate              =   PositiveFloat(70),
)