'''
Cree un programa en Python que imprima la hora del sistema, estado de memoria
RAM y almacenamiento disponible en la partición montada en “/”.
'''
import datetime
import time
print("La hora es:", time.strftime("%H:%M:%S", time.localtime()))