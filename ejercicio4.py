#While - Repite un bloque mientras una condicion sea true. Se usa cuando no sabes de antemano cuantas veces
#necesitas repetir - el numero de repeticiones depende de lo que ocurra durante la ejecucion.

#REGLA CRITICA: algo dentro del while debe cambiar en cada iteracion para que la condicion eventualmente sea
#false. sin eso, el ciclo nunca termina.

#Ejercicio . while basico: contador y acumulador

N = int(input("Suma del 1 hasta: "))
i = 1 #Contador - empieza en 1
suma = 0 #Acumulador - empieza en 0

while i <= N:
    suma = suma + i
    i = i + 1

print(f"Suma de 1 a {N}: {suma}")


#Verificacionb matematica: N * (N+1)/2
formula = N * (N +1) /2
print(f"Verificacion con formula: {formula}")

#Tu turno: Reescribe el ejercicio usando for en lugar de while. 
#¿Cuál versión es más natural para este problema? Explica por qué con tus palabras.

nota = float(input("Calificacion (0-10):"))

while nota < 0 or nota > 10:
    print("Calificacion invalida. Debe ser emntre 0 y 10.")
    nota = float(input("Calificacion (0-10)"))

print(f"Calificacion registrada: {nota:.1f}")
print()

#While True + break
while True:
    edad = int(input("Tu edad(1-80):"))
    if 1 <= edad <=80:
        break
    print("Edad invalida, intenta de nuevo.")

print(f"Edad registrada: {edad}")

#Tu turno: Crea un programa que pida al usuario adivinar un número secreto
#(define tú el número con una constante). Con while, 
#sigue pidiendo hasta que lo adivine e imprime cuántos intentos necesitó.
# Constante con el número secreto

NUMERO_SECRETO = 7

# Variables de control
intentos = 0
respuesta = 0

print("¡Bienvenido al juego de adivinar el número!")
print("Debes descubrir el número secreto.")

# Repetir hasta que el usuario adivine
while respuesta != NUMERO_SECRETO:
    respuesta = int(input("Ingresa un número: "))
    intentos += 1

    if respuesta < NUMERO_SECRETO:
        print("El número secreto es mayor.")
    elif respuesta > NUMERO_SECRETO:
        print("El número secreto es menor.")

# Mensaje final
print(f"¡Felicidades! Adivinaste el número secreto en {intentos} intento(s).")