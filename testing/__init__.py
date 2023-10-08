# ------------------------------ IMPORTS --------------------------------------
from testing.CustomTestRunner import CustomTestRunner

# ------------------------------ CLASSES DE TEST ------------------------------
from testing.utils.Age import AgeTest
from testing.utils.Height import HeightTest
from testing.utils.Weight import WeightTest

# ------------------------------ ASSEMBLAGE -----------------------------------
CLASSES_CONTAINER = (
    AgeTest,
    HeightTest,
    WeightTest,
)