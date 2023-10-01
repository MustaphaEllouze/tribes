import unittest

class CustomTestRunner(unittest.TextTestRunner):
    """Classe permettant de surcharger le runner de test."""
    def run(self, test):
        for test_case in test:
            # Print the name of the test method
            print(
                f"Running test: {test_case.__class__.__name__}."\
                f"{test_case.__dict__['_testMethodName']}"
            )

        # Call the parent's run() method to execute the tests
        super().run(test)