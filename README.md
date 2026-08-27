# Proyecto-Fundamentos-de-programacion
## Predictor del siguiente campeón de la Liga Mx
### Contexto

La liga MX es la competición principal de fútbol profesional en México. Cada torneo participan varios equipos de todo el país buscando ser el siguiente campeón. Este torneo se lleva acabo dos veces por año siendo la apertura y clausura. Durante ambos para llegar a ser campeón los equipos necesitan obtener buenos resultados a lo largo de la campaña para poder clasificar a la liguilla. En la liguilla jugaran un torneo de eliminación directa con ida y vuelta contra los demás clasificados hasta que se consiga un campeón en la final.

Este proyecto consiste en desarrollar un algoritmo que pueda estimar cuáles son los equipos más probables a ganar el siguiente torneo de la Liga MX utilizando información sobre el torneo anterior. El programa tomará en cuenta múltiples factores, como puntos obtenidos, partidos ganas, empatados y perdidos, posición final , goles a favor y en contra y finalmente desempeño en la liguilla si es que llegaron hasta ahí. 

Me parece un proyecto muy interesante ya que permite utilizar datos disponibles al publico y totalmente reales para crear una predicción razonable de lo que puede pasar en el futuro de una de las competiciones más importantes corporativamente en el país. Además se me hace una idea muy interesante que el algoritmo no solo te de el campeón más probable si no varios y que tanta probabilidad hay de que sean campeones. Esto puede permitir obtener un mejor análisis de la liga con lo cual el usuario puede obtener mucha más información y hacer lo que guste con ella. 

Finalmente el programa funcionara al recibir los datos previamente especificados de cada equipo y calculara una puntuación para cada uno. En base a esto los ordenara de acuerdo a la puntuación mayor a menor y regresara el resultado de los 3 a 5 con mayor puntuación y la probabilidad de ser campeones. Aunque la predicción no garantiza el campeón real puede crear una estimación basada en datos de la temporada anterior para hacer su mejor análisis y predicción del ganador. Lo cual puede ser muy útil para futuros proyectos relacionados a la liga mx y su desempeño.

## Pseudoalgoritmo

1. Inicio
2. Solicitar para cada equipo:
   - Puntos obtenidos en la temporada anterior
   - Partidos ganados
   - Partidos empatados
   - Partidos perdidos
   - Goles a favor
   - Goles en contra
   - Etapa alcanzada en la liguilla
3. Calcular puntuación de cada equipo en base a datos anteriores
4. Guardar las puntuaciones de cada equipo
5. Ordenar equipos de mayor a menor puntuación
6. Calcular probabilidad de victoria
7. Mostrar al usuario los 3 a 5 equipos con las puntuaciones más altas y sus probabilidades
