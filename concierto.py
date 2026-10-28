edad=int(input("¿Cuántos años tienes?"))
permiso=input("¿Tienes permiso de tus padres?")
acompañante=input("¿Vas a ir acompañado?")
if edad>=18 or permiso=="si":
    print("Puedes entrar al concierto")
elif edad>=18 or acompañante=="si":
    print("Puedes entrar al concierto")
else:
    print("No puedes entrar al concierto")