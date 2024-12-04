from calendar import monthrange
from datetime import*
from random import *
from math import *

tana=date.today().strftime("%B %d, %Y")

print(f"Tere! Täna on {tana}")
d=tana.day
m=tana.month
y=tana.year

print(d)
print(m)
print(y)


detsP=monthrange(2024,12)[1] #31
novP=monthrange(2024,11)[1] #30
jaak=detsP+novP-d
print(f"Aasta lõppuni on {jaak}")
print(f"Aasta kuu on {jaak2}")

#Ülesanne 2
vastus1=3 + 8 / (4-2) * 4 
vastus2=3 + 8 / 4-2 * 4 
vastus3=(3 + 8) / (4-2) * 4 
vastus3=round((3 + 8 / (4-2) * 4)
print(vastus1,"\n"vastus2,"\n",vastus3,"\n", vastus4)

#Ülesanne 3
1 variant
try:
   R=float(input("Sisesta R: "))
   Sk=pi*R**2
   Lk=2*pi*R
   Skv=(2*R)**2
   Lkv=(2*R)*4
   print(f"Ringi pindala on {Sk}\nRingi ümbermõõt on {Lk}\nRuudu pindala on {Skv}\nRuudu ümbermõõt on {Lkv}")
except:
    print("On vaja number!")


#2 varint
R=random()*100 #0.0....1.0
print(f"R={R}")
Sk=pi*R**2
Lk=2*pi*R
Skv=(2*R)**2
Lkv=(2*R)*4
print(f"Ringi pindala on {Sk}\nRingi ümbermõõt on {Lk}\nRuudu pindala on {Skv}\nRuudu ümbermõõt on {Lkv}")

#Ülesanne 4
d=2.575 #mundi d sm+
maa=6378 #maa radius km
maa*=100000 #maa radius sm+maa=maa*100000
Lmaa=2*pi*maa
kogus=int(Lmaa/d)
print(f"On vaja {kogus}mundi.\nMeil on vaja {kogus*2}eur")

# Ülesanne 5
phrase1 = "Kill-Koll"
phrase2 = "Killadi-Koll"

output = f"{phrase1} {phrase1} {phrase2} {phrase1} {phrase1} {phrase2} {phrase1} {phrase1} {phrase1}\n{phrase1}"
print(output)

# Ülesanne 6
song = """
Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.
"""

print(song.upper())

# Ülesanne 7
a = float(input("Sisestage ristküliku esimese külje pikkus: "))
b = float(input("Sisestage ristküliku teise külje pikkus: "))

umbermoot = 2 * (a + b)
pindala = a * b

print(f"Ristküliku ümbermõõt on: {umbermoot}")
print(f"Ristküliku pindala on: {pindala}")

# Ülesanne 8
liters = float(input("Sisestage tangitud kütuse hulk liitrites: "))
kilometers = float(input("Sisestage läbitud kilomeetrid: "))

fuel_consumption = (liters / kilometers) * 100

print(f"Kütusekulu 100 km kohta on: {fuel_consumption:.2f} liitrit.")

# Ülesanne 9
speed_kmh = 29.9
time_minutes = float(input("Sisestage rulluisutamise aeg minutites: "))

distance_km = (speed_kmh / 60) * time_minutes

print(f"Rulluisutaja jõuab {distance_km:.2f} km kaugusele.")

# Ülesanne 10
minutes = int(input("Sisestage aeg minutites: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(f"Aeg on: {hours}:{remaining_minutes}")



