from dataclasses import dataclass

from tribes.utils import (
    PositiveFloat,
)

@dataclass
class Height:
    """In meters"""
    height : float

    def __post_init__(
            self,
    ):
        self.value_container = PositiveFloat(value=self.height)

    @property
    def value(self):
        return self.value_container.value
    
    @value.setter
    def value(self, a_value : float):
        self.value_container.value = a_value
    
    def __str__(self, ):
        if self.value < 1 :
            return f'{int(self.value*100)} cm'
        else:
            return f'{int(self.value)}m {int(self.value*100)%100}'

    def grow(self, grow_rate : float = 0.0):
        self.value += grow_rate
    
    def grow_in_cm(self, grow_rate : float = 0.0):
        self.value += grow_rate/100