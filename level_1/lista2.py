lista=[1, 2.0, 3, 4.00, 5]
lista[0]=1
lista[1]=2
lista[2]=3
lista[3]=4
lista[4]=5
print(lista)
lista.insert(1,45)
print(lista)
lista.insert(0,34)
print(lista)
lista.insert(6, 6)
print(lista)
#o insert sempre adiciona a variavel ao lado esquerdo da posição escolhida, consequentemente, a lista aumenta de tamanho
del lista[6]
del lista[2]
del lista[0]
print(lista)
#se eu deletasse em uma ordem que não fosse do maior para o menor, eu  teria problemas, pois os indices mudam