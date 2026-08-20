#podemos armazenar funções em variáveis
import math
def converter(x, func): #por enquanto, func é apenas uma variável qualquer
    return func(x)
print(converter("Minha string", str.upper)) #agora, nossa variável func recebe uma função (str.upper) e nossa func aplica em x
#também pode-se fazer
def calculo(x,y):
    return x**2 + y**2
novo_calculo=calculo 

  
#ao definir funções, é sempre ótimo escrever um docstring que explique o propósito, parametro e valor de retorno da função, veja:
def calculo(x, y):
    """
    Calcula a soma dos quadrados de x e y.

    Parâmetros:
    x (int): O primeiro número
    y (int): O segundo número

    Retorna:
    int: A soma dos quadrados de x e y
    """
    resultado = x ** 2 + y ** 2
    return resultado

#parametros e valores padrão

def cumprimentar(nome, saudacao="Ola"):
    """

    Imprime uma mensagem de saudação

    Parâmetros:
    nome(string): o nome da pessoa
    saudacao(string): o tipo de saudação

    Retorna:
    string: a saudação
    """ 
    return print(f"{saudacao}, {nome}!")
cumprimentar("Rui")
cumprimentar("Rui", "Bom dia")

#agora vamos criar outro arquivo em CODES IN PY e criar um modúlo nesse arquivo, depois vamos importar o modulo para nosso código.
import minhas_funcoes
operacao=minhas_funcoes.potencia
print(operacao(*map(float, input().split()))) #aqui, o * realiza o desempacotamento, pois estamos chamando a função ou atribuindo


#outro metodo:
from minhas_funcoes import potencia# Apenas a função calculo importa

resultado = potencia(10, 2) # Armazena o resultado da função
print(resultado) # Imprime o resultado: 104

