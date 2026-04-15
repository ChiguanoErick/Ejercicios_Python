#Actividad de OPERADORES 
#%% 
edad=int(16) 
#%% 
estatura=float(1.66) 
#%% 
print("Área de un triángulo") 
base, altura = float(input("Ingresa la base del triangulo:")), float(input("Ingresa la altura del triángulo:")) 
print("Área = ", 0.5*base*altura) 
#%% 
print("Perimetro de un triángulo") 
a,b,c=float(input("Ingresa la medida del lado a:")),float(input("Ingresa la medida del lado b:")),float(input("Ingresa la medida del lado c:")) 
print("Perímetro = ", a+b+c) 
#%% 
print("Área de un rectángulo") 
longitud, ancho = float(input("Ingresa la longitud del rectángulo:")), float(input("Ingrese el ancho del rectángulo:")) 
print("Área = ", longitud*ancho, "Perímetro = ",2*(longitud+ancho)) 
# %% 
print("Área y circunferencia") 
π=3.14 
r=float(input("Radio del circulo:")) 
print("Área = ",π*r**2, "Circunferencia = ", 2*π*r) 
# %% 
print("Pendiente y distancia") 
x1, y1, x2, y2 = 2, 2, 6, 10 
print ("m = ", (y2 - y1) / (x2 - x1)) 
import math 
print("Distancia euclidana = ", math.sqrt((x2 - x1)**2 + (y2 - y1)**2)) 
#%% 
print("Funcion: y = x² + 6x + 9") 
for x in range(-5, 5): 
    y = x**2 + 6*x + 9 
    if y == 0: 
        print("y = 0 cuando x = ", x) 
#%% 
print("Longitud de palabras") 
print("Python: ", len("python"), "Dragón: ", len("dragón")) 
len("python")>len("dragón") 
#%% 
print("Verificación") 
print("on" in "python" and "on" in "dragon") 
#%% 
print("jerga" in "Espero que este curso no esté lleno de jerga.") 
#%% 
print("Float/String") 
print(len("python")) 
print(float(len("python"))) 
print(str(len("python"))) 
# %% 
print("División entera: 7/3") 
print(7//3 ==2.7)  
# %% 
print("Verficación 2") 
print(type("10")==type(10)) 
print("Verficación 3") 
print(int(9.8)==10) 
# %% 
print("Pagos") 
h,tarifa=float(input("Ingresa el numero de horas:")), float(input("Ingrese la tarifa por hora:")) 
print("El pago total es:", h*tarifa) 
# %% 
años = float(input("Años vividos: ")) 
segundos= años*365*24*60*60 
print("Has vivido:", segundos, "segundos") 
# %% 
for i in range(1,6): 
    print(i,1,i**2,i**3)   