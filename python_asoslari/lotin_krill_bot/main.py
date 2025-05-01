"""
01.05.2025
MohirDev.Uz da FullStack Dasturlash
Lotin - Krill BOT
Dasturchi: Shahboz Shirinboyev
"""
from transliterate import to_cyrillic, to_latin

matn = input("Matn kiriting: ")
if matn.isascii():
  print(to_cyrillic(matn))
else:
  print(to_latin(matn))