#CSV: COMMA SEPARATED VALUES 
# para adicionar dados que contêm caracteres de separação, usamos "", para separar os dados, usa-se , ou ; ou :

import csv


with open("dados.csv", "r") as arquivo:
    dados = csv.reader(arquivo)
    next(dados) # Pula a primeira linha

    for linha in dados:
        print(linha[0], linha[1]) # Imprime o nome e a idade


with open("dados.csv", "r") as arquivo:
    # Carrega os dados do arquivo com o DictReader
    dados = csv.DictReader(arquivo) 

    # Itera sobre os dados, onde cada linha é um dicionário
    for linha in dados:
        # Imprime as chaves "nome" e "idade"
        print(linha['nome'], linha["idade"])

with open("dados.csv", "w") as arquivo:
    # Cria objeto DictWriter
    dados = csv.DictWriter(arquivo, fieldnames=["nome", "idade"], lineterminator='\n')

    # Escreve cabeçalho
    dados.writeheader()
    # Escreve linha
    dados.writerow({
        "nome": "tiago_novo",
        "idade": 100,
    })


