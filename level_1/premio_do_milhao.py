n=int(input())
soma=0
lista=[]
for i in range(n):
    lista.append(int(input()))
i=0
while soma<1000000:
    soma+=lista[i]
    i+=1
print(i)