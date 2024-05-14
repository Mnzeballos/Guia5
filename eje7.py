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
#def checkmem():
#	    result1 = commands.getoutput('free|grep Mem:|tr -s "'" "'" |cut -d "'" "'" -f 2')
#	    result2 = commands.getoutput('free|grep Mem:|tr -s "'" "'" |cut -d "'" "'" -f 3')
#	    result3=int(result2)*100/int(result1)
#	    return result3
#mem=checkmem()

# Para convertir bytes en Gigabytes
def bytes_to_GB(bytes):
    gb = bytes/(1024*1024*1024)
    gb = round(gb, 2)
    return gb
#memoria RAM
mem= psutil.virtual_memory()
print("\n---RAM disponible:", bytes_to_GB(mem.available), "Gb")
