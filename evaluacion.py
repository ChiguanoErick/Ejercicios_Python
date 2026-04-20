# ===== PARTE A =====
# a) Indica el tipo de variable
# Respuesta:
#str
#int
#float
#list
# b) Escribe qué mostraría el programa en pantalla
# Respuesta:
#<class 'str'>
#<class 'int'>
#<class 'float'>
#<class 'list'>
# Explica qué hace len(nombre)
# len(nombre) va a devolver el numero de caracteres que contiene esa variable tipo str
#2. Comprensión conceptual (15 puntos)
#a) ¿Qué diferencia hay entre print() e input()?
#print() se encarga de mostrar el resultado del codigo en la terminal mientras que input() se encarga de habilitar al usuario para que escriba una respuesta ya sea tipo str, int o float
#b) ¿Por qué un dato ingresado con input() puede dar error si se usa directamente en un cálculo?
# Puede dar error si el tipo de dato ingresado no coincide con el tipo de dato de los clauclos. Por ejemplo si se ingresa solo input() sin especificar el tipo de dato, el programa lo toma como una cadena de texto sin importar que lo ingresado sea un valor numerico, por lo tanto al realizar el calculo no se pueden realizar las operaciones correspondientes.
#c) Explica la diferencia entre /, // y %.
# / se utliza para obtener el resultado de una division (5/2=2.5); // se utliza para obtener el resultado entero de la division (5//2=2) y % se utliza para obtener el residuo de la division (5%2=1)
#d) Escribe una instrucción que permita comprobar la versión de Python que se está usando.
#python --version
#e) Escribe una instrucción que permita consultar las palabras reservadas de Python
#keywords.python
# ===== PARTE B =====
# 3. Corrección de código (15 puntos)
# El siguiente programa tiene errores. Reescríbelo de forma correcta para que funcione
#ancho = float(input("Ingrese el ancho del terreno: "))
#largo = float(input("Ingrese el largo del terreno: "))
#precio = float(input("Ingrese el precio por metro cuadrado: "))
#area = ancho * largo
#costo = area * precio
#print("Área total: ", area)
#print("Costo estimado: ", costo)
# a) ¿Cuáles eran los errores principales?
# 1. El tipo de dato en el input() no estaba especificado por lo que los datos ingresados se iban a interpretar como cadenas de texto.
# 2. En el print de los resultados las variables estaban con un + para concatenar, pero esto solo es valido para cadenas de texto. Por lo tanto lo ideal es separar el texto de las variables con una coma.
# b) ¿Por qué tu corrección sí permite obtener resultados válidos?
# Porque al especificar el tipo de dato en el input() como float, el programa ya lo interpreta como un dato numerico para poder realizar los calculos. Ademas separando las variables con una coma perimite que el print final se visualizen las respuestas correctas y no un error al intentar concatenar datos que no son str
# 4. Construcción breve (15 puntos)
#Escribe un fragmento de código que haga lo siguiente:
#1. Cree la variable frase con el texto "Tecnología para todos".
#2. Muestre la frase en mayúsculas.
#3. Muestre la cantidad de caracteres de la frase.
#4. Verifique si la palabra "Python" está dentro de la frase.
#5. Reemplace "Tecnología" por "Programación
#texto = "Tecnología para todos"
#print(texto.upper())
#print(len(texto))
#print('python' in texto)
#print(texto.replace('Tecnología', 'Programación'))

