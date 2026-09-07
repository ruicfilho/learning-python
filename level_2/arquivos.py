#modos de abertura: r, w, a 
# r lê o arquivo, w escreve no arquivo, a anexa ao arquivo (append)
#caso o arquivo nao exista, usar read gera eero no terminal
#read sempre sobrescreve as informacoes
#caso nao se especifique o modo de abertura, será aplicado read, por padrao
arquivo = open("teste.txt", "a")
arquivo.write("\nola mundo!4")


#para escrever várias linhas por vez, podemos usar o método writelines, ele recebe como paramêtro uma lista
lista = [
    "Primeira linha\n",
    "Segunda linha\n"
] # Lista de strings

arquivo = open("teste.txt", "w") # Abre o arquivo no modo de escrita
arquivo.writelines(lista) # Escreve as strings da lista no arquivo


#sempre que abrirmos um arquivo, devemos fechá-lo:
arquivo.close()

#fazer sempre isso não é prático. Logo, usa-se o comando with, que sempre fecha o arquivo no seu fim:
with open("teste.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha)
    #para printar sem quebra de linhas: print(linha, end='') ou linha.rstrip() (remove caracteres no final da str)

#para ler linhas(após ler uma, será lida a próxima)
with open("teste.txt", "r") as arquivo:
    print(arquivo.readline(), end="") # Imprime primeira linha
    print(arquivo.readline(), end="") # Imprime segunda linha
    print(arquivo.readline(), end="") # Imprime terceira linha

#usando readlines:
with open("teste.txt", "r") as arquivo:
    # Armazena as linhas na lista "linhas"
    linhas = arquivo.readlines() 

for linha in linhas: # Para cada linha da lista
    print(linha, end="") # Imprima a linha


#Existe ainda modos de "atualização" que permite leitura e escrita ao mesmo tempo. Ao adicionar o símbolo + ao modo ativamos o modo de atualização. Por exemplo: "r+", "w+" e "a+".
