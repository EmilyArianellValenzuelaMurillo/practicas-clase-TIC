nombres = ["Angel", "Karla", "Luis", "Mateo", "Maria", "Luis", "Karla"]
print(f"Los nombres que se tienen son: {nombres}")
nombreBuscar = input("¿Qué nombre deseas buscar?: ")
encontrado = False
contador = 0
i = 0
while i < len(nombres):
    if nombres[i] == nombreBuscar:
        encontrado = True
        contador = contador + 1
        print("Encontrado en la posición:", i)
    i = i + 1

if encontrado == True:
    print("Nombre encontrado")
    print("Aparece", contador, "veces")
else:
    print("Nombre no encontrado")

# Extra
if contador > 1:
    while nombreBuscar in nombres:
        nombres.remove(nombreBuscar)
    print("Lista actualizada sin el nombre repetido:", nombres)