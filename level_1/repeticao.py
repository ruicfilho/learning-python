v=0
lista=[]
i=0
while v<10:
    lista.append(v)
    v=v+1
print(lista)

print("------------------")
for v in [0,2,4,6,8]:
    print(lista[v])
print("---------------------")
for v in range (10, 21):
    print(v)
print("-----------------")
for v in range (0,41, 2):
    print(v, end=' ')
print()
print("---------------------")
r=range(0,11)
print(r, end=' e ')
print(list(r))
print("---------------------")
print(lista)
print("quantos elementos tem a nossa lista inicial?")
print(len(lista))
for i in range(len(lista)):
    print(f"o indice {i} da lista armazena o elemento {lista[i]}")
print("---------------------")
for indice, elemento in enumerate(lista):
    print(indice, elemento)
#funcao enumerate retorna um tipo de dado chamado Tupla, a primeira variavel é o indice a segunda o elemento