from random import* # #*-kõik funksioonid, randint as rd сокращение
from math import* #pi


#Ülesanne 1
print ("Hello World") #lower()-aaa,upper()-AAA,capitalize()-Aaa
name=input("Mis on sinu nimi? ").capitalize()
print("Hello World!Tervitan sind", name)
print("Hello World!Tervitan sind"+ name)
age=int(input("Kui vana sa oled?" ))
print("Hello World! Tervitan sind "+name+"Sa oled ",age,"aastat vana")
print(f"Hello World! Tervitan sind {name} Sa oled {age} aastat vana")



#Ülesanne 2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print(type(vanus)),print(type(eesnimi)),print(type(pikkus)),print(type(kas_käib_koolis))


#Ülesanne 3
kokku=randint(1,1000)
print(f"Kokku on {kokku} kommi")
kommi=int(input("Mittu kommi sa tahad?"))
kokku=kokku-kommi
print(f"Jääk on {kokku} kommi")


#Ülesanne 4
print("Läbimõõdu leidmine ")
#l
#-ümbermõõt
l=float(input("ümbermõõt: "))
d=l/pi
print(f"Läbimõõdu suurus on {round(d,2)}")


#Ülesanne 5
import math
N = float(input("Sisestage maatüki laius (m): "))
M = float(input("Sisestage maatüki pikkus (m): "))
diagonaal = math.sqrt(N**2 + M**2)
print(f"Maatüki diagonaal on {diagonaal:.2f} meetrit.")


#Ülesanne 6
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg 
print(f"Sinu kiirus oli {kiirus:.2f} km/h")


#Ülesanne 7
print("Sisestage 5 täisarvu:")
num1 = int(input("Esimene arv: "))
num2 = int(input("Teine arv: "))
num3 = int(input("Kolmas arv: "))
num4 = int(input("Neljas arv: "))
num5 = int(input("Viies arv: "))
keskmine = (num1 + num2 + num3 + num4 + num5) / 5
print(f"Aritmeetiline keskmine on: {keskmine}")


#Ülesanne 8
print ("    @..@ ")
print ("   (----)  ")
print ("  ( \__/ ) ")
print("  ^^    ^^   ")


#Ülesanne 9
a = int(input("Sisestage esimese külje pikkus (cm): "))
b = int(input("Sisestage teise külje pikkus (cm): "))
c = int(input("Sisestage kolmanda külje pikkus (cm): "))
P = a + b + c
print(f"Kolmnurga ümbermõõt on {P} cm.")


#Ülesanne 10
P = int(input("Mitu sõpra söövad pitsa? "))
pizza_price = 12.90
tip = pizza_price * 0.10
total_price = pizza_price + tip
per_person = total_price / P
print(f"Igaüks peab maksma: {per_person:.2f} €")