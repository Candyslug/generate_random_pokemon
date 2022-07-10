
from random import randint
import requests

amount = int(input("how many pokemon?\n>>> "))

def get_thing(i):
  s = "https://pokeapi.co/api/v2/pokemon/" + str(i) + "/"
  r = requests.get(s)

  code = r.status_code
  if code != 200:
    return (False, code)

  j = r.json()
  n = j['name']
  return (True, n)

def get_random_pokemon(c = 5):
  x1, x2 = 1, 898
  d = []
  for i in range(c):
    n = randint(x1, x2)
    if get_thing(n)[0] == False:
      print(n, get_thing(n)[1])
      break
    d.append(get_thing(n)[1])
    print(i+1, get_thing(n)[1])
  return d

print("retrieving the pocket men...\n")

p = get_random_pokemon(amount)
print()
print(p)
