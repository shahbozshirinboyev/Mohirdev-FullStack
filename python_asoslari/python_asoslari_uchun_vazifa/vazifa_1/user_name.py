"""
Username Generator
"""
import random

def user_name():
  while True:
    name = input("Ismingizni kiriting: ").lower()
    if name:
      username = ''.join(reversed(name))
      random_number = str(random.randint(0, 9))
      print(f"Siz uchun generatsiya qilingan username: {username+random_number}")
      break
    else:
      print("Iltimos, ism kiriting...")