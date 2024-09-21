import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_challenge(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')

    def test_run(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')

    def test_walk(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')

class TournamentTest(unittest.TestCase):
    is_frozen = True

    def test_first_tournament(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')

    def test_second_tournament(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')

    def test_third_tournament(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')

test_suite = unittest.TestSuite()
test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)
