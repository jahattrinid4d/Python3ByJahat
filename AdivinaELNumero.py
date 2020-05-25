import random

intentos = 0

print("¡Hola! ¿Como te llamas?")
nombre = input()
print()

numero = random.randint(1, 20)

print("Bueno " + nombre + ", estoy pensndo en un número entre 1 y 20.")

while intentos < 6 :
    print("Intenta adivinar.")
    estimacion = input()
    estimacion = int(estimacion)

    intentos = intentos + 1

    if estimacion < numero :
        print("Tu estimación es muy baja.")

    if estimacion > numero :
        print("Tu estimación es muy alta.")

    if estimacion == numero :
        break

if estimacion == numero :
    intentos = str(intentos)

    print("¡Buen trabajo " + nombre + "! Has adivinado mi número en " + intentos + " intentos.")

if estimacion != numero :
    numero = str(numero)

    print("Pues no. El número que estaba pensando era " + numero)