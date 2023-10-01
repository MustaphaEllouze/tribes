# Bibliothèque de tests unitaires
import unittest

# Bilbiothèque de tests pour les classes Vortex
from testing import (
    CustomTestRunner, CLASSES_CONTAINER,
)


# -----------------------------------------------------------------------------
# On lance tous les tests qui ont été définis
#   à partir d'un héritage de unittest.TestCase
# -----------------------------------------------------------------------------

# On définit la suite de tests à partir de ces classes
TEST_SUITE = unittest.TestSuite()
for testing_cls in CLASSES_CONTAINER:
    TEST_SUITE.addTests(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            testing_cls
        )
    )
    
if __name__ == '__main__':
    # LANCEMENT DES TESTS
    runner = CustomTestRunner()
    print("Start running tests")
    runner.run(TEST_SUITE)