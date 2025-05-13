import unittest
from circle import getArea, getPerimeter

class CircleTest(unittest.TestCase):
  def test_area(self):
    self.assertAlmostEqual(getArea(5), 78.53975)
    # yana boshqa qiymatlarni ham tekshirish mumkin

  def test_perimeter(self):
    self.assertAlmostEqual(getPerimeter(10), 62.8318)
    # yana boshqa qiymatlarni ham tekshirish mumkin

    
unittest.main()