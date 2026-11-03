nombre="Arianell"
frase="El mundo es bonito"
print(nombre)
print(frase)
#Mostrar el nombre en mayus
print(nombre.upper())
print(frase.upper())
#Mostrar en minus
print(frase.lower())
#obtener un carácter en una posición
letra=frase[4]
print(letra)
frase2="El-cielo-es-azul"
print(frase2.split("-"))
nombre_completo="Emily Arianell Valenzuela Murillo"
print(nombre_completo.split(" "))
#Dos primeras letras del nombre
#[epieza en la posicion 0 y termina en la 2] (termina en la posicion -1)
letras1=nombre_completo[0:2]
print(letras1)
#Reemplazar en la cadena
nueva_frase=frase.replace("bonito","malvado")
print(nueva_frase)
#numero de caracteres en la cadena:largo
largo_cadena=len(nueva_frase)
print(largo_cadena)