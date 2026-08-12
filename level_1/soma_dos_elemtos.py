n=int(input())
lista=list(map(int, input().split()))
soma=0
for i in range(n):
    soma+=lista[i]
print(soma)