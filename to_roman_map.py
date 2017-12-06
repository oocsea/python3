#Design the Python function to_roman to convert a positive integer (less than 4000) to a string containing a roman numeral and the Python function from_roman to convert a roman numeral (less than 5000) to a positive integer.

import unittest

roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))  

def to_roman(n):
  """converts a positive integer (less than 4000) to a string containing a roman numeral"""

  result = ''

  for numeral, integer in roman_numeral_map: 
    while n >= integer:
        n -= integer       
        result += numeral

  return result


# print(to_roman(14))

class TestRomanFunction(unittest.TestCase):

  def test_roman1(self):
    self.assertEqual(to_roman(1), 'I')

  def test_roman1(self):
    self.assertEqual(to_roman(2), 'II')

  def test_roman2(self):
    self.assertEqual(to_roman(100), 'C')

  def test_roman3(self):
    self.assertEqual(to_roman(149), 'CXLIX')

if __name__ == '__main__':
  unittest.main()