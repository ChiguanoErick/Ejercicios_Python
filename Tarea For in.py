#%%
notas = [8.5, 6.0, 9.0, 7.0, 5.5]
sum=0
aprob=0
reprob=0
for num in notas:
    sum = sum + num
    if num >=7:
        aprob=aprob+1
    else:
        reprob=reprob+1
prom=sum/len(notas)
print(notas)
print(f'Suma total de notas:{sum}\nAprobados: {aprob}\nReprobados: {reprob}\nEl promedio del curso es: {prom}')
#%%
contrasena='Python2026'
letras=0
num=0
o=0
for x in contrasena:
    if x in '0123456789':
        num=num+1
    else:
        letras=letras+1
    if x == 'o':
        o=o+1
print(f'Letras: {letras}\nNúmeros: {num}\nLetra "o": {o}')   
# %%
productos = {"teclado", "mouse", "monitor", "mouse", "impresora"}
cant=0
u=0
for p in productos:
    u=u+1
    letras = 0
    for letra in p:
        letras= letras +1
    if letras >6:
            cant=cant +1
print(f'Hay {u} productos únicos\nProductos con mas de 6 letras: ', cant)
# %%
correo=input('Ingrese su correo electrónico: ')
user=''
for nombre in correo:
    if nombre == '@':
        break
    user=user+nombre
print(f'Usuario: {user}')
# %%
cel=input('Ingrese su numero celular: ')
nuevo=''
for x in cel:
    if x == '-' or x== ' ':
        continue
    nuevo = nuevo + x
print(f'Version final: {nuevo}')
