# Análisis exploratorio de datos de la English Premier League
## Introducción

La English Premier League, a la que llamaremos a lo largo de esta memoria como EPL, se ha convertido en los últimos tres años, hoy a año 2022, en la mejor liga del mundo, llegando a encabezar el ranking UEFA de las ligas europeas muy por encima de la anterior dominadora, LaLiga Santander (España). Este hecho ha supuesto un aumento masivo de la notoriedad de la EPL alrededor del mundo que sea visto traducido en los ingresos de la liga y por ende de sus participantes. No es desconocido para nadie que el dinero es importante para todo… bueno… para casi todo, y el deporte no es la excepción, desde tener mejores equipamientos, mejores preparadores físicos, mejores instalaciones, comodidades, más horas a la semana para dedicar a la actividad, entre otras cosas que tener dinero te permite para ser más y más competitivo. Las direcciones deportivas de los clubes de fútbol se preparan todo el año constantemente para dos momentos en particular, los cuales son: El mercado de verano y el mercado de invierno.
Estos mercados, mejores conocidos como ventanas de fichajes, son los momentos en los cuales por reglas del fútbol los equipos pueden inscribir jugadores en sus plantillas para disputar las competiciones oficiales y suele haber movimientos masivos de dinero, hablamos de decenas de millones de euros por equipo y siempre solemos observar que los equipos que mayores desembolsos suelen hacer son los equipos que suelen ganar o estar en altas posiciones de la clasificación, en base a estas observaciones se establecieron los objetivos de este análisis exploratorio de datos para poder determinar que tan difícil es competir en la mejor liga del mundo y si el dinero es realmente determinante a la hora de establecer quienes pueden competir a alto nivel a lo largo de la campaña y que equipos estarán por debajo en la tabla a final de temporada. A continuación, vamos a descubrir si el éxito de los grandes equipos del fútbol inglés o apodados recientemente como Big Six (Manchester City, Liverpool FC, Manchester United, Chelsea FC, Tottenham Hotspur y Arsenal FC) son realmente dominadores por las inversiones que hacen y eso les permite ser altamente competitivos o si existe algún otro factor.

## Objetivos

Como objetivo general de este proyecto esta el de satisfacer la siguiente pregunta: ¿Por qué siempre gana el Big Six?
	Para ello nos planteamos las siguientes afirmaciones:
1. La EPL es muy difícil en cuanto a competir se refiere
2. Se necesitan inversiones enormes para competir en la EPL
Para abordar la primera el primer paso fue en hacer por escalas lo que es competir para la realidad de cada equipo, ya que evidentemente cada equipo tiene sus objetivos y aspiraciones a final de temporada que para todos no es salir campeón. Las escalas son las siguientes:
1. Salir campeón
2. Clasificarse a competiciones europeas (Champions League y Europa League)
3. Mantener la categoría (No descender)

## Desarrollo

