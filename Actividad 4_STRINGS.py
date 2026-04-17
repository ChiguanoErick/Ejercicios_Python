#Actividad de STRINGS
#Nivel 1: Operaciones básicas
texto="Programación Para Todos"
print(texto)
print(len(texto))
#Nivel 2: Transformación de texto
print(texto.upper())
print(texto.lower())
print(texto.title())
print(texto.capitalize())
#Nivel 3: Busqueda y verificación
print(texto.startswith('Programación'))
print(texto.endswith('Todos'))
print(texto.find("Para"))
print('Python'in texto)
#Nivel 4: Manipulación
print(texto.replace('Programación','Python'))
print(texto.split())
print(texto.join("_"))
#Nivel 5: Indices
print(texto[0])
print(texto[-1])
print(texto[5])

