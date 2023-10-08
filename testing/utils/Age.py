"""Définition des tests pour tribes.utils.Age"""
# Bibliothèque standard de test
import unittest

# Classe à tester
from tribes.utils import Age, Time

class AgeTest(unittest.TestCase):
    """Définition des tests"""
    
    valeurs = (1.0, 2.0, 3.0, 1, 2, 3, -1, 0, 1000)
    shift_values = (0., 1., 2, -0.37, 0.37, -100, 0.98782)

    def test_00(self):
        """Création et attributs"""

        # On vérifie que les valeurs sont bien cohérentes
        for _value in AgeTest.valeurs : 
            self.assertEqual(
                Age(value=_value).value,
                Time(value=_value).value,
            )
    
    def test_01(self):
        """
        Vérifie que 'value' se comporte Time.
        Vérifie que les fonctions add_time*** sont bien implémentés.
        """

        # add_time
        for _value in AgeTest.valeurs :
            for _shift in AgeTest.shift_values :

                _from_Age = Age(value=_value)
                _from_Time = Time(value=_value)

                _from_Age.add_time(time = _shift)
                _from_Time.add_time(time = _shift)
                
                self.assertEqual(
                    _from_Age.value,
                    _from_Time.value,
                )

        # add_time_in_months
        for _value in AgeTest.valeurs :
            for _shift in AgeTest.shift_values :

                _from_Age = Age(value=_value)
                _from_Time = Time(value=_value)

                _from_Age.add_time_in_months(time = _shift)
                _from_Time.add_time_in_months(time = _shift)
                
                self.assertEqual(
                    _from_Age.value,
                    _from_Time.value,
                )

        # add_time_in_days
        for _value in AgeTest.valeurs :
            for _shift in AgeTest.shift_values :

                _from_Age = Age(value=_value)
                _from_Time = Time(value=_value)

                _from_Age.add_time_in_days(time = _shift)
                _from_Time.add_time_in_days(time = _shift)
                
                self.assertEqual(
                    _from_Age.value,
                    _from_Time.value,
                )
    