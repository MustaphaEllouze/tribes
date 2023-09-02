import random

from tribes.utils import CappedFloat


def gauss01(sigma:float=0.25)->float:
    """Renvoie un nombre entre 0 et 1 selon une distribution 
    gaussienne."""
    random_value = random.gauss(mu=0.5, sigma=sigma)
    return CappedFloat(random_value).value