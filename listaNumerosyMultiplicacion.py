numeros=[]
resultados=[]
i=0
while i<5:
    num=int(input("Ingresa un número: "))
    numeros.append(num)
    i=i+1
multiplicador=int(input("¿Por cuánto deseas multiplicar?:"))

for num in numeros:
    resultado=num*multiplicador
    resultados.append(resultado)

print("Números originales:", numeros)
print("Resultados:", resultados)
#EXTRA
numBuscar=int(input("¿Qué número buscas?"))
if numBuscar in resultados:
    print("Sí está")
else:
    print("No está")