#Programa que agrega peliculas a una lista
#Ponerle nombre a mi lista
peliculas=[]
#Preguntar cuantas pelis
cantidadPelis=int(input("¿Cuántas peliculas vas a agregar?"))
#valor inicial para el while
i=0
#Mientras i sea menor a cantidad ejecuta
while i<=cantidadPelis:
    #Preguntar pelis
    peli=input("Ingresa peli: ")
    #Agrega peliculas a la lista
    peliculas.append(peli)
    #Muetra la lista
    print(peliculas)
    i=i+1
#Buscar una pelicula en la lista
#Preguntar la peli que busca
peliBuscar=input("¿Qué peli buscas?")
if peliBuscar in peliculas:
    print("Sí está")
else:
    print("No está pero dejame la agrego")
    peliculas.append(peliBuscar)
    print(peliculas)
#EXTRA
#Solicita una pelicula para borrar
#Borra la pelicula
#Muestra la pelicula
peliBorrar=input("¿Cuál pelicula quieres borrar?")
peliculas.remove(peliBorrar)
print(peliculas)