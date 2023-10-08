"""Définition des tests de tribes.utils.Height"""
# Bibliothèque standard de test
import unittest

# Classe à tester
from tribes.utils import Height, PositiveFloat

class HeightTest(unittest.TestCase):
    """Définition des tests"""
    
    valeurs = (1.0, 2.0, 3.0, 1, 2, 3, -1, 0, 1000, 0.37, -0.22, 0.999)
    shift_values = (0., 1., 2, -0.37, 0.37, -100, 0.98782)

    def test_00(self):
        """Création et attributs"""

        # On vérifie que les valeurs sont bien cohérentes
        for _value in HeightTest.valeurs : 
            self.assertEqual(
                Height(value=_value).value,
                PositiveFloat(value=_value).value,
            )
    
    def test_01(self):
        """
        Vérifie que 'value' se comporte PositiveFloat.
        Vérifie que les fonctions add*** et remove*** sont bien implémentées.
        """

        # add_height
        for _value in HeightTest.valeurs :
            for _shift in HeightTest.shift_values :

                _from_Height = Height(value=_value)
                _from_Positive_Float = PositiveFloat(value=_value)

                _from_Height.add_height(height_rate = _shift)
                _from_Positive_Float +=  _shift
                
                self.assertEqual(
                    _from_Height.value,
                    _from_Positive_Float.value,
                )

        # add_time_in_months
        for _value in HeightTest.valeurs :
            for _shift in HeightTest.shift_values :

                _from_Height = Height(value=_value)
                _from_Positive_Float = PositiveFloat(value=_value)

                _from_Height.add_height_in_cm(height_rate = _shift)
                _from_Positive_Float += _shift/100
                
                self.assertEqual(
                    _from_Height.value,
                    _from_Positive_Float.value,
                )
                
        # remove_height
        for _value in HeightTest.valeurs :
            for _shift in HeightTest.shift_values :

                _from_Height = Height(value=_value)
                _from_Positive_Float = PositiveFloat(value=_value)

                _from_Height.remove_height(height_rate = _shift)
                _from_Positive_Float -=  _shift
                
                self.assertEqual(
                    _from_Height.value,
                    _from_Positive_Float.value,
                )

        # remove_height_in_cm
        for _value in HeightTest.valeurs :
            for _shift in HeightTest.shift_values :

                _from_Height = Height(value=_value)
                _from_Positive_Float = PositiveFloat(value=_value)

                _from_Height.remove_height_in_cm(height_rate=_shift)
                _from_Positive_Float -= _shift/100
                
                self.assertEqual(
                    _from_Height.value,
                    _from_Positive_Float.value,
                )
    
    def test_02(self):
        """Vérifie que la conversion en str est fonctionnelle"""

        for _valeur in HeightTest.valeurs:
            str(Height(value=_valeur))
        
        self.assert_(True)

    