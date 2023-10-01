"""Représentation de la personnalité d'une personne."""

# -------------------------------- IMPORTS ------------------------------------
from enum import Enum
from typing import Self

from tribes.utils.random import gauss01
from tribes.utils import (
    CappedFloat_0_1,
)

# ---------------------------------- UTILS ------------------------------------
def _random_trait(
        strategy : str = 'gaussian',
)->float:
    """Fonction qui renvoie une stratégie d'attribution aléatoire d'un trait 
    de personnalité.
    
    Returns : 
        float : Nombre aléatoire pour un trait de personnalité."""
    if strategy == 'gaussian':
        return gauss01()
    else:
        raise ValueError(f"'{strategy}' is unknown.")

class PersonalityTraitEnum(Enum):
    """Enumération des axes différents de personnalités."""
    EXTRAVERTED     = 'Extraverted'
    EXPRESSIVE      = 'Expressive'
    SERIOUS         = 'Serious'
    LOGICAL         = 'Logical'
    CAUTIOUS        = 'Cautious'
    INDEPENDENT     = 'Independent'
    OPTIMISTIC      = 'Optimistic'
    CREATIVE        = 'Creative'
    EMPATHETIC      = 'Empathetic'
    CONFIDENT       = 'Confident'
    PATIENT         = 'Patient'
    TOLERANT        = 'Tolerant'
    UNPREDICTABLE   = 'Unpredictable'
    COOPERATIVE     = 'Cooperative'
    AMBITIOUS       = 'Ambitious'
    PERFECTIONIST   = 'Perfectionist'
    ORGANIZED       = 'Organized'
    OPENMINDED      = 'Openminded'
    HUMBLE          = 'Humble'
    GENEROUS        = 'Generous'
    FORGIVING       = 'Forgiving'
    HONEST          = 'Honest'
    GRATEFUL        = 'Grateful'
    LOYAL           = 'Loyal'

# -------------------------------- CLASSE -------------------------------------
class Personality :
    """Structure de donnée d'une personnalité."""
    def __init__(
            self,
            Extraverted     : float | CappedFloat_0_1 = _random_trait(), 
            Expressive      : float | CappedFloat_0_1 = _random_trait(), 
            Serious         : float | CappedFloat_0_1 = _random_trait(), 
            Logical         : float | CappedFloat_0_1 = _random_trait(), 
            Cautious        : float | CappedFloat_0_1 = _random_trait(), 
            Independent     : float | CappedFloat_0_1 = _random_trait(), 
            Optimistic      : float | CappedFloat_0_1 = _random_trait(), 
            Creative        : float | CappedFloat_0_1 = _random_trait(), 
            Empathetic      : float | CappedFloat_0_1 = _random_trait(), 
            Confident       : float | CappedFloat_0_1 = _random_trait(), 
            Patient         : float | CappedFloat_0_1 = _random_trait(), 
            Tolerant        : float | CappedFloat_0_1 = _random_trait(), 
            Unpredictable   : float | CappedFloat_0_1 = _random_trait(), 
            Cooperative     : float | CappedFloat_0_1 = _random_trait(), 
            Ambitious       : float | CappedFloat_0_1 = _random_trait(), 
            Perfectionist   : float | CappedFloat_0_1 = _random_trait(), 
            Organized       : float | CappedFloat_0_1 = _random_trait(), 
            Openminded      : float | CappedFloat_0_1 = _random_trait(), 
            Humble          : float | CappedFloat_0_1 = _random_trait(), 
            Generous        : float | CappedFloat_0_1 = _random_trait(), 
            Forgiving       : float | CappedFloat_0_1 = _random_trait(), 
            Honest          : float | CappedFloat_0_1 = _random_trait(), 
            Grateful        : float | CappedFloat_0_1 = _random_trait(), 
            Loyal           : float | CappedFloat_0_1 = _random_trait(), 
    ):
        
        # --- Attributes --- 

        # Construction d'un dictionnaire intermédiaire 
        _personality = {
            PersonalityTraitEnum.EXTRAVERTED     : Extraverted  ,
            PersonalityTraitEnum.EXPRESSIVE      : Expressive   ,
            PersonalityTraitEnum.SERIOUS         : Serious      ,
            PersonalityTraitEnum.LOGICAL         : Logical      ,
            PersonalityTraitEnum.CAUTIOUS        : Cautious     ,
            PersonalityTraitEnum.INDEPENDENT     : Independent  ,
            PersonalityTraitEnum.OPTIMISTIC      : Optimistic   ,
            PersonalityTraitEnum.CREATIVE        : Creative     ,
            PersonalityTraitEnum.EMPATHETIC      : Empathetic   ,
            PersonalityTraitEnum.CONFIDENT       : Confident    ,
            PersonalityTraitEnum.PATIENT         : Patient      ,
            PersonalityTraitEnum.TOLERANT        : Tolerant     ,
            PersonalityTraitEnum.UNPREDICTABLE   : Unpredictable,
            PersonalityTraitEnum.COOPERATIVE     : Cooperative  ,
            PersonalityTraitEnum.AMBITIOUS       : Ambitious    ,
            PersonalityTraitEnum.PERFECTIONIST   : Perfectionist,
            PersonalityTraitEnum.ORGANIZED       : Organized    ,
            PersonalityTraitEnum.OPENMINDED      : Openminded   ,
            PersonalityTraitEnum.HUMBLE          : Humble       ,
            PersonalityTraitEnum.GENEROUS        : Generous     ,
            PersonalityTraitEnum.FORGIVING       : Forgiving    ,
            PersonalityTraitEnum.HONEST          : Honest       ,
            PersonalityTraitEnum.GRATEFUL        : Grateful     ,
            PersonalityTraitEnum.LOYAL           : Loyal        ,
        }

        # Construction de l'attribut personality à partir du dictionnaire 
        # intermédiaire.
        self.personality = {
            _trait.value:CappedFloat_0_1.cast_to_number(
                value=_value
            )
            for _trait, _value in _personality.items()
        }
    
    @classmethod
    def random_personnality(cls, )->Self:
        """Renvoie une personnalité randomisée.

        Returns:
            Self: Personnalité randomisée.
        """

        # Création des arguments pour le constructeur, génération aléatoire
        attributes = {}
        for trait in PersonalityTraitEnum:
            attributes[trait.value] = _random_trait()
        
        # Appel du constructeur avec ces arguments
        return Personality(**attributes)