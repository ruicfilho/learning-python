#funcao decoradora é uma funcao que recebe outra como parametro e estende seu comportamento sem modificá-la
def decorador(func): #cria uma função que recebe um função como argumento
    def wrapper():
        print("Esse print está sendo excutado antes da função")
        func()
        print("Esse print está sendo executado depois da função")
    return wrapper
def hello():
    print("Hello World")
hello_decorada= decorador(hello)
hello_decorada()

#o python tem uma forma de fazer isso:
@decorador
def hello1():
    print("Hello World1")
hello1()

#devemos ter atenção quando uma funcao retorna algo
print("----------------------------------------------")
def decorador(func):
    def wrapper():
        print("Esse print está sendo executado antes da função")
        retorno=func() #cria uma variável que armazena o retorno da função
        print("Esse print está sendo executado depois da função")
        return retorno
    return wrapper

@decorador
def hello():
    return ("Hello World!")
print(hello())

#função que retorna argumentos
print("-----------------------------------------------")
def decorador(func):
    def wrapper(nome): #wrapper recebe os mesmos argumentos de func
        print(f"Seu nome é {nome}")
        return func(nome) #executa a função decorada
    return wrapper

@decorador
def hello(nome):
    return f"Hello {nome}!"
print(hello("TIago"))

print("----------------------------")
#note que as vezes nao sabemos a quantia de argumentos, nesse cenário usamos args
def teste(*args): #args é só uma convenção, * é um empacotador, empacota tudo em uma tupla
    print(args) #se botassemos * ele iria desempacotar aqui
teste(1,2,3)
teste(3,4,5)

#usamos args pois foram argumentos não nomeados, mas, para argumentos noemados, devemos usar **kwargs
def teste(**kwargs): #o operador empacota na variável kwargs, os argumentos em dicionário
    print(kwargs)
teste(arg1="oi", arg2="Rui")

#agora, podemos aplicar um decorador independentemente dos tipos de argumentos!
def decorador(func):
    def wrapper(*args2, **kwargs2): #empacota os argumentos posiconais e nomeados
        print(f"Argumentos posicionais: {args2}")
        print(f"Argumentos nomeados: {kwargs2}")
        return func(*args2, **kwargs2)
    return wrapper
@decorador
def teste(arg1, agr2, arg3):
    pass
teste("valor1", "valor2", arg3="valor3")



