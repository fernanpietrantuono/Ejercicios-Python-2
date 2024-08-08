import random

adivinanza = 0
num_secreto = random.randint(1, 10)
while adivinanza != num_secreto:
    adivinanza = int(input("Adiviná un número: "))
    if adivinanza == num_secreto:
        print(f'Correcto! El número correcto es {num_secreto}')
    else:
        print("Incorrecto! Intentalo otra vez")
