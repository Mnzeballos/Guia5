#Haga un programa en python donde tome dos valores de entrada: sueldo y rango.
#Con ello, calcule la asignación que percibirá el empleado, considerando la siguiente tabla:
#RANGO FÓRMULA
#1 sueldo x 0.83
#2 sueldo x 1.2
#3 sueldo x 5
print("¿Cuál es su sueldo?")
sueldo=int(input())
print("¿Cuál es su rango?")
rango=int(input())
if rango == 1:
    print("El sueldo es:$",sueldo*0.83,"para el rango: 1")
elif rango == 2:
    print("El sueldo es:$",sueldo*1.2,"para el rango: 2")
else:
    print("El sueldo es:$",sueldo*5,"para el rango: 3")