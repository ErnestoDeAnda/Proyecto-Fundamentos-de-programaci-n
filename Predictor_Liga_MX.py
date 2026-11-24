import random

# Constantes a nivel de modulo
PARTIDOS_TOTAL = 17
TOTAL_EQUIPOS = 18
MAX_PUNTOS = PARTIDOS_TOTAL * 3


def puntos_obtenidos(partidos_ganados, partidos_empatados):
    """Calcula los puntos totales obtenidos por un equipo."""
    return (partidos_ganados * 3) + partidos_empatados


def rendimiento(max_puntos, val_puntos):
    """Calcula el porcentaje de rendimiento final del equipo."""
    return (val_puntos / max_puntos) * 100


def diferencia_gol(goles_favor, goles_contra):
    """Calcula la diferencia entre goles a favor y en contra."""
    return goles_favor - goles_contra


def puntuacion_final(rendimiento_val, partidos_ganados, dif_gol,
                     nivel_alcanzado):
    """Calcula la puntuacion final ponderada de un equipo."""
    puntuacion = ((rendimiento_val * 0.4)
                  + (partidos_ganados * 0.15)
                  + (dif_gol * 0.25)
                  + (nivel_alcanzado * 0.2))
    return puntuacion


def probabilidad(puntuacion, suma_puntuacion):
    """Calcula el porcentaje de probabilidad de ser campeon."""
    probabilidad_equipo = (puntuacion / suma_puntuacion) * 100
    return probabilidad_equipo


def prob_final(val_prob):
    """Devuelve una descripcion textual segun la probabilidad."""
    if val_prob >= 15:
        return "Probabilidad de victoria muy alta"
    elif val_prob >= 10:
        return "Probabilidad de victoria alta"
    elif val_prob >= 5:
        return "Probabilidad de victoria media"
    else:
        return "Probabilidad de victoria baja"


def liguilla(nivel_alcanzado):
    """Asigna puntos extra segun la fase alcanzada en liguilla."""
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


def nombre_limpio(nombre):
    """Elimina caracteres no alfanumericos del nombre del equipo."""
    limpio = ""
    for letra in nombre:
        if letra.isalnum() or letra == " ":
            limpio = limpio + letra
    return limpio.strip().title()


def es_numero(mensaje):
    """Valida que la entrada del usuario contenga digitos enteros."""
    while True:
        valor = input(mensaje)
        digitos = ""
        for letra in valor:
            if letra.isdigit():
                digitos = digitos + letra
        if digitos != "":
            return int(digitos)
        else:
            print("Ingresa un numero valido")


def cargar_datos(nombre_archivo, nombres, ganados, empatados, favor,
                 contra, alcanzado):
    """Lee los datos historicos de los equipos desde un archivo."""
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    archivo.readline()

    for linea in archivo:
        linea_limpia = linea.strip()
        if linea_limpia != "":
            datos = linea_limpia.split(",")
            nombres.append(nombre_limpio(datos[0]))
            ganados.append(int(datos[1]))
            empatados.append(int(datos[2]))
            favor.append(int(datos[3]))
            contra.append(int(datos[4]))
            alcanzado.append(int(datos[5]))
    archivo.close()


# Listas y matriz para almacenar datos de los equipos
nombres = []
ganados = []
empatados = []
favor = []
contra = []
alcanzado = []
puntuaciones = []
probabilidades = []
matriz_puntuaciones = []

cargar_datos("liga_mx.txt", nombres, ganados, empatados, favor,
             contra, alcanzado)

temporadas = es_numero("Numero de temporadas por calcular: ")

for year in range(temporadas):
    puntuaciones_year = []

    for i in range(len(nombres)):
        partidos_ganados = ganados[i] + random.randint(-2, 2)
        if partidos_ganados < 0:
            partidos_ganados = 0

        partidos_empatados = empatados[i] + random.randint(-2, 2)
        if partidos_empatados < 0:
            partidos_empatados = 0

        goles_favor = favor[i] + random.randint(-4, 4)
        goles_contra = contra[i] + random.randint(-4, 4)
        nivel_alcanzado = random.randint(0, 5)

        val_puntos = puntos_obtenidos(partidos_ganados, partidos_empatados)
        rendimiento_val = rendimiento(MAX_PUNTOS, val_puntos)
        val_dif_gol = diferencia_gol(goles_favor, goles_contra)
        val_liguilla = liguilla(nivel_alcanzado)
        val_final_puntos = puntuacion_final(rendimiento_val,
            partidos_ganados,val_dif_gol,val_liguilla)
        puntuaciones.append(val_final_puntos)
        puntuaciones_year.append(val_final_puntos)

    matriz_puntuaciones.append(puntuaciones_year)

# Calculo e impresion de resultados por temporada
for year in range(temporadas):
    print("\nResultado año " + str(year + 1))
    suma_puntuacion = sum(matriz_puntuaciones[year])

    for i in range(len(nombres)):
        val_prob = probabilidad(matriz_puntuaciones[year][i], suma_puntuacion)
        probabilidades.append(val_prob)

        print("\nResultados para " + nombres[i] + " año " + str(year + 1))
        print("Puntuacion Final: %.2f" % matriz_puntuaciones[year][i])
        print("Probabilidad: %.2f%%" % val_prob)
        print(prob_final(val_prob))