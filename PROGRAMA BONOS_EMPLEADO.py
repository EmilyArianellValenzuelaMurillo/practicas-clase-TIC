nomb=input("Ingresar nombre")
pago_por_hora=float(input("Ingresar pago por hora"))
horas_mes=int(input("Ingresar horas trabajadas al mes"))
sueldo=pago_por_hora*horas_mes
print("Su sueldo mensual es:$",sueldo)
if sueldo>=100 and sueldo<=300:
    print("Su bono es de $500")
    print("Su sueldo final es:$",sueldo+500)
elif sueldo>300 and sueldo<=1500:
    print("Su bono es de $1700")
    print("Su sueldo final es:$",sueldo+1700)
elif sueldo>1500 and sueldo<=3000:
    print("Su bono es de $3500")
    print("Su sueldo final es:$",sueldo+3500)
elif sueldo>3000 and sueldo<=8000:
    print("Su bono es de $8500")
    print("Su sueldo final es:$",sueldo+8500)
elif sueldo>8000:
    print("Su bono es de $10,000")
    print("Su sueldo final es:$",sueldo+10000)
else:
    print("No válido")
