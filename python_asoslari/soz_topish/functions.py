import random
from uzwords_latin import words

def soz_top():
  print("Men 5 xonali so'z o'yladim. Topishga harakat qiling:")
  tanlov = random.choice(words)
  print(tanlov)

soz_top()