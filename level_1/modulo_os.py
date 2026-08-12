#Os
#serve para interagir com o sistema operacional
import os
caminho_pasta_atual=os.getcwd()
print(caminho_pasta_atual)
#vamos mudar o diretorio que o pyhton usa no codigo:
os.chdir(r"C:\Users\T-GAMER\OneDrive\Documents") #o r serve para ler como uma raw string, ou seja, o pyhton vai ignorar \n ou semelhantes, nao executnado comandos
print(os.getcwd())
#para saber os arquivos contidos em um diretório:
print(os.listdir()) #o parametro é o diretório #caso não seja listado um parametro, usa-se o do diretorio atual
print(os.listdir(r"C:\Users\T-GAMER\Pictures"))
#lembrnado  que nosso diretório atual é Documents, podemos criar uma pasta nesse diretório, ou em outro tb:
os.mkdir("pasta_nova") #n se especificou o caminho, usa-se o diretorio atual
print(os.listdir())
os.mkdir(r"C:\Users\T-GAMER\OneDrive\Documents\NovaPasta") #aqui se especificou o caminho, que por sinal, é o mesmo
print(os.listdir())
#se já houver uma pasta com mesmo nome, o terminal retorna um erro
#usando os para executar comandos do proprio sistema operacional:
os.system("cls") # Executa o comando "clear", que limpa o terminal
print("Após limpar o terminal")
#para não haver conflito se rodar esse codifos em sistemas diferentes, pode-se usar o os.path
caminho = os.path.join("pasta", "subpasta", "teste.txt")
print(caminho)