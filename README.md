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
1. Mayor cantidad de escuelas en un radio de 3Km

2. Mayor cantidad de terminales de aeropuertos en un radio de 3 km

3. Mayor cantidad de Restauran Veganos en un radio de 2 km

4. Mayor cantidad de canchas de basket en un radio de 3 km

5. Mayor cantidad de cafeterias en un radio de 1 km

6. Mayor cantidad de C. Veterinarias en un radio de 3 km


## Estado Inicial

<div style="text-align:left"><img src=output/1.jpg width="400">




## Estado Final

<div style="text-align:left"><img src=output/2.jpg width="400">




