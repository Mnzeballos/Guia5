import time
import sys
print("Contar hasta")
n=int(input())
def contador(n):
    for i in range(1, n):
        print(i)
        time.sleep(1)
