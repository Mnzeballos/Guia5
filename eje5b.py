import time
import sys
print("Segunda cuenta hasta:",sys.argv[1])
n2=int(sys.argv[1])
for i in range(1, n2+1):
    print("Cuenta 2:",i)
    time.sleep(1)
