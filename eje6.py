'''
# Funciones de la calculadora
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2
# Introducción dos valores
print("Número 1")
num1=float(input())
print("operación (+, -, *, /):")
op=input()
print("Número 2")
num2=float(input())

# Calculo
if op=="+":
    print(f"Resultado:", suma(num1, num2))
if op=="-":
    print(f"Resultado:", resta(num1, num2))
if op=="*":
    print(f"Resultado:", multiplicacion(num1, num2))
if op=="/":
    print(f"Resultado:", division(num1, num2))
'''
#### OPCIÓN 2 CON EVAL
operacion=input("Introduzca su operación:")
print(operacion,"=",eval(operacion))