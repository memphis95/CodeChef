import math
import sys

input = sys.stdin.readline

def isPrime(n):
    try:
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True
    except Exception:
        pass


t = int(input())
for i in range(0,t):
    n = int(input())
    result = isPrime(n)
    if result:
        print("yes")
    else:
        print("no")