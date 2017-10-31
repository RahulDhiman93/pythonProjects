import unittest

def roman(num):
    ie = 'I'
    vo = 'V'
    xe = 'X'
    ce = 'C'
    fi = 'M'

    one = ie
    two = ie+ie
    three = ie+ie+ie
    four = ie+vo
    five = vo
    six = vo+ie
    seven = vo+ie+ie
    eight = vo+ie+ie+ie
    nine = ie+xe
    
    if num == 1:
        return one
    elif num == 2:
        return two
    elif num == 3:
        return three
    elif num == 4:
        return four
    elif num == 5:
        return five
    elif num == 6:
        return six
    elif num == 7:
        return seven
    elif num == 8:
        return eight
    elif num == 9:
        return nine
    elif num == 10:
        return xe
    elif num > 10:
        number = ''
        
        count = int(num/100)
        left = num - 100*count
        while count > 0:
            number += ce
            count -=1
            
        count2 = int(left/50)
        left2 = left - 50*count2
        while count2 > 0:
            number += fi
            count2 -=1

        count3 = int(left2/10)
        left3 = left2 - 10*count3
        while count3 > 0:
            number += xe
            count3 -=1

        if left3 == 1:
            number += one
        elif left3 == 2:
            number += two
        elif left3 == 3:
            number += three
        elif left3 == 4:
            number += four
        elif left3 == 5:
            number += five
        elif left3 == 6:
            number += six
        elif left3 == 7:
            number += seven
        elif left3 == 8:
            number += eight
        elif left3 == 9:
            number += nine

 


        return number
       

class roman_testcases(unittest.TestCase):
    def test1(self):
        self.assertEqual(roman(1),'I')
    def test2(self):
        self.assertEqual(roman(2),'II')
    def test3(self):
        self.assertEqual(roman(3),'III')
    def test4(self):
        self.assertEqual(roman(5),'V')
    def test5(self):
        self.assertEqual(roman(10),'X')
    def test6(self):
        self.assertEqual(roman(23),'XXIII')

unittest.main()
