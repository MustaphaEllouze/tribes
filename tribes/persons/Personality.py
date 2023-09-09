from enum import Enum

from tribes.utils.random import gauss01
from tribes.utils import (
    CappedFloat_0_1,
)

class PersonalityTraitEnum(Enum):
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

class Personality :
    def __init__(
            self,
            Extraverted     : float | CappedFloat_0_1, 
            Expressive      : float | CappedFloat_0_1, 
            Serious         : float | CappedFloat_0_1, 
            Logical         : float | CappedFloat_0_1, 
            Cautious        : float | CappedFloat_0_1, 
            Independent     : float | CappedFloat_0_1, 
            Optimistic      : float | CappedFloat_0_1, 
            Creative        : float | CappedFloat_0_1, 
            Empathetic      : float | CappedFloat_0_1, 
            Confident       : float | CappedFloat_0_1, 
            Patient         : float | CappedFloat_0_1, 
            Tolerant        : float | CappedFloat_0_1, 
            Unpredictable   : float | CappedFloat_0_1, 
            Cooperative     : float | CappedFloat_0_1, 
            Ambitious       : float | CappedFloat_0_1, 
            Perfectionist   : float | CappedFloat_0_1, 
            Organized       : float | CappedFloat_0_1, 
            Openminded      : float | CappedFloat_0_1, 
            Humble          : float | CappedFloat_0_1, 
            Generous        : float | CappedFloat_0_1, 
            Forgiving       : float | CappedFloat_0_1, 
            Honest          : float | CappedFloat_0_1, 
            Grateful        : float | CappedFloat_0_1, 
            Loyal           : float | CappedFloat_0_1, 
    ):
        self.personality = {
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

        for personality, value in self.personality.items():
            self.personality[personality] = CappedFloat_0_1.cast_to_number(
                value=value,
            )
    
    @classmethod
    def random_personnality(cls, ):
        attributes = {}
        for trait in PersonalityTraitEnum:
            attributes[trait.value] = gauss01()
        
        return Personality(**attributes)