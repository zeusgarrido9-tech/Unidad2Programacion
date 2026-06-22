# SISTEMA DE REGISTRO DE CALIFICACIONES
# Registra las calificaciones de 15 estudiantes, valida
# los datos, calcula estadísticas y genera un reporte.

#CONSTANTES
CALIFICACION_MINIMA_APROBATORIA = 6.0
TOTAL_ESTUDIANTES = 15

CALIFICACION_MINIMA = 0.0
CALIFICACION_MAXIMA = 10.0

LETRA_A_MINIMA = 9.0
LETRA_B_MINIMA = 8.0
LETRA_C_MINIMA = 7.0
LETRA_D_MINIMA = 6.0

PORCENTAJE_TOTAL = 100

#LISTAS

nombres = []
calificaciones = []

#CAPTURA Y VALIDACIÓN DE DATOS 

for numero_estudiante in range(TOTAL_ESTUDIANTES):

    print(f"\n--- Estudiante {numero_estudiante + 1} de {TOTAL_ESTUDIANTES} ---")

    nombre = input("Ingresa el nombre del estudiante: ").strip()

    while nombre == "":
        print("Error: el nombre no puede estar vacío.")
        nombre = input("Ingresa el nombre del estudiante: ").strip()

    while True:
        try:
            calificacion = float(input("Ingresa la calificación (0.0 - 10.0): "))

            if CALIFICACION_MINIMA <= calificacion <= CALIFICACION_MAXIMA:
                break
            else:
                print(
                    f"Error: la calificación debe estar entre "
                    f"{CALIFICACION_MINIMA} y {CALIFICACION_MAXIMA}."
                )

        except ValueError:
            print("Error: debes ingresar un número decimal válido.")

    nombres.append(nombre)
    calificaciones.append(calificacion)

#CÁLCULO DE RESULTADOS

suma_calificaciones = 0
total_aprobados = 0
total_reprobados = 0

# Inicializar estudiante con mayor y menor calificación
mejor_nombre = nombres[0]
mejor_calificacion = calificaciones[0]

peor_nombre = nombres[0]
peor_calificacion = calificaciones[0]

for indice in range(TOTAL_ESTUDIANTES):

    calificacion = calificaciones[indice]

    suma_calificaciones += calificacion

    if calificacion >= CALIFICACION_MINIMA_APROBATORIA:
        total_aprobados += 1
    else:
        total_reprobados += 1

    # Buscar la calificación más alta sin usar max()
    if calificacion > mejor_calificacion:
        mejor_calificacion = calificacion
        mejor_nombre = nombres[indice]

    # Buscar la calificación más baja sin usar min()
    if calificacion < peor_calificacion:
        peor_calificacion = calificacion
        peor_nombre = nombres[indice]

promedio_grupo = suma_calificaciones / TOTAL_ESTUDIANTES

porcentaje_aprobados = (
    total_aprobados * PORCENTAJE_TOTAL
) / TOTAL_ESTUDIANTES

#REPORTE FINAL

print("\n" + "=" * 72)
print("              REPORTE FINAL DE CALIFICACIONES")
print("=" * 72)

print(
    f"{'No.':<5}"
    f"{'Nombre':<25}"
    f"{'Calificación':<15}"
    f"{'Estado':<15}"
    f"{'Letra':<10}"
)

print("-" * 72)

for indice, nombre in enumerate(nombres):

    calificacion = calificaciones[indice]

    # Determinar estado
    if calificacion >= CALIFICACION_MINIMA_APROBATORIA:
        estado = "Aprobado"
    else:
        estado = "Reprobado"

    # Determinar letra
    if calificacion >= LETRA_A_MINIMA:
        letra = "A"
    elif calificacion >= LETRA_B_MINIMA:
        letra = "B"
    elif calificacion >= LETRA_C_MINIMA:
        letra = "C"
    elif calificacion >= LETRA_D_MINIMA:
        letra = "D"
    else:
        letra = "F"

    print(
        f"{indice + 1:<5}"
        f"{nombre:<25}"
        f"{calificacion:<15.1f}"
        f"{estado:<15}"
        f"{letra:<10}"
    )

print("=" * 72)

print(f"Promedio del grupo: {promedio_grupo:.1f}")
print(f"Total de aprobados: {total_aprobados}")
print(f"Total de reprobados: {total_reprobados}")

print("\n--- Estadísticas adicionales ---")

print(
    f"Estudiante con la calificación más alta: "
    f"{mejor_nombre} ({mejor_calificacion:.1f})"
)

print(
    f"Estudiante con la calificación más baja: "
    f"{peor_nombre} ({peor_calificacion:.1f})"
)

print(f"Porcentaje de aprobación: {porcentaje_aprobados:.1f}%")