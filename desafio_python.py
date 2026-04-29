nombre= input("Nombre: ")
edad= int(input("Edad: "))
puntaje= int(input("Puntaje: "))
asistencia= float(input("% Asistencia: "))
codigo= input("Codigo: ")
print(nombre.upper())
print('Caracteres:'len(nombre))
promedio= (puntaje + asistencia) / 2
print("El promedio es: ", promedio)
if edad >= 14:
    if puntaje >= 80:
        if codigo == ("PYTHON2026"):
            print("Resultado: Acceso VIP")
        else:
            print("Resultado: Acceso regular")
    elif puntaje >= 60 and puntaje <=79:
        print("Resultadoo: Acceso con observación")
    else:
        print("Resuñtado: Acceso denegado por bajo rendimiento")
else:
    if codigo == ("PYTHON2026"):
        print("Resultado: Acceso con especial con acompañante")
    else:
        print("Resultado: No cumple la edad minima")
if puntaje >= 90 and asistencia >= 90:
    print("Mensaje adicional: Candidato destacado")
elif puntaje >= 50 and asistencia >= 50:
    print(" Mensaje adicional: Requiere refuerzo previo")