import unittest
from cars import Car

class CarTest(unittest.TestCase):
  def setUp(self):
    model = 'onix ltz'
    year = 2023
    self.price = 18000 # self bilan yaratilgan o'zgaruvchilar istalgan yerda foydalanish mumkin
    self.km = 1200
    self.avto1 = Car(model, year)
    self.avto2 = Car(model, year, price = self.price)

  # Xususiyatlarni tekshirish uchun test
  def test_create(self):
    self.assertIsNotNone(self.avto1.model) # xususiyat bor yoki yo'qligini tekshiradi
    self.assertIsNotNone(self.avto1.year)
    #
    self.assertIsNone(self.avto1.price)
    self.assertEqual(0, self.avto1.get_km()) # xususiyat qiymati teng yoki teng emasligini tekshiradi.
    #
    self.assertEqual(self.price, self.avto2.price)

  def test_set_price(self):
    new_price = 45000
    self.avto2.set_price(new_price)
    self.assertEqual(new_price, self.avto2.price)

  def test_add_km(self):
    #1 musbat qiymat bilan tekshirib ko'ramiz
    self.avto1.add_km(self.km)
    self.assertEqual(self.km, self.avto1.get_km())
    self.avto1.add_km(300)
    self.assertEqual(1500, self.avto1.get_km())
    #2 manfiy qiymat berib ko'ramiz
    new_km = -4000
    try:
      self.avto1.add_km(new_km)
    except ValueError as error:
      self.assertEqual(type(error), ValueError)

unittest.main()
