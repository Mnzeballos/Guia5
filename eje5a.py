import time
import sys
print("Contar hasta")
n=int(input())
def contador():
    for i in range(1, n+1):
        print(i)
        time.sleep(1)
#if __name__ == "__main__":
#   if len(sys.argv) != 2:
#        print("Uso: python contador3.py <número>")
#        sys.exit(1)
#    n = int(sys.argv[1])
#    contador(n)