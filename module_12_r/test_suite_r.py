import unittest
import test_new_calk, test_calk

calkST = unittest.TestSuite()
calkST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_calk.CalkTest))
calkST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_new_calk.NewCalkTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(calkST)