#funcao de ordem superior
#é aquela que retorna uma funcao ou a que possui uma funcao como parametro
def ola(nome):
    return f"Ola {nome}"
def imprime_ola(funcao, nome):
    print(funcao(nome))
imprime_ola(ola, "Rui")
#imprime_ola é uma funcao superior

#funcao anonima, é uma funcao simples de apenas 1 expressao
funcao_anonima= lambda n: n+5
funcao_anonima= lambda a,b,c,d: a+b+c

#funcao map, é aquela que recebe uma funcao como parametro e aplica em alguma lista de variaveis
#exemplo sem map:
quadrado= lambda x:x**2
lista_quadrado=[]
lista=[1,2,3,4]
for _ in lista:
    lista_quadrado.append(quadrado(_))
print(lista_quadrado)
#com map:
quadrado1= lambda x:x**2
lista1=[1,2,3,4]
lista_quadrado2=list(map(quadrado1, lista1))
print(lista_quadrado2)

#funcao filter, é aquela que recebe uma funcao como parametro e um conjunto de valores e retorna uma lista de elementos no qual
#a funcao parametro retorna true
lista=[1,2,3,6,10,11]
lista2=list(filter(lambda x: x>=10, lista))
print(lista2)

#funcao reduce, reduz um conjunto de valores a apenas um valor:
lista3=[2,4,6]
produto=1
for item in lista3:
    produto *= item
print(produto)
#façamos usando reduce:
from functools import reduce
produto= lambda x,y: x*y
resultado=reduce(produto, lista3)
print(resultado)

