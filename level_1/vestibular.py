n=int(input())
gabarito=list(map(str, input()))
resposta=list(map(str, input()))
soma=0
for i in range(n):
    if gabarito[i]==resposta[i]:
        soma+=1
print(soma)

