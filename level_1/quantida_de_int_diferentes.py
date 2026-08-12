n=int(input())
lista=[]
for i in range(n):
    lista.append(int(input()))
numeros={valor for valor in lista}
print(len(numeros))

#
n=int(input())
numeros={int(input()) for _ in range(n)}
print(len(numeros))