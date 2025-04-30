import random
import keyboard


def son_top_user(x=10):
  son = random.randint(1, x)
  print(f"1 dan {x} gacha oraliqda son o'yladim: Topa olasizmi?")
  sanoq = 0
  while True:
    user_son = int(input(">> "))
    if user_son == son:
      print(f"Tabriklaymiz, siz topdingiz! O'ylangan son: {son}")
      sanoq += 1
      break
    elif son > user_son:
      print(f"Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling:")
      sanoq += 1
    else:
      print(f"Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling:")
      sanoq += 1
  print(f"Tabriklaymiz, siz {sanoq} urunishda topdingiz!")
  return sanoq

def son_top_pc(x=10):
  print(f"1 dan {x} gacha son o'ylang. Men topishga harakat qilaman!")
  input("Son o'ylagan bo'lsangiz istalgan tugmani bosing!")
  print("Ajoyib, son o'yladingiz... men topishga harakat qilaman:")
  past = 1
  yuqori = x
  taxminlar = 0
  while True:
    son = random.randint(past, yuqori)
    print(f"Siz {son} o'yladingiz:\n(T) - to'g'ri\n(+) - o'ylagan soningiz bundan kattaroq\n(-) - o'ylagan soningiz bundan kichikroq")
    if keyboard.read_event().name == 't':
      print(f"To'g'ri topdingiz...")
    elif keyboard.read_event().name == '+':
      past = son + 1
    elif keyboard.read_event().name == '-':
      yuqori = son - 1