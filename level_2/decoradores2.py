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
