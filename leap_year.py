import unittest

def leap(year):
    if year % 4 == 0:
        return 1
    else:
        return 0
    
class leap_testcase(unittest.TestCase):
    def test_year(self):
        self.assertEqual(leap(2016),1)

    def test_year_second(self):
        self.assertFalse(leap(2017))

unittest.main()
