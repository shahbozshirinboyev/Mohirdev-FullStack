import random

def son_top_user():
  son = random.randint(1, 10)
  print("[1, 2, ... 10] oraliqda son o'yladim: Topa olasizmi?")
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



def son_top_comp():
  