#Programa que me indica como me fue
calif=float(input("¿Cuál es tu calificación?"))
if calif==10:
    print("Exelente!!!")
elif calif==9:
    print("Muy bien")
elif calif==8:
    print("Bien")
elif calif==7:
    print("Puedes mejorar")
elif calif==6:
    print("De panzazo jeje")
else:
    print("Chanclazoo")
#Temperatura
temp=float(input("¿Cuál es la temperatura de hoy?"))
if temp>=40:
    print("Hace mucho calor")
elif temp>=30 and temp<40:
    print("Esta templadito")
elif temp>=20 and temp<30:
    print("Está fresco")
elif temp<20:
    print("Hace frío")
else:
    print("No valido")
#Solicitar sexo tipo cadena
#Solicitar edad ipo entero
sexo=input("¿Cuál es tu sexo?")
edad=int(input("¿Cuál es tu edad?"))
if sexo=="hombre" and edad>=18:
    print("Puedes sacar cartilla militar")
else:
    print("No puedes sacar cartilla militar")