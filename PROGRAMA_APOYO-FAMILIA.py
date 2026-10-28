sexo=input("Introducir sexo:")
edad=int(input("Introducir edad:"))
estado_civil=input("Introducir estado civil:")
cantidad_hijos=int(input("Introdicir cantidad de hijos"))
if sexo=="mujer" and cantidad_hijos=="1" and edad<18:
    print("Eres mujer, tienes un hijo y eres menor de edad entonces el apoyo será de $800")
elif sexo=="mujer" and cantidad_hijos==1 and edad>=18:
    print("Eres mujer, tienes un hijo y eres mayor de edad entonces el apoyo será de $300")
elif sexo=="mujer" and cantidad_hijos>1 and edad<18:
    print("Eres mujer, tienes más de un hijo y eres menor de edad entonces el apoyo es de $1500")
elif sexo=="mujer" and cantidad_hijos>1 and edad>=18:
    print("Eres mujer, tienes más de un hijo y ya eres mayor de edad entonces el apoyo es de $500")
elif sexo=="hombre" and cantidad_hijos>=1 and estado_civil=="soltero":
    print("Eres hombre y tienes hijos, el apoyo es de $780")
else:
    print("No válido")