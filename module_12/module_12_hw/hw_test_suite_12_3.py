import unittest
import test_runner

TS = unittest.TestSuite()
TS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner.RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(TS)