import  math # * from не нужен


print("Ruudu karakteristikud") 
try: #добавила try для проверки типа данных

    a=float(input("Sisesta ruudu külje pikkus => ")) #нужно добавить двойные кавычки (") вместо (')
# а так же все вводимые данные преобразую в float
    S = a**2
    print("Ruudu pindala:", S) #Где нужно вводить ответ добавила (:)
    P = 4 * a
    print("Ruudu ümbermõõt:", P)  #Вместо таких (' ') скобок ставим (")
    di = a * math.sqrt(2) #sgrt вместо sgt
    print("Ruudu diagonaal:", round(di,2))
except ValueError: # Добавила для обработки ошибок, связанных с неправильным вводом данных
 #(например ввод букв, вместо числ) вместо ошибки, программа выдаст сообщение Palun sisestage arvuline väärtus!
    print("Palun sisestage arvuline väärtus!")

    print("\nRistküliku karakteristikud:") # Добавила \n для перехода на новую строку

try: #добавила try для проверки типа данных как и выше
    b= float (input("Sisesta ristküliku 1. külje pikkus => ")) #все вводимые данные преобразую в float
    c = float(input("Sisesta ristküliku 2. külje pikkus => "))
    S=b*c
    print("Ristküliku pindala:", S) # Добавила (")
    P=2 * (b + c) # Добавила знак умножения чтоюы формула работала корректно*
    print("Ristküliku ümbermõõt:", P)
    di=math.sqrt(b**2+c**2) # Исправила на ** чтобы возвести в степень.
    print("Ristküliku diagonaal:", round(di,2)) #Добавила 2 чтобы округилить до двух знаков после запятой
except ValueError: # Сделала тоже самое что и выше
    print("Palun sisestage arvuline väärtus!")

    print("\nRingi karakteristikud") # Так же добавила \n для перехода на новую строку
  
try:# тоже добавила try для проверки типа данных
    r = float(input("Sisesta ringi raadiusi pikkus => ")) #Поменяла ковычки и добавила float
    d = 2 * r #Добавила * для корректной формулы
    print("Ringi läbimõõt:", d) #Добавила (,)
    S = math.pi * r**2 # Исправила формулу math.pi вместо pi() чтобы избежать ошибки в коде а так же возмела (r) в квадрат
    print("Ringi pindala:", round(S,2)) # Добавила 2 чтобы округилить до двух знаков после запятой
    C = 2 * math.pi * r # Исправила формулу, добавила значение числа пи и знак умножения после 2
    print("Ringjoone pikkus:", round(C, 2)) # Так же добавила 2 чтобы округилить до двух знаков после запятой и добавила вторую скобку в конце 

except ValueError:
    print("Palun sisestage arvuline väärtus!")# Сделала тоже самое что и выше




