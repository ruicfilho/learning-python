lista=list(input())
i=len(lista)
soma=0
for j in range(i):
    k=i-1-j
    if lista[k]!="a" and lista[k]!="e" and lista[k]!="i" and lista[k]!="o" and lista[k]!="u":
        del lista[k]
inversa=lista[ : : -1]
i=len(lista) 
for j in range(i):
    if lista[j]==lista[i-1-j]:
        soma+=1
    else:
        break
if soma==i:
    print("S")
else:
    print("N")