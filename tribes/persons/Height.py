from dataclasses import dataclass

@dataclass
class Height:
    """In meters"""
    value : float

    
    def __str__(self, ):
        if self.value < 1 :
            return f'{int(self.value*100)} cm'
        else:
            return f'{int(self.value)}m {int(self.value*100)%100}'

    def grow(self, grow_rate : float = 0.0):
        self.value += grow_rate
    
    def grow_in_cm(self, grow_rate : float = 0.0):
        self.value += grow_rate/100
    