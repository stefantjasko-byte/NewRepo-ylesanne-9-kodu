#Töö1.1
# Lisatud try-except (õpiku punkt 1.14): programm ei jookse kokku,
# kui kasutaja sisestab arvu asemel midagi muud.

# Abifunktsioonid: küsivad sisendit seni, kuni see on õiget tüüpi
def küsi_täisarv(tekst):
    while True:
        try:
            return int(input(tekst))
        except ValueError:
            print("Palun sisesta täisarv!")

def küsi_arv(tekst):
    while True:
        try:
            return float(input(tekst))
        except ValueError:
            print("Palun sisesta arv!")


# Ülesanne 1
print("Tere maailm!")
nimi = input("Sisesta oma nimi: ")
print(f"Tere, maailm! Tervitan sind {nimi}!")
vanus = küsi_täisarv("Sisesta oma vanus: ")
print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")


# Ülesanne 2
vanus = 18  # int
eesnimi = "Jaak"  # str
pikkus = 16.5  # float
kas_käib_koolis = True  # bool (teine võimalus: False)
print(f"Muutuja: {vanus}, tüüp: {type(vanus)}")
print(f"Muutuja: {eesnimi}, tüüp: {type(eesnimi)}")
print(f"Muutuja: {pikkus}, tüüp: {type(pikkus)}")
print(f"Muutuja: {kas_käib_koolis}, tüüp: {type(kas_käib_koolis)}")


# Ülesanne 3
from random import *  # randint
kommide_arv = randint(1, 100)
print(f"Laual on {kommide_arv} kommi.")
kommid = küsi_täisarv("Mitu kommi soovid laualt ära võtta? ")
kommide_arv -= kommid
print(f"Laual on nüüd {kommide_arv} kommi.")


# Ülesanne 4
from math import *  # pi, sqrt()
ümbermõõt = küsi_arv("Sisesta puu ümbermõõt: ")
läbimõõt = ümbermõõt / pi
print(f"Puu läbimõõt on {läbimõõt}.")


# Ülesanne 5
N = küsi_arv("Sisesta ristküliku 1. külje pikkus: ")
M = küsi_arv("Sisesta ristküliku 2. külje pikkus: ")
d = sqrt(N**2 + M**2)
print(f"Ristküliku diagonaal on {d}.")


# Ülesanne 6
while True:
    try:
        aeg = float(input("Mitu tundi kulus sõiduks? "))
        teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
        kiirus = teepikkus / aeg  # kiirus = tee / aeg
        break
    except ValueError:
        print("Palun sisesta arv!")
    except ZeroDivisionError:
        print("Aeg ei saa olla 0!")
print("Sinu kiirus oli " + str(kiirus) + " km/h")


# Ülesanne 7
arv1 = küsi_täisarv("Sisesta 1. täisarv: ")
arv2 = küsi_täisarv("Sisesta 2. täisarv: ")
arv3 = küsi_täisarv("Sisesta 3. täisarv: ")
arv4 = küsi_täisarv("Sisesta 4. täisarv: ")
arv5 = küsi_täisarv("Sisesta 5. täisarv: ")
summa = arv1 + arv2 + arv3 + arv4 + arv5
keskmine = summa / 5
print(f"Arvude summa on {summa}.")
print(f"Arvude keskmine on {keskmine}.")

# Summa jagamine kasutaja sisestatud arvuga (täisosa ja jääk)
while True:
    try:
        jagaja = int(input("Sisesta arv, millega summa jagada: "))
        täisosa = summa // jagaja
        jääk = summa % jagaja
        break
    except ValueError:
        print("Palun sisesta täisarv!")
    except ZeroDivisionError:
        print("Nulliga jagada ei saa!")
print(f"Täisosa on {täisosa}.")
print(f"Jääk on {jääk}.")


# Ülesanne 9
a = küsi_täisarv("Sisesta 1. täisarv: ")
b = küsi_täisarv("Sisesta 2. täisarv: ")
c = küsi_täisarv("Sisesta 3. täisarv: ")
P = a + b + c
print(f"Ümbermõõt P on {P}.")
