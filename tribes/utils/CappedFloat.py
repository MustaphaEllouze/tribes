from dataclasses import dataclass
from typing import Self

@dataclass
class CappedFloat:
    value       : float 

    def __post_init__(self, ):
        self.value = max(min(self.value, 1), 0)

    @classmethod
    def cast_to_float(
        cls, 
        value : float | Self,
    ):
        if isinstance(value, CappedFloat) :
            true_value = value.value
        else:
            true_value = value

        return true_value
        

    def __add__(self, value : float | Self):
        val = CappedFloat.cast_to_float(value)

        return CappedFloat(value=self.value+val)
    
    def __sub__(self, value : float | Self):
        val = CappedFloat.cast_to_float(value)

        return CappedFloat(value=self.value-val)
    
    def __mul__(self, value : float|Self):
        val = CappedFloat.cast_to_float(value)

        return CappedFloat(value=self.value*val)
    
    def __truediv__(self, value : float|Self):
        val = CappedFloat.cast_to_float(value)

        return CappedFloat(value=self.value/val)
