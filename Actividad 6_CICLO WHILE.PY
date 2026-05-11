opcion = ''
while opcion != '3':
    print('==MENU==')
    print('1. Saludar')
    print('2. Mostrar mensaje')
    print('3. Salir')
    opcion =input('Seleccione una opcion: ')

    if opcion=='1':
        print('Hola, bienvenido')
        break
    elif opcion=='2':
        print('Estamos aprendienco ciclos while')
        break
    elif opcion=='3':
        print('Saliendo del programa')
    else:
        print('Opcion no valida')

#%%
count=0
while count <5:
    print(count)
    count=count+1
    if count == 3:
        continue
    print(count)
#%%

intentos=0
while intentos <3:
    clave=input('Ingrese la clave: ')
    intentos=intentos+1
    if clave == 'python123':
        print('Clave correcta')
        break
else:
    print('Demasiados intentos')
#%%
n=0 

num=int(input("Ingrese un número entero positivo: ")) 

while num<1: 

    print("Numero invalido") 

    num=int(input("Ingrese un número entero positivo: ")) 

while n<=num: 

    if n%5==0: 

        n+=1 

        continue 

    else: 

        print(n) 

        n+=1 
# %%
