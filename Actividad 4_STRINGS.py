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
print("-".join(texto)) 
#Nivel 5: Indices 
print(texto[0]) 
print(texto[-1]) 
print(texto[5]) 
#Nivel 6 
nombre="Erick Chiguano" 
print(f"Hola, mi nombre es {nombre}") 
iniciales = nombre.split() 
acronimo = iniciales[0][0] + iniciales[1][0] 
print("Acrónimo:", acronimo) 

 

