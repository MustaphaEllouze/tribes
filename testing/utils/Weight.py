"""Définition des tests de tribes.utils.Weight"""
# Bibliothèque standard de test
import unittest

# Classe à tester
from tribes.utils import Weight, PositiveFloat

class WeightTest(unittest.TestCase):
    """Définition des tests"""
    
    valeurs = (1.0, 2.0, 3.0, 1, 2, 3, -1, 0, 1000)
    shift_values = (0., 1., 2, -0.37, 0.37, -100, 0.98782)

    def test_00(self):
        """Création et attributs"""

        # On vérifie que les valeurs sont bien cohérentes
        for _value in WeightTest.valeurs : 
            self.assertEqual(
                Weight(value=_value).value,
                PositiveFloat(value=_value).value,
            )
    
    def test_01(self):
        """
        Vérifie que 'value' se comporte PositiveFloat.
        Vérifie que les fonctions add*** et remove*** sont bien implémentées.
        """

        # add_Weight
        for _value in WeightTest.valeurs :
            for _shift in WeightTest.shift_values :

                _from_Weight = Weight(value=_value)
                _from_Positive_Float = PositiveFloat(value=_value)

                _from_Weight.add_mass(mass_rate = _shift)
                _from_Positive_Float +=  _shift
                
                self.assertEqual(
                    _from_Weight.value,
                    _from_Positive_Float.value,
                )

        # add_time_in_months
        for _value in WeightTest.valeurs :
            for _shift in WeightTest.shift_values :

                _from_Weight = Weight(value=_value)
                _from_Positive_Float = PositiveFloat(value=_value)

                _from_Weight.add_mass_in_g(mass_rate = _shift)
                _from_Positive_Float += _shift/1000
                
                self.assertEqual(
                    _from_Weight.value,
                    _from_Positive_Float.value,
                )
                
        # remove_Weight
        for _value in WeightTest.valeurs :
            for _shift in WeightTest.shift_values :

                _from_Weight = Weight(value=_value)
                _from_Positive_Float = PositiveFloat(value=_value)

                _from_Weight.remove_mass(mass_rate = _shift)
                _from_Positive_Float -=  _shift
                
                self.assertEqual(
                    _from_Weight.value,
                    _from_Positive_Float.value,
                )

        # remove_Weight_in_cm
        for _value in WeightTest.valeurs :
            for _shift in WeightTest.shift_values :

                _from_Weight = Weight(value=_value)
                _from_Positive_Float = PositiveFloat(value=_value)

                _from_Weight.remove_mass_in_g(mass_rate=_shift)
                _from_Positive_Float -= _shift/1000
                
                self.assertEqual(
                    _from_Weight.value,
                    _from_Positive_Float.value,
                )

    