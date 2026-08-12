#Sys
#serve para ler o argumento mandado ao executar python nome_do_arquivo.py
import sys
print(sys.argv) #FAÇA NO TERMINAL python modulos_embutidos.py argumento1
# caso queiramos que o usuario necessariamente mande o argumento(ou os argumentos):
if len(sys.argv) != 2: # Caso o tamanho da lista seja diferente de 2, ou seja, optopu-se por 1 argumento
    sys.exit("O programa deve ser executado como: python nome_arquivo argumento")#o exit encerra o programa
print(sys.argv[1])


