import random
import keyboard

def son_top_user():
  son = random.randint(1, 10)
  print(son)
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
  print(f"1 dan 10 gacha son o'ylang. Men topishga harakat qilaman.")
  print(f"Son o'ylagan bo'lsangiz istalgan tugmani bosing:")
  while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        print(f"Tugma bosildi: {event.name}")
    if event.name == 'esc':
        print("Dastur to‘xtatildi.")
        break


son_top_comp()