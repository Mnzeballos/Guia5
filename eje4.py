#Reemplace el ejercicio 3 por una implementación con parámetros pasados por
#consola usando la librería sys.
import sys
print("¿Cuál es su sueldo?")
sueldo=int(sys.stdin.readline())
print("¿Cuál es su rango?")
rango=int(sys.stdin.readline())
if rango == 1:
    print("El sueldo es:$",sueldo*0.83,"para el rango: 1")
elif rango == 2:
    print("El sueldo es:$",sueldo*1.2,"para el rango: 2")
else:
    print("El sueldo es:$",sueldo*5,"para el rango: 3")