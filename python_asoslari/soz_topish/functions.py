import random
from uzwords_latin import words

def random_word(x=5):
  while True:
    tanlov = random.choice(words)
    while "-" in tanlov or " " in tanlov or "ʻ" in tanlov or "‘" in tanlov:
      tanlov = random.choice(words)
    if len(tanlov) == x:
      break
  return tanlov.upper()

def display(user_letters, word):
  display_letter = ""
  for letter in word:
    if letter in user_letters.upper():
      display_letter += letter
    else:
      display_letter += "-"
  return display_letter

def play():
  word = random_word()
  word_letters = set(word)
  user_letters = ""
  print(f"Men {len(word)} xonali son o'yladim. Topa olasizmi?")
  while len(word_letters) > 0:
    print(display(user_letters, word))
    if len(user_letters) > 0:
      print(f"Shu vaqtgacha kiritgan harflaringiz: {user_letters}")

    letter = input('Harf kiriting: ').upper()
    if letter in user_letters:
      print("Bu harfni avval kiritgansiz boshqa harf kiriting!")
      continue
    elif letter in word:
      word_letters.remove(letter)
      print(f"{letter} harfi to'g'ri")
    else:
      print("Bunday harf yo'q.")
    user_letters += letter
  print(f"Tabriklayman! {word} so'zini {len(user_letters)} ta urunishda topdingiz!")