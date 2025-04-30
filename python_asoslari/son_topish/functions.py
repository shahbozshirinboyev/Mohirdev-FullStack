import random

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
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar

def play(x=10):
    yana = True
    while yana:
        taxminlar_user = son_top_user(x)
        taxminlar_pc = son_top_pc(x)

        if taxminlar_user>taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
        elif taxminlar_user<taxminlar_pc:
            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))