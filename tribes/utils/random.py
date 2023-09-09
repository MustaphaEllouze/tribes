import random

from tribes.utils import CappedFloat_0_1


def gauss01(sigma:float=0.25)->CappedFloat_0_1:
    """Renvoie un nombre entre 0 et 1 selon une distribution 
    gaussienne."""
    random_value = random.gauss(mu=0.5, sigma=sigma)
    return CappedFloat_0_1(random_value).value