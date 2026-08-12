lista_de_inteiros = map(int, input().split())

resultado = [elemento*2 if elemento%2==0 else elemento*3 for elemento in lista_de_inteiros]

print(resultado)