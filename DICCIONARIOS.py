#Listas
alumnos=["Juanito", "Angelica"]
#Diccionarios
alumno1={
    "nombre":"Juanito",
    "edad":15,
    "promedio":8.2
}
alumno2={
    "nombre":"Angelica",
    "edad":18,
    "promedio":10
}
#Consultar valores
#Forma1
print("Nombre :", alumno1["nombre"])
#Forma2 2
print("Nombre: ", alumno1.get("nombre"))
#Modificarr algun campo
alumno1["nombre"]="Pedrito"
print("Nombre: ", alumno1.get("nombre"))
#Mostrar CLAVE:VALOR
for clave, valor in alumno1.items():
    print(clave, ":", valor)