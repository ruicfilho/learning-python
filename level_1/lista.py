lista= [1, 3.0, "R", "RUI"]
lista.append("AFONSO")
print(lista)
print("-------------------")
print(lista[0])
print(lista[-4])
print(lista[2])
print(lista[3])
print(lista[4])
print(type(lista[0]))
print(type(lista[-4]))
print(type(lista[2]))
print(type(lista[3]))
print(type(lista[4]))
print("-------------------")
lista[0]=1
lista[1]=2
lista[2]=3
lista[3]=4
lista[4]=5
print(lista)
print(type(lista[0]))
print(type(lista[1]))
print(type(lista[2]))
print(type(lista[3]))
print(type(lista[4]))
lista.insert(5, 6)
print(lista)
