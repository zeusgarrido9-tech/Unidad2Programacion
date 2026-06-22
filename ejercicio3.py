#CICLO FOR / Repite un bloque para cada elemento de una secuencia. Se usa cuando sabes de antemano cuantas
#veces repetir o cuando quieres recorrer los elementos de una lista, rango o cadena.

#Ejercicio: Variante de range() 
#range(fin) - Empiez en 0, termina antes del fin
print("range(5)")
for i in range(5):
    print (i, end=" ") #0 1 2 3 4
print()

#range(inicio, fin) - desde inicio hasta fin.
print("range(1,6):")
for i in range(1, 6):
    print(i, end= " ") #12345
print()

#range(inicio, fin, paso) - paso personalizado
print("Pare del 0 al 10:")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

#Cuenta regresiva con paso negativo
print("Cuenta regresiva:")
for i in range(5, 0, -1):
    print(i, end=" ")
print("¡Despegue")

#Tu turno: Escribe un for que imprima solo los múltiplos de 3 entre 3 y 30 usando range() 
#con los argumentos correctos. No uses if dentro del for para filtrar — usa el paso de range().

print("Rango de 3 a 30")
for i in range(3, 31, 3):
    print(i, end=" ")
print()

#Ejercicio - for recorriendo una lista: promedio y conteo.
#El for no solo funciona con numeros. Puede recorrer cualquier y acumular resultados.

calificaciones = [8.5, 9.0, 6.5, 10.0, 7.5, 5.0, 8.0]

print("Calificacion del grupo:")
for Calificacion in calificaciones:
    print(f" {Calificacion:.1f}")

total = 0
aprobados = 0

for calificacion in calificaciones:
    total = total + calificacion
    if calificacion >= 6.0:
        aprobados = aprobados + 1

    promedio = total / len(calificaciones)
    reprobados = len(calificaciones) - aprobados

print(f"\nPromedio del grupo: {promedio:.2f}")
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")

#Encuentra e imprime la calificacion mas alta y la mas baja. Necesitaras dos variables que guarden
#el maximo y el minimo mientras recorres la lista.

maximo = calificaciones[0]
minimo = calificaciones[0]

for calificacione in calificaciones:
    if calificacion >= maximo:
        maximo = calificacion

    if calificacion <= minimo:
        minimo = calificacion

print(f"Calificacion mas alta: {maximo}")
print(f"Calificacion mas baja: {minimo}")

#Ejercicio: for con enumarate(): indice y valor juntos.
#enumerate() te da la posicion y el valor en cada iteracion. Muy util para reportes numerados.

alumnos = ["Iran", "Povedano", "Gissel", "Susana", "Zeus", "Carlos", "Sulub"]
notas = [9.0, 7.5, 8.0, 9.5, 6.0, 10.0, 9.8]

#Encabezado de la tabla
print(f"{"No.":<5} {"Alumno":<12} {"Nota":<6} {"Estado":<10}")
print("-"*37)

for i, alumno in enumerate(alumnos):
    nota = nota[i]
    estado = "Aprobado" if nota >= 7.0 else "Reprobado"
    print(f"{i+1:<5} {alumno:<12} {nota:<6.1f} {estado:<10}") 

#Turno: Agrega al ejercicio un resumen al final del reporte:
#promedio del grupo y cantidad de aprobados, calculados dentro del mismo for que genera el reporte.
# Ejercicio: for con enumerate(): índice y valor juntos

alumnos = ["Iran", "Povedano", "Gissel", "Susana", "Zeus", "Carlos", "Sulub"]
notas = [9.0, 7.5, 8.0, 9.5, 6.0, 10.0, 9.8]

# Variables para el resumen
suma_notas = 0
aprobados = 0

# Encabezado de la tabla
print(f'{"No.":<5} {"Alumno":<12} {"Nota":<6} {"Estado":<10}')
print("-" * 37)

for i, alumno in enumerate(alumnos):
    nota = notas[i]
    estado = "Aprobado" if nota >= 7.0 else "Reprobado"

    print(f"{i + 1:<5} {alumno:<12} {nota:<6.1f} {estado:<10}")

    # Cálculos del resumen
    suma_notas += nota

    if nota >= 7.0:
        aprobados += 1

# Resumen final
promedio = suma_notas / len(notas)

print("-" * 37)
print(f"Promedio del grupo: {promedio:.2f}")
print(f"Cantidad de aprobados: {aprobados}")