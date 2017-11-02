import unittest

def adding(num1,num2):
    return num1+num2

class adding_testcase(unittest.TestCase):
    def test_oneplusone(self):
        self.assertEqual(adding(1,1),2)


unittest.main()
