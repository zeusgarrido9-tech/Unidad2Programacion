# CICLOS ANIDADOS + BREAK Y CONTINUE - 

# Ciclos anidados — un ciclo dentro de otro

#Un ciclo anidado es un ciclo dentro del bloque de otro ciclo. Por cada iteración del ciclo externo, el ciclo interno 
# se ejecuta completamente. Total de ejecuciones = iteraciones_externo × iteraciones_interno.
#Cuándo usarlos: tablas, matrices, patrones, comparación de dos listas. Si necesitas más de 2 niveles de anidación, 
#busca antes una solución más simple.

#Ejercicio -- Ciclos anidados: tabla de multiplicar

#El ciclo externo es la tabla y el interno son los multiplicadores del 1 al 10.

# ── Ejercicio: Tabla de multiplicar ───────────────────────
N = int(input("¿Hasta qué tabla quieres? "))

for tabla in range(1, N + 1):
    print(f"--- Tabla del {tabla} ---")
    for mult in range(1, 11):
        resultado = tabla * mult
        print(f"  {tabla} x {mult:2} = {resultado:3}")
    print()    # línea en blanco entre tablas

#Tu turno: Modifica el Ejercicio para imprimir solo los resultados impares de cada tabla. 
# Necesitarás un if dentro del for interno que verifique si el resultado es impar usando el operador %.




# break y continue — control del flujo del ciclo

# Estas dos palabras reservadas modifican el comportamiento normal de un ciclo:

#break: termina el ciclo inmediatamente, aunque la condición todavía sea True. El programa continúa después del ciclo.
#continue: salta el resto del bloque actual y pasa a la siguiente iteración. El ciclo NO termina.
#Úsalos con criterio. Abusar de ellos hace el código difícil de seguir. Son válidos cuando simplifican la lógica, no cuando la complican.

# Ejercicio:  break y continue: diferencia en acción
# Observa cómo cada uno altera el flujo del ciclo de forma completamente diferente.

# ── Ejercicio: break y continue ───────────────────────────
notas = [9.0, 8.5, 7.0, 4.5, 9.5, 6.0]

# break — sale del ciclo al encontrar el primer reprobado
print("Buscando primer reprobado...")
for i, nota in enumerate(notas):
    if nota < 6.0:
        print(f"  Primer reprobado en posición {i}: {nota}")
        break    # ya encontramos lo que buscábamos
print()

# continue — salta los reprobados, solo procesa aprobados
print("Solo aprobados:")
for nota in notas:
    if nota < 6.0:
        continue    # salta esta iteración, el ciclo continúa
    print(f"  Aprobado: {nota:.1f}")


#Tu turno: Reescribe el bloque de "Solo aprobados" del Ejercicio sin usar continue, usando un if normal. 
# ¿El resultado es el mismo? ¿Cuál versión es más fácil de leer?

# break — sale del ciclo al encontrar el primer reprobado
print("Buscando primer reprobado...")
for i, nota in enumerate(notas):
    if nota < 6.0:
        print(f"  Primer reprobado en posición {i}: {nota}")
        break

print()

# if normal — solo procesa aprobados
print("Solo aprobados:")
for nota in notas:
    if nota >= 6.0:
        print(f"  Aprobado: {nota:.1f}")

#El resultado es el mismo 

#¿Cuál versión es más fácil de leer?
#En este caso, la versión con un if normal suele ser más fácil de entender
#porque expresa directamente la condición que debe cumplirse.