#uma funcao pode ser decorada inumeras vezes
def decorador1(func): #decorador 1

    def wrapper(*args,**kwargs):
        print("Decorador 1 chamado")
        func(*args, **kwargs)
        print("Decorador 1 finalizado")
    return wrapper

def decorador2(func):

    def wrapper(*args,**kwargs):
        print("Decorador 2 chamado")
        func(*args,**kwargs)
        print("Decorador 2 finalizado")
    return wrapper

@decorador2
@decorador1
def teste():
    print("função teste chamada")

teste()
#a função teste é decorada por decorador1, e a função resultante é decorada por decorador2

#informações de funções decoradas
def teste():
    pass
print(teste.__name__) #aqui é retornado o nome da função teste

def decorador(func):
    def wrapper(*args, **kwargs):
        return(func(*args, **kwargs))
    return wrapper

@decorador
def teste():
    pass 
print(teste.__name__) #aqui, infelizmente, perde-se a propriedade e é retornado wrapper

#contorna-se isso:
from functools import wraps
def decorador(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return(func(*args, **kwargs))
    return wrapper

@decorador
def teste():
    pass
print(teste.__name__)

#agora faremos um decorador que recebe paramêtro:

def criar_decorador(arg):
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Argumentos posicionais: {args}")
            print(f"Argumentos nomeados: {kwargs}")
            print(f"Argumentos do decorador: {arg}") #temos acesso ao argumento
            return func(*arg, **kwargs)

        return wrapper
    return decorador

@criar_decorador("argumento do decorador!!!")
def teste(arg1, arg2):
    pass 
teste("valor1", arg2="valor da chave arg2")



##contando o tempo de debug

from functools import wraps
import time


def calcular_tempo(func): # Decorador que calcula o tempo de execução da função
    @wraps(func)
    def wrapper(*args, **kwargs):

        tempo_inicial = time.time() # Armazena o tempo inicial
        retorno = func(*args, **kwargs) # Executa a função
        tempo_final = time.time() # Armazena o tempo final

        tempo_de_execucao = tempo_final - tempo_inicial # Calcula o tempo de execução
        print(f"{func.__name__} finalizada em  {tempo_de_execucao:.5f} segundos") 
        return retorno

    return wrapper

@calcular_tempo
def funcao_linear(): # Função de complexidade O(n) (linear)
    resultado = 0 
    for i in range(1000):
        resultado += i

@calcular_tempo
def funcao_quadrada(): # Função de complexidade O(n²) (quadrada)
    resultado = 0
    for i in range(1000):
        for j in range(1000):
            resultado += i + j


funcao_linear()
funcao_quadrada()
