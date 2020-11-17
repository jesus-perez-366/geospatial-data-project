# geospatial-data-project

## Expliación
Determinar la ubicacion optima de una empresa de juego en funcion de diversos criterios.

## Librerias Usadas
Pandas,
Folium,
pymongo y
Json

## Infomación Extraida:
API Resquests ('https://api.foursquare.com/v2/venues/explore')

## Desarrollo
Se extrajo la geolocalización de diversas empresas de Juegos ubicadas en USA de la Base de Datos de "Companies" de Mongodb. Se realizó inicialmente un filtro con respecto a cuales empresas tenian en un radio de 3km una o más empresas de software que tuviesen una recaudación monetaria mayor al 1.000.000$

## Los filtros posteriores fueron:
Mayor cantidad de escuelas en un radio de 3Km
Mayor cantidad de terminales de aeropuertos en un radio de 3 km
Mayor cantidad de Restauran Veganos en un radio de 2 km
Mayor cantidad de canchas de basket en un radio de 3 km
Mayor cantidad de cafeterias en un radio de 1 km
Mayor cantidad de C. Veterinarias en un radio de 3 km


## Estado Inicial

<div style="text-align:right"><figure src=output/Mapa_empresas.jpg width="400">



## Estado Final

<div style="text-align:right"><img src=output/Mapa_empresas2.html width="400">




