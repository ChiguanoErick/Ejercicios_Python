a = float(input('Ingrese un numero:'))
if a==0:
    print('El numero es 0')
else:
    if a > 0 and a%2==0:
        print('A es un numero par positvo')
    else:
        if a < 0 and a%2==0:
            print('A es un numero par negativo')
        else:
            if a > 0 and a%2==1:
                print('A es un numero primo positvo')
            else:
                print('A es un numero primo negativo')

a = float(input('Ingrese un numero:'))
if a == 0:
    print('A es 0')
elif a > 0 and a%2==0:
    print('A es un numero par positvo')
elif a < 0 and a%2==0:
    print('A es un numero par negativo')
elif a > 0 and a%2==1:
    print('A es un numero primo positvo')
else:
    print('A es un numero primo negativo')
    
edad=int(input('Ingresa tu edad: '))
print('Mayor de edad') if edad > 18 else print ('Menor de edad') 