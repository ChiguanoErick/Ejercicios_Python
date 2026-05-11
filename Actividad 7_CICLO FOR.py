''' #LISTA

notas= [8,7,9,10,6]
suma=0
for nota in notas:
    suma= suma + nota
promedio= suma/len(notas)
print(promedio)
'''
''' # CON STR
language=input('Nombre y Apellido: ')
for letter in language:
    print(letter)
'''
'''
#  CASO PRACTICO: CAZADOR DE VOCALES 
palabra=input('Ingrese una palabra:')
vocales=0
consonantes=0
for letra in palabra:
    if letra == 'a' or letra =='e' or letra == '1' or letra == 'o' or letra == 'u':
        vocales = vocales + 1
    else:
        consonantes = consonantes + 1
print('La cantidad de vocales es:', vocales)
print('La cantidad de consonantes es:',consonantes )
'''
'''
palabra=input('Ingrese una palabra:')
vocales=0
consonantes=0
for letra in palabra:
    if letra in 'aeiouAEIOU':
        vocales = vocales + 1
    else:
        consonantes = consonantes + 1
print('La cantidad de vocales es:', vocales)
print('La cantidad de consonantes es:',consonantes )
'''
''' # SET (CONJUNTO)
it_companies = {'Facebook', 'Google', 'Amazon', 'Facebook'}
for company in it_companies:
    print (company)
'''
'''
asistentes = {'Ana', 'Luis', 'Maria','Ana', 'Carlos', 'Luis', 'Sofia'}
for estudiante in asistentes:
    print('Generar certificado para estudiante:', estudiante)
'''
'''
numbers=[1,2,3,4,5]
for number  in numbers:
    n=int(input('Ingresa un numero: '))
    if n in numbers:
        print('Ganaste')
        break
    else:
        print('Perdiste')
'''