nombres=[]
i=0
while i<5:
    nombre=input("Ingresa un nombre")
    nombres.append(nombre)
    i=i+1

for nombre in nombres:
    print(nombre.upper())