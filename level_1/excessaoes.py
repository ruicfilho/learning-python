try:
    numero=int(input()) 
    print(f"Seu número é {numero}")
except ValueError:
    print("Valor atribuído deve ser um número")
except:
    print('Uma variável diferente de ValueError foi gerada')

#modo abstrato usando a classe Exception
try:
    int(input())
except Exception as error:
    print(error)
    print(type(error))

#utilizando else para evitar captura de excessoes acidentais
#nesse caso, o else ocorre se não houver nenhuma excessao
try:
    numero2=int(input())
except Exception as error:
    print(error)
    print(type(error))
else:
    print(numero2)
finally:
    print("finally é sempre executado")

#comando pass
while True:
    try:
        numero3=int(input())
        break #break não é lido pq ao digitar algo diferente de um numero, é gerado uam excessao
    except ValueError:
        pass

#gerando uma excessao:
numero4=int(input())
if numero4<=0:
    raise ValueError("Numero deve ser maior que zero")
