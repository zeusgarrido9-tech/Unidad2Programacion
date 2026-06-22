#Condicional multiple y anidada 

#elif (else if) agrga ramas intermedias 

#Clasificador de calificaciones 

nota = float(input("Calificacion (0-10): "))

if nota < 0 or nota >10:
    print("Calificacion invalida")
elif nota >=9.0:
    letra = "A - Excelente"
elif nota >=8.0:
    letra = "B - Bien"
elif nota >=7.0:
    letra = "C - Suficiente"
elif nota >=6.0:
    letra = "D - Aprobado minimo"
else:
    letra ="F - Reprobado"

if 0 <= nota <= 10:
    print(f"Nota: {nota:.1f} -> {letra}")

#Tu turno: Agrega  un mensaje que diga cuántos puntos le faltan para subir de letra. Por ejemplo,
#si obtuvo 7.2 (letra C), necesita 0.8 puntos para llegar a la B.

#Ejercicio
calificacion = float(input("Ingresa tu calificación: "))


if calificacion >= 9:
    print("Tu letra es A")
    print("Ya tienes la calificación máxima.")
elif calificacion >= 8:
    print("Tu letra es B")
    faltan = 9 - calificacion
    print("Te faltan", round(faltan, 1), "puntos para llegar a la A.")
elif calificacion >= 7:
    print("Tu letra es C")
    faltan = 8 - calificacion
    print("Te faltan", round(faltan, 1), "puntos para llegar a la B.")
elif calificacion >= 6:
    print("Tu letra es D")
    faltan = 7 - calificacion
    print("Te faltan", round(faltan, 1), "puntos para llegar a la C.")
else:
    print("Tu letra es F")
    faltan = 6 - calificacion
    print("Te faltan", round(faltan, 1), "puntos para llegar a la D.") 

#Tu turno: Reescribe el Ejercicio  usando una sola condición con and en lugar del if anidado. 
#Luego compara las dos versiones: 
# ¿cuál da mensajes de error más específicos y por qué?

calificacion = float(input("Ingresa tu calificación: "))

if calificacion >= 9 and calificacion <= 10:
    print("Tu letra es A")
    print("Ya tienes la calificación máxima.")

elif calificacion >= 8 and calificacion < 9:
    print("Tu letra es B")
    faltan = 9 - calificacion
    print(f"Te faltan {round(faltan, 1)} puntos para llegar a la A.")

elif calificacion >= 7 and calificacion < 8:
    print("Tu letra es C")
    faltan = 8 - calificacion
    print(f"Te faltan {round(faltan, 1)} puntos para llegar a la B.")

elif calificacion >= 6 and calificacion < 7:
    print("Tu letra es D")
    faltan = 7 - calificacion
    print(f"Te faltan {round(faltan, 1)} puntos para llegar a la C.")

elif calificacion >= 0 and calificacion < 6:
    print("Tu letra es F")
    faltan = 6 - calificacion
    print(f"Te faltan {round(faltan, 1)} puntos para llegar a la D.")

else:
    print("Error: la calificación debe estar entre 0 y 10.")

#La versión con and puede dar mensajes de error más específicos porque permite validar 
#claramente si la calificación está fuera del rango permitido (por ejemplo, menor que 0 o mayor que 10).