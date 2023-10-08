"""Définition des tests de tribes.utils.Time"""
# Bibliothèque standard de test
import unittest

# Classe à tester
from tribes.utils import (
    Time, 
    FormatTime,
    PositiveFloat,
)

from tribes.utils.Time import (
    YEARS_TO_DAYS, 
    YEARS_TO_MONTHS,
)

class TimeTest(unittest.TestCase):
    """Définition des tests"""
    
    valeurs = (1.0, 2.0, 3.0, 1, 2, 3, -1, 0, 1000, 0.37, -0.22, 0.999)
    shift_values = (0., 1., 2, -0.37, 0.37, -100, 0.98782)

    def test_00(self):
        """
        Vérification de la création
        Vérification de la property value
        """

        # On vérifie que les valeurs sont bien cohérentes
        for _value in TimeTest.valeurs : 
            self.assertEqual(
                Time(value=_value).value,
                PositiveFloat(value=_value).value,
            )

    def test_01(self):
        """
        Vérification de la définition de l'attribut ymd
        """
        for _value in TimeTest.valeurs :
            _the_time = Time(value=_value)
            self.assertTupleEqual(
                _the_time.ymd,
                _the_time.get_time_in_ymd(),
            )
    
    def test_02(self):
        """
        Vérifie que 'value' se comporte en tant que PositiveFloat.
        Vérifie que les fonctions add*** et remove*** sont bien implémentées.
        """

        # add_time
        for _value in TimeTest.valeurs :
            for _shift in TimeTest.shift_values :

                _from_Time = Time(value=_value)
                _from_Positive_Float = PositiveFloat(value=_value)

                _from_Time.add_time(time = _shift)
                _from_Positive_Float +=  _shift
                
                self.assertEqual(
                    _from_Time.value,
                    _from_Positive_Float.value,
                )

        # add_time_in_days
        for _value in TimeTest.valeurs :
            for _shift in TimeTest.shift_values :

                _from_Time = Time(value=_value)
                _from_Positive_Float = PositiveFloat(value=_value)

                _from_Time.add_time_in_days(time = _shift)
                _from_Positive_Float += _shift/YEARS_TO_DAYS
                
                self.assertEqual(
                    _from_Time.value,
                    _from_Positive_Float.value,
                )
                
        # add_time_in_months
        for _value in TimeTest.valeurs :
            for _shift in TimeTest.shift_values :

                _from_Time = Time(value=_value)
                _from_Positive_Float = PositiveFloat(value=_value)

                _from_Time.add_time_in_months(time = _shift)
                _from_Positive_Float +=  _shift/YEARS_TO_MONTHS
                
                self.assertEqual(
                    _from_Time.value,
                    _from_Positive_Float.value,
                )

        # substract_time
        for _value in TimeTest.valeurs :
            for _shift in TimeTest.shift_values :

                _from_Time = Time(value=_value)
                _from_Positive_Float = PositiveFloat(value=_value)

                _from_Time.substract_time(time = _shift)
                _from_Positive_Float -=  _shift
                
                self.assertEqual(
                    _from_Time.value,
                    _from_Positive_Float.value,
                )

        # substract_time_in_days
        for _value in TimeTest.valeurs :
            for _shift in TimeTest.shift_values :

                _from_Time = Time(value=_value)
                _from_Positive_Float = PositiveFloat(value=_value)

                _from_Time.substract_time_in_days(time = _shift)
                _from_Positive_Float -= _shift/YEARS_TO_DAYS
                
                self.assertEqual(
                    _from_Time.value,
                    _from_Positive_Float.value,
                )
                
        # substract_time_in_months
        for _value in TimeTest.valeurs :
            for _shift in TimeTest.shift_values :

                _from_Time = Time(value=_value)
                _from_Positive_Float = PositiveFloat(value=_value)

                _from_Time.substract_time_in_months(time = _shift)
                _from_Positive_Float -=  _shift/YEARS_TO_MONTHS
                
                self.assertEqual(
                    _from_Time.value,
                    _from_Positive_Float.value,
                )

    
    def test_03(self):
        """Vérifie que les conversions en autres unités sont bien faites
        """

        for _valeur in TimeTest.valeurs:
            
            _the_value = Time(value=_valeur)
            
            # Âge entier
            total_time = _the_value.value

            # Années = partie entière
            years = int(total_time)        

            # Mois = Partie entière de ce qui reste (* facteur de conversion)
            months = int((total_time-years)*YEARS_TO_MONTHS)

            # Jours = même principes
            days = int((total_time-years-months/YEARS_TO_MONTHS)*YEARS_TO_DAYS)

            # Vérifications 
            self.assertTupleEqual(
                (years, months, days),
                _the_value.get_time_in_ymd()
            )
            self.assertTupleEqual(
                (years*YEARS_TO_MONTHS+months, days),
                _the_value.get_time_in_months_days()
            )
            self.assertEqual(
                int(total_time*YEARS_TO_DAYS),
                _the_value.get_time_in_days()
            )
    
    def test_04(self):
        """Vérifie que les conversions en str ne plantent pas"""

        for _valeur in TimeTest.valeurs : 
            str(Time(value=_valeur))
            for _format in FormatTime : 
                Time(value=_valeur).to_str(format=_format.value)

        self.assert_(True)
    
    def test_5(self):
        """Vérifie qu'une demande d'un format inconnu fait bien planter
        la conversion en str"""

        _a_time = Time(value=TimeTest.valeurs[0])
        try : 
            # Typiquement un format qui n'est pas supposé exister.
            _a_time.to_str(format='BABAYAGA, the hallouba is strong')
        except ValueError : 
            self.assert_(True)
        except : 
            self.assert_(False)


    