Para determinar los objetivos de cada equipo lo primero que se observó es el rendimiento de los equipos a lo largo de las temporadas estudiadas, que va desde la temporada 2010/2011 hasta la temporada 2020/2021. Se vio su promedio de puntos, promedio de goles a favor y de victorias y vemos que la mayoría de equipos que se logran mantener a lo largo de los años en la categoría son los que números más altos suelen tener en este apartado, es decir que uno de los requisitos para competir en esta liga es lograr afianzarse en esta. Luego se separó a los campeones y se observó que entre estos el gran dominador es el Manchester City con 5 títulos seguido por el Chelsea y el Manchester United con 2 títulos cada uno y por últimos el Liverpool y el Leicester City con 1 título para cada equipo.
Para los clasificados a la Champions League que son los primeros 4 clasificados de la tabla, excluyendo a los campeones ya mencionados que la mayoría se clasifica con regularidad, vemos que los equipos que suelen ser constantes son el Tottenham Hotspur y el Arsenal y para la Europa League los dos mencionados anteriormente suelen clasificarse también algún que otro año que no llegan a la Champions y también algún que otro ocasional como el Everton FC o Newcastle United.
Y por último para los salvados del descenso podemos encontrar equipos como el Queens Park Rangers, el Hull City o el AFC Bournemouth, aunque los más frecuentes en estas posiciones son el Aston Villa y el Sunderland AFC.
Para medir la dificultad de ser campeón de liga medimos la distancia que hay entre los campeones y el segundo y tercer clasificado por temporada y encontramos que dependiendo del año de hasta 18 puntos entre el primero y el segundo como es el caso de la temporada 2019/2020 entre el Liverpool y el Manchester City seguidos del Manchester United con 66 puntos, o casos como el de la temporada 2013/2014 que gana el Manchester City por 2 puntos de ventaja sobre el Liverpool que fue segundo y 4 sobre el Chelsea que fue tercero. Como media la distancia entre el primero y el segundo suele ser entre 7 y 9 puntos y entre el segundo y el tercero varía muchísimos más ya que hay campañas como la 2018/2019 en la que el Liverpool que fue segundo hizo 97 puntos y el tercero que fue el Chelsea hizo 66 o el 2010/2011 que segundo y tercero, Chelsea y Manchester City puntuaron igual. Estas altas y bajas diferencias entre segundo y tercero se reparten casi equitativamente entorno a las campañas estudiadas, pero siempre suele ser claro, o están muy cerca o muy distantes. Todo esto nos permite concluir que salir campeón de la EPL no solo depende mucho del año que puede que suban o bajen mucho las puntuaciones de campeonato entorno a la media (90 puntos de media de los campeones) si no también de los puntos conseguidos por sus competidores, concluyendo que, aunque el claro dominador a nivel de títulos en estos años es el Manchester City, ha sido difícil para este equipo mantener ese ritmo ya que hay un período en el que tuvieron un bajón que fue entre la campaña 20115/2016 que no estuvieron entre los 3 primeros clasificados y la 2016/2017 que fueron tercero con 71 puntos, muy por debajo de su media que es de 82 puntos.
Para la dificultad de clasificarse a competiciones europeas observamos la distancia entre el tercer y cuarto clasificado con el clasificado a Europa League que es el posterior y el sexto clasificado que es el inmediato que no clasifica para ninguna competición europea. Observamos que entre estos equipos a lo largo de las temporadas la mayoría de veces suelen estar muy cerca en la puntuación, es decir que no existe demasiada distancia entre sí, salvo en la campaña 2012/2013 que hay una gran brecha entre el quinto y el sexto clasificado que fue entre el Tottenham Hotspur con 71 puntos y el Everton con 58, o la campaña 2013/2014 entre el cuarto clasificado que fue el Arsenal con 79 puntos sobre el quinto clasificado que fue el Everton con 72 puntos. En base a esto podemos concluir que, aunque suelen repetir mucho el Chelsea, Arsenal, Tottenham y Manchester United si el equipo logra ser lo suficientemente consistente a lo largo de la temporada intentar clasificarse a competiciones europeas suele ser muy reñido y no se tiene muy claro quienes van a ir a que competición y quien se quedará fuera hasta los últimos partidos de la campaña.
Y para la dificultad de la liga en general comparamos la distancia existente entre los tres primeros clasificados y los 3 salvados del descenso en lo que nos encontramos brechas muy grandes siendo la más pequeña en la temporada 2019/2020 entre el tercero Manchester United y el decimoséptimo Burnley FC de 25 puntos que equivale a 8 victorias y un empate, por ende, la conclusión no fue demasiado difícil, es complicado competir en la EPL en general
En base a las observaciones anteriores la primera afirmación es tomada como correcta.
Respecto a la segunda, para poder abordarla, se tomó en cuenta el valor de las plantillas de los equipos y sus balances de fichajes y lo primero que se hizo fue averiguar si existía una correlación entre ambas cuya respuesta es que no muy significativa, por lo tanto, surge otra pregunta ¿Cómo se puede usar tan bien el dinero gastando poco y tener plantillas de alto valor? Y la respuesta fue sencilla, o revalorizas a tus jugadores en el mercado o fichas con inteligencia a jugadores que su valor de mercado del momento no corresponde a su valor real en el mismo, y observamos que los equipos que no tienen balances tan lejanos a la media (-31.71 millones de euros) y valores de plantillas superiores a la media (222.09 millones de euros) encontramos al Liverpool FC con balance y calor de plantilla de -33.51 millones de euros y un valor de plantilla de 571.89 millones de euros, al Tottenham Hotspur con un balance de millones -17.16 de euros y un valor de plantilla de 515.88 millones de euros y el Chelsea FC con un balance de -54.84 millones de euros y un valor de plantilla de 662.25 millones de euros como los equipos que mejor usan su dinero en cuanto a estos criterios.
En cuanto al equipo que más invierte, no debe ser misterio que es el amplio dominador de esta liga, el Manchester City el cual carga con un balance de fichajes promedio de -104.51 millones de euros y un valor de plantilla promedio de 701.95 millones de euros, muy por encima de los promedios de los antes mencionados, igual que sus resultados a largo plazo
También observamos el coste de los puntos, goles a favor y victorias de los equipos y observamos que entran los mismos equipos que en cuanto a los criterios de uso del dinero, Liverpool, Tottenham y Chelsea, aunque entra otro por encima del Chelsea en cuestión de coste de estas estadísticas el cual es el Arsenal que a pesar de no tener valor de plantilla promedio superior al del Chelsea se encuentra bien posicionado en cuanto a este apartado, lo que quiere decir que con los elementos que tiene llega a ser competitivo. Y el equipo que mayor coste tiene de estos es el Manchester City de nuevo con un gasto por punto, gol y victoria bastante muy por encima de los anteriores mencionados
Por lo cual para segunda afirmación se puede decir que también, como la primera, es correcta.
Para contrastar entre las dos afirmaciones si existe relación entre la dificultad de la liga y el gasto se tomó por temporada los valores de plantilla promedio, balances de fichajes promedio que se cotejaron con las puntuaciones hechas en esa misma temporada y se observó que las ligas que se han ido a puntuaciones más altas han sido precedidas por mayores inversiones de parte de los clubes, por ende es un punto más de dificultad para esos años en particular poder competir, lo que se puede tomar como una constante ya que repetidas veces se dio este suceso, más notoriamente en las temporadas 2017/2018 y 2018/2019 ambas ganadas por el Manchester City que hizo inversiones muy potentes aquellos años llegando a tener un balance de fichajes de -226.15 millones de euros en la 2017/2018 o que su plantilla alcanzase un valor de 1200 millones de euros en la campaña 2018/2019.
También descubrimos que en promedio los equipos que gastan más dinero por cada posición promedio en la tabla son los terceros, lo que quiere decir que tampoco gastar grandes cantidades de dinero te haga campeón de liga inmediatamente, existen otros factores no estudiados en este análisis como el rendimiento deportivo en general del equipo y otros factores externos.
Para finalizar, la conclusión es que en la mejor liga del mundo debes tener un equipo constate y la capacidad de que tu equipo se vaya afianzando en las posiciones e ir escalando en tus objetivos como club de fútbol y también hacer inversiones importantes, aunque no exageradas, para poder ser capaz de fichar mejores jugadores y mejorar la calidad de tu equipo, lo que te va a permitir estar en las posiciones superiores,  clasificarse las competiciones europeas y poder optar a ser un candidato al título
