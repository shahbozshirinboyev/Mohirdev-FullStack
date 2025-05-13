class Car:
  def __init__(self, model, year, km=0, price=None):
    self.model = model
    self.year = year
    self.km = km
    self.price = price

  def set_price(self, narx):
    self.price = narx

  def add_km(self, km):
    if km > 0:
      self.km += km
    else:
      raise ValueError("km manfiy bo'lishi mumkin emas.")
      # raise - xatolik keltirib chiqarishi haqida

  def get_info(self):
    info = f"{self.model.upper()} {self.year}-yil, "
    info += f"{self.km} km yo'l bosgan"
    if self.price:
      info += f", Narxi: {self.price}"
    return info

  def get_km(self):
    return self.km