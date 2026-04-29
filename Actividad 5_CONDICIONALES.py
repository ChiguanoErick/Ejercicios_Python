# Ejercicios: Nivel 1 
edad=int(input('Ingrese su edad: ')) 
if edad >=18: 
    print("Tienes la edad suficiente para aprender a conducir") 
else:
    diferencia= int(18-edad) 
    print(f"Necesitas {diferencia} años más para poder aprender a conducir") 

 
my_age, your_age = 16, int(input('Ingresa tu edad: ')) 
if my_age > your_age: 
    dif = my_age - your_age 
    if dif == 1: 
        print(f'Soy {dif} año mayor que tú') 
    else: 
        print(f'Soy {dif} años mayor que tú') 
else:
    if your_age > my_age: 
        dif = your_age - my_age 
        if dif == 1: 
            print(f'Eres {dif} año mayor que yo') 
        else: 
            print(f'Eres {dif} años mayor que yo') 
            if your_age==my_age:
                print('WOW, tenemos la misma edad') 

 
a = float(input("Ingrese el primer número: ")) 
b = float(input("Ingrese el segundo número: ")) 
if a > b: 
    print(f"{a} es mayor que {b}") 
elif a < b: 
    print(f"{a} es menor que {b}") 
else: 
    print(f"{a} es igual a {b}") 

nota = int(input("Ingrese su puntaje: ")) 
if 90 <= nota <= 100: 
    print("A") 
elif 80 <= nota <= 89: 
    print("B") 
elif 70 <= nota <= 79: 
    print("C") 
elif 60 <= nota <= 69: 
    print("D") 
else: 
    print("F") 

 
 
mes = input("Ingrese el mes: ").lower() 
if mes in ["septiembre", "octubre", "noviembre"]: 
    print("Otoño") 
elif mes in ["diciembre", "enero", "febrero"]: 
    print("Invierno") 
elif mes in ["marzo", "abril", "mayo"]: 
    print("Primavera") 
elif mes in ["junio", "julio", "agosto"]: 
    print("Verano") 
else: 
    print("Mes no válido") 


fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruta = input("Ingrese una fruta: ").lower() 
if fruta in fruits: 
    print("Esa fruta ya existe en la lista") 
else: 
    fruits.append(fruta) 
    print("Fruta agregada:", fruits) 

 