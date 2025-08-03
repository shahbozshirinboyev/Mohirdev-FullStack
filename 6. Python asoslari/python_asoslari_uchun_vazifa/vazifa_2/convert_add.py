"""
  String to Integers
"""

def convert_add():
  print("Ro'yxat shakillantirayapmiz: ")
  royxat = []
  while True:
    son = input("Son kiriting: (Son kiritishni to'xatish uchun 'q' ni kiritng.) ")
    if son == 'q':
      break
    else:
      if son.isdigit():
        royxat.append(son)
        print(royxat)
      else:
        print('Iltimos, son kiriting...')

  for idx in range(len(royxat)):
    royxat[idx] = int(royxat[idx])

  print(f"Ro'yxat: {royxat}")
  print(f"Ro'yxat sonlari yig'indisi: {sum(royxat)}")
