#Type hint ou Type Annotation: anotacoes de tipos, em traducao livre
#python tem tipagem dinamica, mas podemos informar o tipo de variavel
#mas isso nao faz com que o codigo nao rode se usarmos um diferente tipo da informada!!!!
#nome_variavel: tipo = valor
inteiro: int = 12

#para estruturas:
#estrutura: tipo_de_estrutura[tipo_de_variavel_armazenada]=[variaveis]
d: dict[str, str | int] = { #dict[chave, valor(str ou int)]
    "Rui": 12,
    "Vics": "12"
}

#Type Alias: armazenamos tipos de dados em variáveis:
ListaString= list[str]
lista: ListaString = ["v", "r"]

#para classes:
class MinhaClasse: #criamos uma classe vazia
    pass
obj: MinhaClasse=MinhaClasse() #indicamos que obj deve ser uma instância de MinhaClasse

#para bom uso de funcoes:
def funcao(x:float, y:float) -> int: #recebe dois parametros floats e retorna um inteiro
    return x+y
def imprime(s: str) -> None: #indicamos que a funcao nao retorna nada util, mas isso nao muda o codigo, podemos ate inserir um return
    print(s) #sintaticamente, ao terminar print, ela realiza return


#para poder ser informado se for usado um tipo diferente do declarado, use pip install mypy==0.991

