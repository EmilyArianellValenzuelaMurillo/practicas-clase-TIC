#Programa para calcular áreas
#Área cuadrado; lado x lado
lado=float(input("Ingresa lado"))
areaCuadrado=lado*lado
print("El área es ", areaCuadrado)
print(f'El área es {areaCuadrado}')
#Área triangulo; base x altura / 2
#pedir base
base=float(input("Ingresar base"))
#pedir altura
altura=float(input("Ingresar altura"))
#calcular el área
area_triangulo=(base*altura)/2
#Muestra el resultado
print(f'El area del triangulo es: {area_triangulo}')
#Área de un trapecio; (base mayor+base menor) * altura / 2
#pedir base mayor
base_mayor=float(input("Ingresar la base mayor"))
#pedir base menor
base_menor=float(input("Ingresar la base menor"))
#pedir altura
altura=float(input("Ingresar la altura"))
#calcular área
area_trapecio=((base_mayor+base_menor)*altura)/2
#muestra el resultado
print(f'El área del trapecio es:{area_trapecio}')
radio=float(input("Ingresar el radio"))
area_circulo=3.1416*(radio*radio)
print(f'El área del circulo es:{area_circulo}')
perimetro=float(input("Ingresar perimetro"))
apotema=float(input("Ingresar apotema"))
area_pentagono=(perimetro*apotema)/2
print(f'El área del pentagono es: {area_pentagono}')



