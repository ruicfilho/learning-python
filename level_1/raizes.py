import math
n=int(input())
lista=list(map(float, input().split()))
for i in range(len(lista)):
    v=math.sqrt(lista[i])
    print(f"{v:.4f}")