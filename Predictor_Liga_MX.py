#Operaciones
partidos_total = 17
total_equipos = 18

#Maximo de puntos por temporada
max = partidos_total * 3

#Puntos obtenidos
def puntos_obtenidos(partidos_ganados, partidos_empatados):
    return (partidos_ganados * 3) + partidos_empatados
    
#Rendimiento final del equipo
def rendimiento(max, val_puntos):
    return (val_puntos / max) * 100

#Diferencia de goles
def diferencia_gol(goles_favor, goles_contra):
    return goles_favor - goles_contra

#Nivel alcanzado en liguilla 0=no clasifica, 1=play-in, 2=cuartos, 3=semis, 4=final
def liguilla(nivel_alcanzado):
    return nivel_alcanzado * 2

#Puntuacion final por equipo en base a todos los resultados
def puntuacion_final(redimiento, partidos_ganados, diferencia_gol, nivel_alcanzado):
    puntuacion = (redimiento * 0.4) + (partidos_ganados * 0.15) + (diferencia_gol * 0.25) + (nivel_alcanzado * 0.2)
    return puntuacion

#Suma de todas las puntaciones finales de los equipos
#suma_puntuacion= puntuacion_final de cada equipo sumada

#Probabilidad de ser campeon
def probabilidad(puntuacion, suma_puntuacion):
    probabilidad_equipo = (puntuacion / suma_puntuacion) * 100
    return probabilidad_equipo

#Prueba de calculos
nombre_equipo = input("nombre: ")
partidos_ganados = int(input("ganados:"))
partidos_empatados = int(input("empatados:"))
goles_favor = int(input("Favor:"))
goles_contra = int(input("Contra:"))
nivel_alcanzado = int(input("Nivel alcanzado en liguilla 0=no clasifica, 1=play-in, 2=cuartos, 3=semis, 4=final:"))

#Calcular para un equipo
val_puntos = puntos_obtenidos(partidos_ganados, partidos_empatados)
rendimiento_val = rendimiento(max, val_puntos)
val_dif_gol = diferencia_gol(goles_favor, goles_contra)
val_liguilla = liguilla(nivel_alcanzado)

val_final_puntos = puntuacion_final(rendimiento_val, partidos_ganados, val_dif_gol, val_liguilla)

#Se asume que hay promedio de 12 puntos para cada equipo, a futuro se usaran listas para tener los datos de todos los equipos
suma_puntuacion = val_final_puntos + (12 * (total_equipos - 1))

val_prob = probabilidad(val_final_puntos, suma_puntuacion)

print(f"\nResultados para {nombre_equipo}:")
print(f"Puntuación Final: {val_final_puntos:.2f}")
print(f"Probabilidad: {val_prob:.2f}%")