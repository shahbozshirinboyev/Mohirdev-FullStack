class Person:
  def __init__(self, first_name: str, last_name: str, age: int, email:str, birth_day: int, birth_month: int, birth_year: int):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.email = email
    self.birth_day = (birth_day, birth_month, birth_year)

  def get_info(self):
    info = f"Shaxs: {self.first_name.title()} {self.last_name.title()}\n"
    info += f"Yosh: {self.age}\n"
    info += f"Email: {self.email}\n"
    info += f"Tug'ulgan sana: {self.birth_day[0]}.{self.birth_day[1]}.{self.birth_day[2]}"
    return info

  def get_life_path_number(self):
    all_digits = [int(d) for number in self.birth_day for d in str(number)]
    total = sum(all_digits)
    while total >= 10:
      total = sum(int(d) for d in str(total))
    return f"{self.first_name.title()}ning life path numberi bu {total} ekan."

  def get_info_by_number(self, number: int):
    if 1 <= number <= 9:
      filename = 'hayot_yoli.txt'
      with open(filename) as file:
       lines = file.readlines()
      return lines
    else:
      return f"Iltimos raqam kiriting: 1, 2, 3, ... 9."


  




person0 = Person('umid', "mamatov", 23, 'mamatovu@gmail.com', 1, 8, 1997)
print(person0.get_info())
print(person0.get_life_path_number())
print(person0.get_info_by_number(29))