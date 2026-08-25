#classe é o modelo. É um conjunto de características intrisecas. (ex: ser humano: altura, idade, pes)
#objeto tem características individuais(atributos) que pertencem ao mesmo conjunto das da classe (ex: Rui(objeto): 1,67(atributo), 18, 72)
#métodos são açôes que os objetos podem tomar (ex: falar, correr, dormir)
#ATRIBUTOS E MÉTODOS DEVEM SER DETERMINADOS PELA CLASSE
#ATRIBUTOS SÃO REPRESENTADOS POR VARIÁVEIS, MÉTODOS POR FUNÇÃO

class MinhaClasse:
    pass
objeto1 = MinhaClasse()
objeto1.atr = "atributo teste de objeto1"

objeto2 = MinhaClasse()
objeto2.atr = "atributo teste de objeto2"
print(objeto1) 
#outra maneira de verificar se o um objeto é de fato um objeto e pertence a classe específica é:
print(isinstance(objeto1,MinhaClasse))  #imprime true 
print(objeto1.atr)
print(objeto2)
print(objeto2.atr)

#atributos estáticos são atributos compartilhados por todas as instâncias
#eles devem ser atribuídos dentro da classe
class MinhaClasseDois:
    A = 10
objeto_new = MinhaClasseDois()
print(objeto_new.A)
print(MinhaClasseDois.A)

#ALTERAÇÃO DE ATRIBUTO

class MinhaClasseNew():
    A = 10 
obj01 = MinhaClasseNew()
obj02 = MinhaClasseNew()

print(f"Antes: {obj01.A}, {obj02.A}")
MinhaClasseNew.A = 2 
print(f"Depois: {obj01.A}, {obj02.A}")



