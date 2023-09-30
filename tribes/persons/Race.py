"""Gestion des caractéristiques générales des races."""

# -------------------------------- IMPORTS ------------------------------------
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

# --------------------------------- CLASSE ------------------------------------

@dataclass
class Race :
    """Définition des races"""

    # Taille cible
    male_height           : Height
    female_height         : Height
    
    # Poids cible
    male_weight           : Weight
    female_weight         : Weight
    
    # Age à la mort cible
    male_lifespan         : Age
    female_lifespan       : Age
    
    # Age cible auquel la race peut procréer
    sex_mature_age_male   : Age
    sex_mature_age_female : Age

    # Age cible auquel la race atteint son corps d'adulte
    mature_age_male       : Age
    mature_age_female     : Age

    # Temps de gestation
    gestation_time        : Age

    # Nombre moyen d'enfants par gestation 
    number_of_children    : FloatSuperiorTo_1

    # Chances d'avoir des enfants à chaque "rencontre"
    reproductive_rate     : CappedFloat_0_1
    
    # Equilibre du régime alimentaire. La somme des trois ratios doit valoir
    #   1.
    carnivorous_rate      : CappedFloat_0_1
    herbivorous_rate      : CappedFloat_0_1
    insectivorous_rate    : CappedFloat_0_1

    # Equilibre de la composition physique. La somme des trois ratios doit 
    # valoir 1.
    muscle_ratio          : CappedFloat_0_1
    bone_ratio            : CappedFloat_0_1
    organs_ratio          : CappedFloat_0_1

    # Détermine à quelle vitesse est-ce que les calories sont brulées
    metabolic_rate        : CappedFloat_0_1

    # Cible des BPM du coeur
    heart_rate            : PositiveFloat

    def __post_init__(self):
        """Vérification de la validité des arguments"""

        # Vérification que le régime alimentaire somme à 1
        if self.carnivorous_rate +\
            self.herbivorous_rate +\
            self.insectivorous_rate != 1: 
            raise ValueError("carnivorous_rate"\
                            "+herbivorous_rate+insectivorous_rate"\
                            " should be equal to 1.")
        
        # Vérification que la composition physique somme à 1
        if self.muscle_ratio +\
            self.bone_ratio +\
            self.organs_ratio != 1: 
            raise ValueError("muscle_ratio"\
                            "+bone_ratio+organs_ratio"\
                            " should be equal to 1.")


