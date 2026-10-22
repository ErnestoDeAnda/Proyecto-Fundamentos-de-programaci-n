#Operaciones
PARTIDOS_TOTAL = 17
TOTAL_EQUIPOS = 18

#Maximo de puntos por temporada
MAX_PUNTOS = PARTIDOS_TOTAL * 3

def puntos_obtenidos(partidos_ganados, partidos_empatados):
    #Puntos obtenidos
    
    return (partidos_ganados * 3) + partidos_empatados
    
def rendimiento(MAX_PUNTOS, val_puntos):
    #Rendimiento final del equipo

    return (val_puntos / MAX_PUNTOS) * 100


def diferencia_gol(goles_favor, goles_contra):
    #Diferencia de goles

    return goles_favor - goles_contra


def puntuacion_final(rendimiento, partidos_ganados, diferencia_gol, nivel_alcanzado):
    #Puntuacion final por equipo en base a todos los resultados

    puntuacion = (rendimiento * 0.4) + (partidos_ganados * 0.15) + (diferencia_gol * 0.25) + (nivel_alcanzado * 0.2)
    return puntuacion


#Suma de todas las puntaciones finales de los equipos
#suma_puntuacion= puntuacion_final de cada equipo sumada


def probabilidad(puntuacion, suma_puntuacion):
    #Probabilidad de ser campeon

    probabilidad_equipo = (puntuacion / suma_puntuacion) * 100
    return probabilidad_equipo

def prob_final(val_prob):
    if val_prob >= 15:
        return "Probabilidad de victoria muy alta"
    elif val_prob >= 10:
        return "Probabilidad de victoria alta"
    elif val_prob >= 5:
        return "Probabilidad de victoria media"
    else:
        return "Probabilidad de victoria baja"

def liguilla(nivel_alcanzado):
    if nivel_alcanzado == 1:
        return 2
    elif nivel_alcanzado == 2:
        return 4
    elif nivel_alcanzado == 3:
        return 6
    elif nivel_alcanzado == 4:
        return 8
    elif nivel_alcanzado == 5:
        return 10
    else:
        return 0

correr = "y"

#Datos a guardar
nombres = []
ganados = []
empatados = []
favor = []
contra = []
alcanzado = []
puntuaciones = []
probabilidades = []

matriz_puntuaciones = []

temporadas = int(input("Numero de temporadas por calcular: "))

while correr == "y":
    
    nombre_equipo = input("nombre: ")
    nombres.append(nombre_equipo)
    correr = input("¿Quieres agregar otro equipo? (y/n): ")
  
for year in range(temporadas):
    puntuaciones_year = []
    
    for x in range(len(nombres)):
        print("Informacion del", nombres[x], "año", year+1)
        
        #Prueba de calculos input
        partidos_ganados = int(input("ganados: "))
        partidos_empatados = int(input("empatados: "))
        goles_favor = int(input("Favor: "))
        goles_contra = int(input("Contra: "))
        nivel_alcanzado = int(input("Nivel alcanzado en liguilla 0=no clasifica, " 
        "1=play-in , 2=cuartos, 3=semis, 4=final , 5= Campeón: "))

        #Incluir en listas
        
        ganados.append(partidos_ganados)
        empatados.append(partidos_empatados)
        favor.append(goles_favor)
        contra.append(goles_contra)
        alcanzado.append(nivel_alcanzado)
            
        val_puntos = puntos_obtenidos(partidos_ganados, partidos_empatados)
        rendimiento_val = rendimiento(MAX_PUNTOS, val_puntos)
        val_dif_gol = diferencia_gol(goles_favor, goles_contra)
        val_liguilla = liguilla(nivel_alcanzado)
        val_final_puntos = puntuacion_final(rendimiento_val, partidos_ganados, val_dif_gol, val_liguilla)
        puntuaciones.append(val_final_puntos)
        
        puntuaciones_year.append(val_final_puntos)
    
    matriz_puntuaciones.append(puntuaciones_year)

# Suma real de las puntuaciones de los equipos registrados 
for year in range(temporadas):
    print("Resultado año", year+1)
    suma_puntuacion = sum(matriz_puntuaciones[year])

    #Calculo probabilidad
    for x in range(len(nombres)):
        val_prob = probabilidad(matriz_puntuaciones[year][x], suma_puntuacion)
        probabilidades.append(val_prob)

        print(f"\nResultados para {nombres[x]}:", "año", year+1)
        print(f"Puntuación Final: {matriz_puntuaciones[year][x]:.2f}")
        print(f"Probabilidad: {val_prob:.2f}%")
        print(prob_final(val_prob))