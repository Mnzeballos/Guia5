'''
Cree un programa en Python que imprima la hora del sistema, estado de memoria
RAM y almacenamiento disponible en la partición montada en “/”.
'''
import time
import os
#import commands
#import sys
#import getop
import psutil

## Hora
print("La hora es:", time.strftime("%H:%M:%S", time.localtime()))

## Memoria

# Para convertir bytes en Gigabytes
def bytes_to_GB(bytes):
    gb = bytes/(1024*1024*1024)
    gb = round(gb, 2)
    return gb
#memoria RAM
mem= psutil.virtual_memory()
print("\n---RAM disponible:", bytes_to_GB(mem.available), "Gb")
print("\n---RAM utilizada:", bytes_to_GB(mem.used), "Gb")
print("\n---RAM total:", bytes_to_GB(mem.total), "Gb")

## Almacenamiento
alm=psutil.disk_usage(path='/')
print("Almacenamiento disponible en /",bytes_to_GB(alm.free))