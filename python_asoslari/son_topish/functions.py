import random
import keyboard

def son_top_user(x=10):
  son = random.randint(1, x)
  print(f"1 dan {x} gacha oraliqda son o'yladim: Topa olasizmi?")
  urunishlar = 0
  while True:
    user_son = int(input(">> "))
    urunishlar += 1
    if user_son == son:
      print(f"Tabriklaymiz, siz topdingiz! O'ylangan son: {son}")
      break
    elif son > user_son:
      print(f"Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling:")
    else:
      print(f"Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling:")
  print(f"Tabriklaymiz, siz {urunishlar} urunishda topdingiz!")
  return urunishlar

def son_top_pc(x=10):
  print(f"1 dan {x} gacha oraliqda son o'ylang. Men topishga harakat qilaman!")
  print(f"Sonni o'ylagan bo'lsangiz istalgan tugmani bosing.")
  keyboard.read_key(suppress=True)

  past = 1
  yuqori = x
  urunishlar = 0

  while True:
    son = random.randint(past, yuqori)
    urunishlar += 1
    print(f"Siz o'ylagan son {son}\nAgar:\n(t) - to'g'ri bo'lsa\n(+) - o'ylagan son bu sondan katta\n(-) - o'ylagan son bu sondan kichik")

    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == 'down':
            javob = event.name
            break

    if javob == 't':
        print(f"Topdim! Siz {son} sonini o‘ylagansiz. Urunishlar soni: {urunishlar}")
        break
    elif javob == '+':
        past = son + 1
    elif javob == '-':
        yuqori = son - 1
    return urunishlar

def play(x=10):
    yana = True
    while yana:
        taxminlar_user = son_top_user(x)
        taxminlar_pc = son_top_pc(x)

        if taxminlar_user > taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
        elif taxminlar_user < taxminlar_pc:
            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))

play()