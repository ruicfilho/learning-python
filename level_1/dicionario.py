#o dicionario é semelahnte a uma lista
dicionario = {}
print(type(dicionario))

dicionario= {
    "Tiago": "tiago@neps.com",
    "Rui": "ruimacielfilho@gmail.com"
}
print(dicionario["Rui"]) #imprime o valor da chave Rui
print(dicionario.get("Rui", "Chave não encontrada"))
print(dicionario.get("Luciana", "Chave não encontrada"))
dicionario["Rui"]= "notruiw@gmail.com"
print(dicionario["Rui"])
dicionario["Luciana"]="luciana.farias@tjpa.jus.br"
print(dicionario.get("Luciana", "Chave não encontrada"))
del dicionario["Tiago"]
print(dicionario.pop("John", "Chave não encontrada")) #deleta a chave caso exista, mas se não exisitr devolve chave não encontrada. Se deletar, exibe o elemento
#percorrer um dicionario
for chave in dicionario:
    print(chave, dicionario[chave])
#Outros tipos de retorno de valores:
for chave in dicionario.keys(): #para cada chave do dicionario
    print(chave) #imprime a chave 
for valor in dicionario.values(): #para cada valor do dicionario
    print(valor) #imprime o valor
for chave,valor in dicionario.itens(): #para cada chave e valor no dicionario
    print(chave, valor) #imprime a chave e o valor

#verificar a existencia de elementos no dicionario:

print("Rui" in dicionario)
print("Luciana" in dicionario.keys())
print("notruiw@gmail.com" in dicionario.values())

