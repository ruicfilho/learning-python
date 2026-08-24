#para criar métodos basta criar uma função dentro da classe
class Pessoa:
    def falar(self):
        print("Olá!")

p=Pessoa()
p.falar() #isso é basicamente fazer "objeto p, execute falar"
#fazemos isso e usamos self porque o python faz isso, internamente: Pessoa.falar(p) e falar recebe p como self
Pessoa.falar(p)

#um método importante é o construtor. Ele é um método que é chamado automaticamente quando criamos uma instância de uma classe
class MinhaClasse:
    def __init__(self):
        print("construindo o objeto")
objeto = MinhaClasse()
#isto é, este método é chamado automaticamente na instanciação do objeto

#aplicação do método construtor
class MinhaClasseNew():
    def __init__(self, valor_atr_1, valor_atr_2):
        self.atributo1 = valor_atr_1
        self.atributo2 = valor_atr_2
objeto_new = MinhaClasseNew("atributo 1", "atributo 2")
print(objeto_new.atributo1)
print(objeto_new.atributo2)
#ou seja, ao criar um objeto, o pyhton faz instantaneamente: __init__(objeto_new, "atributo 1", "atributo 2")


#método de classe:

class MyClass:
    @classmethod
    def metodo_de_classe(cls):
        print(cls)
MyClass.metodo_de_classe()
#aqui, diferente do self, que era o objeto, cls é classe





