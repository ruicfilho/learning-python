#usamos set quando queremos abandonar valores repetidos ou criar um conjunto
set_exemplo={1, 2, 3, 4,}
print(type(set_exemplo))
lista=[1, 2, 2, 3, 3, 3, 5]
set_new=set(lista)
print(set_new)
#adicionar ou remover elementos do set:
set_new.add(4)
set_new.remove(1)
print(set_new)
#para não retornar erro ao terminal se a chave não existir
set_new.discard(6)
#os elementos são armazenados de forma desordenada, se aparecer ordenado é conincidencia do método dele
teste={5,4,3,6,7,2,1}
for item in teste:
    print(item, end=" ")
#verificar exsitencia de elemento:
print(10 in teste)
print(1 in teste)
#uniao
s={1,2}
t={3,2}
print(s|t)
#intersecao
print(s & t)
print(s.intersection(t))
#diferenca
print(s-t)
print(s.difference(t))

#tupla
#sao semelhantes a listas, mas imutaveis. Os itens permanecem na ordem definida e podem ser repetidos
tupla=(1,2)
print(type(tupla))
tupla_falsa=(1)
print(type(tupla_falsa))
tupla_verdadeira=(1, )
print(type(tupla_verdadeira))
print(tupla[1])
#comparacao de tuplas:
A = (1, 2) 
B = (1, 2) 
C = (2, 3)

print(A < C) # True. Pois 1 < 2
print(A > C) # False. Pois 1 < 2
print(A == B) # True. Pois 1 == 1 e 2 == 2.

#Listas: coleção ordenada e mutável de elementos, indexada e que permite elementos duplicados.
#Tuplas: coleção ordenada e imutável de elementos, indexada e que permite elementos duplicados.
#Set: coleção desordenada, não indexada e que não permite elementos duplicados.
#Dicionário: coleção ordenada e mutável, não permite chaves duplicadas.

#Podem ser armazenados diferentes tipos de dados em uma tupla.

#Uma tupla pode ser chave de dicionário e set, pois é imutável

#Quando utilizamos o enumerate na aula de listas, em cada iteração, estávamos na verdade acessando uma tupla 