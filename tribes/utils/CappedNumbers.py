"""Permet de générer des nombres avec bornes supérieres et inférieures."""

# -------------------------------- IMPORTS ------------------------------------
from dataclasses import dataclass
from typing import Self

# --------------------------------- CLASSE ------------------------------------
class CappedNumber :
    """Classe permettant de générer des sous-classes avec bornes inférieures 
    et supérieures."""

    def __new__(cls, *args, **kwargs) -> Self:
        """This class cannot be instanciated"""
        if cls is CappedNumber:
            raise NotImplementedError("Cannot instanciate CappedNumber.")
        return object.__new__(cls, *args, *kwargs)
    
    @classmethod
    def generate_type(
            self, 
            number_type : type        = float,
            min_val     : float | int = None,
            max_val     : float | int = None,
    ):
        """Renvoie une classe dont le comportement est identique à float ou int
        , qui inclut une gestion de bornes supérieure et inférieure. Chaque
        opération fait en sorte de renvoyer une des deux bornes en cas 
        d'overflow.

        Args:
            number_type (type, optional): Classe à laquelle doit ressembler 
            le résultat (float ou int). Defaults to float.

            min_val (float | int, optional): Borne inférieure. 
            Defaults to None.

            max_val (float | int, optional): Borne supérieure.
            Defaults to None.

        Returns:
            type: Une classe se comportant comme number_type et implémentant 
            automatiquement une gestion des bornes supérieure et inférieure.
        """
        
        
        class CappedClass : 
            """Classe de retour
            """

            # Attributs de classe : bornes supérieure et inférieure
            min_value   : float | int  = min_val
            max_value   : float | int  = max_val

            def __init__(
                    self, 
                    value : float | int,
            ):
                """
                Args:
                    value (float | int): La valeur. Peut dépasser les bornes.
                """
                _value = value

                # Si les bornes suéprieur et inférieure sont définies, on 
                # replace la valeur dans le bon intervalle
                if CappedClass.min_value is not None : 
                    _value = max(_value, CappedClass.min_value)
                if CappedClass.max_value is not None : 
                    _value = min(_value, CappedClass.max_value)
                
                # Attribut
                self.value      = number_type(_value)
            
            def __str__(self) -> str:
                return f"{self.value}"
            
            @classmethod
            def cast_to_number(
                cls,
                value : number_type | Self,
            )->number_type:
                """Permet de convertir des nombre et des CappedClass en nombre

                Args:
                    value (number_type | Self): La valeur à convertir

                Returns:
                    number_type: Valeur convertie
                """

                # On récupère la valeur s'il y a lieu
                if isinstance(value, CappedClass):
                    true_value = value.value
                elif isinstance(value, (float, int)):
                    true_value = value
                else:
                    raise NotImplementedError()
                
                return number_type(true_value)

            def get_value(self, )->number_type:
                """
                Returns:
                    number_type: La valeur stockée dans l'instance
                """
                return self.value
            
            def __add__(self, value : number_type | Self):
                val = CappedClass.cast_to_number(value)

                return CappedClass(value=self.value+val)
            
            def __sub__(self, value : number_type | Self):
                val = CappedClass.cast_to_number(value)

                return CappedClass(value=self.value-val)
            
            def __mul__(self, value : number_type | Self):
                val = CappedClass.cast_to_number(value)

                return CappedClass(value=self.value*val)
            
            def __truediv__(self, value : number_type | Self):
                val = CappedClass.cast_to_number(value)

                return CappedClass(value=self.value/val)
            
            def __lt__(self, value : number_type | Self):
                val = CappedClass.cast_to_number(value)
                return self.value < val

            def __le__(self, value : number_type | Self):
                val = CappedClass.cast_to_number(value)
                return self.value <= val

            def __eq__(self, value : number_type | Self):
                val = CappedClass.cast_to_number(value)
                return self.value == val

            def __ne__(self, value : number_type | Self):
                val = CappedClass.cast_to_number(value)
                return self.value != val

            def __gt__(self, value : number_type | Self):
                val = CappedClass.cast_to_number(value)
                return self.value > val

            def __ge__(self, value : number_type | Self):
                val = CappedClass.cast_to_number(value)
                return self.value >= val

        
        return CappedClass


# -------------------------------------------------------

CappedFloat_0_1 = CappedNumber.generate_type(
    number_type = float,
    min_val     = 0.0,
    max_val     = 1.0, 
)

PositiveFloat = CappedNumber.generate_type(
    number_type = float, 
    min_val     = 0.0,
)

FloatSuperiorTo_1 = CappedNumber.generate_type(
    number_type = float,
    min_val     = 1.0,
)