#Design the Python function to_roman to convert a positive integer (less than 4000) to a string containing a roman numeral and the Python function from_roman to convert a roman numeral (less than 5000) to a positive integer.

import unittest

def to_roman(n):
  """converts a positive integer (less than 4000) to a string containing a roman numeral"""

  result = ''

  while n > 0:
    if n >= 1000:
      n -= 1000
      result += 'M' 
    elif n >= 900:
      n -= 900
      result += 'CM'
    elif n >= 500:
      n -= 500
      result += 'D'
    elif n >= 400:
      n -= 400
      result += 'CD'
    elif n >= 100:
      n -= 100
      result += 'C'
    elif n >= 90:
      n -= 90
      result += 'XC'
    elif n >= 50:
      n -= 50
      result += 'L'
    elif n >= 40:
      n -= 40
      result += 'XL'
    elif n >= 10:
      n -= 10
      result += 'X'
    elif n >= 9:
      n -= 9
      result += 'IX'
    elif n >= 5:
      n -= 5
      result += 'V'
    elif n >= 4:
      n -= 4
      result += 'IV'
    elif n >= 1:
      n -= 1
      result += 'I'         

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