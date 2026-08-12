n=int(input())
lista=list(map(int, input().split()))
i=0
l1=0
l2=0
aux=0
for i in range(n):
    if lista[i]==1:
        l1 ^= 1 # ^= faz xnor com 1, 1^1=0, 0^1=1
    else:
        l1 ^= 1
        l2 ^= 1
print(l1)
print(l2)