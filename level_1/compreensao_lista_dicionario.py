
#criação de listas a partir de outras
lista=[1, 2, 3, 4]
lista_modificada=[]
for item in lista:
    lista_modificada.append(item +1)
#outro modo:
lista=[1, 2, 3, 4]
lista_modificada=[item +1 for item in lista] #aqui a declaração já atribui valores
lista_modificada=[item for item in lista if item%2==0]
lista_modificada=[f"{item} eh par" if item%2==0 else f"{item} eh impar" for item in lista]

#dicionarios
lista=[1, 2, 3, 4]
dicionario={}
for item in lista:
    if item%2==0:
        dicionario[item]= item**2
#outro modo
dicionario={item: item**2 for item in lista if item%2==0} #aqui não foi necessário entrar com o if no laço 
#nesse modo trabalha-se com comprehensions:
#este é um conceito que o nome vem da matemática o "set comprehension" ou compreensão de conjuntos
# exemplo {x pertence a B/ P(x)=x^2}
#em python, usa-se uma sintaxe semelhante para dicionários, listas ou conjuntos:
#list comprehension: [x**2 for x in lista]
#Dictionary comprehension: {x:x**2 for x in lista}
#Set comprehension: {x**2 for x in lista}
#Generator comprehension(gera um iterador sem armazenar tudo na memória): (x**2 for x in lista)
#ou seja:
#forma tradicional:
dicionario = {}

for item in lista:
    if item % 2 == 0:
        dicionario[item] = item**2
#comprehension:
dicionario = {
    item: item**2
    for item in lista
    if item % 2 == 0
}

#dicionario a partir de outro:
alunos={
    "Rui": 9,
    "Victoria": 9,
    "Caio":10


}
alunos_atualizado= {chave.upper(): item +1 if item<=9 else item for chave,item in alunos.items()}
print(alunos_atualizado)
