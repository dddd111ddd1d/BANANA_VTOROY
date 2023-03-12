import requests
from colorama import Fore

class Person:
  def __init__ (self, nat, gender):
    r = requests.get("https://randomuser.me/api/?nat=" + nat + '&gender=' + gender)
    res = r.json()
    self.name = res["results"][0]["name"]["first"]
    self.surename = res["results"][0]["name"]["last"]
    self.age = res["results"][0]["dob"]["age"]
    self.phone = res["results"][0]["phone"]
    self.email = res["results"][0]["email"]
    self.isMale = res["results"][0]["gender"] == "male"


  def print_person(self):
    if self.isMale:
      print(Fore.CYAN)
    else:
      print(Fore.MAGENTA)
    print(self.name)
    print(self.surename)
    print(self.age)
    print(self.phone)
    print(self.email)
    print(self.isMale)

a = input("Ckilki tobi treba pracuvnukiv dla kompanii?")
a = int(a)

m = input('Tilku choloviku?')

gen = "male"

if m == "-":
  gen = "female"
  

pracivnuk = []

#  генеруємо колектив
while a != 0:
  p = Person('ua', gen)
  pracivnuk.append(p)
  a -= 1

# виписуємо дані працівників
for p in pracivnuk:
  p.print_person()