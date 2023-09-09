from tribes.utils import (
    PositiveFloat,
)

class Age(PositiveFloat):
    """in years"""

    def __str__(self, ):
        if self.value < 1 :
            return f'{int(self.value*100)} cm'
        else:
            return f'{int(self.value)}m {int(self.value*100)%100}'

    def grow(self, age : float = 0.0):
        self.value += age
    
    def grow_in_months(self, age : float = 0.0):
        self.value += age/12
    
    def grow_in_days(self, age : float = 0.0):
        self.value += age/365