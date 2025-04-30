import random
from uzwords_latin import words

def random_soz(x=5):
  print("Men 5 xonali so'z o'yladim. Topishga harakat qiling:\n-----")
  while True:
    tanlov = random.choice(words)
    if len(tanlov) == x:
      break
  return tanlov

tanlov = random_soz()
print(tanlov)