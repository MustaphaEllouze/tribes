from enum import Enum

from tribes.utils.random import gauss01

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
            Extraverted     : float, 
            Expressive      : float, 
            Serious         : float, 
            Logical         : float, 
            Cautious        : float, 
            Independent     : float, 
            Optimistic      : float, 
            Creative        : float, 
            Empathetic      : float, 
            Confident       : float, 
            Patient         : float, 
            Tolerant        : float, 
            Unpredictable   : float, 
            Cooperative     : float, 
            Ambitious       : float, 
            Perfectionist   : float, 
            Organized       : float, 
            Openminded      : float, 
            Humble          : float, 
            Generous        : float, 
            Forgiving       : float, 
            Honest          : float, 
            Grateful        : float, 
            Loyal           : float, 
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
    
    @classmethod
    def random_personnality(cls, ):
        attributes = {}
        for trait in PersonalityTraitEnum:
            attributes[trait.value] = gauss01()
        
        return Personality(**attributes)