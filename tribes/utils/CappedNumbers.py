from dataclasses import dataclass
from typing import Self

class CappedNumber :

    def __init__(
            self,
    ):
        raise ValueError("Cannot instantiate.")
    
    @classmethod
    def generate_type(
            self, 
            number_type : float | int,
            min_val     : float | int = None,
            max_val     : float | int = None,
    ):
        
        
        class CappedClass : 
            min_value   : float | int  = min_val
            max_value   : float | int  = max_val

            def __init__(
                    self, 
                    value : float | int,
            ):
                self.value = value

                if CappedClass.min_value is not None : 
                    self.value = max(self.value, CappedClass.min_value)
                if CappedClass.max_value is not None : 
                    self.value = min(self.value, CappedClass.max_value)
                
                self.value      = number_type(self.value)
            
            def __str__(self) -> str:
                return f"{self.value}"
            
            @classmethod
            def cast_to_number(
                cls,
                value : number_type | Self,
            ):
                if isinstance(value, CappedClass):
                    true_value = value.value
                elif isinstance(value, (float, int)):
                    true_value = value
                else:
                    raise NotImplementedError()
                
                return number_type(true_value)

            def get_value(self, )->number_type:
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