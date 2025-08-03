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
    print(f"{self.first_name.title()}ning life_path_number'i bu {total} ekan.")
    return total

  def get_info_by_number(self, number: int):
      if 1 <= number <= 9:
          filename = 'hayot_yoli.txt'
          with open(filename, encoding='utf-8') as file:
              text = file.read()
          parts = text.split('#')
          for part in parts:
              if part.startswith(f"{number} -"):
                  return part[len(f"{number} -"):].strip()
          return f"#{number} bo‘lim topilmadi."
      else:
          return "Iltimos 1 dan 9 gacha bo‘lgan raqam kiriting."