import click #eu baixei na biblioteca virtual xenv
#click é uma biblioteca que te permite trablhar como um CLI
#CLI=Commnad-Line Interface, ou Interface de Linha de Comando
#CLI é um programa que o usuario controla usando o terminal ao inves de botoes ou menus

@click.command() #esse decorador informa ao click que a função abaixo será um comando executável pela linha de comando, um decorador faz: funcao=decoracao(funcao)
@click.argument("nome", required=True) #esse prorgram receb um argumento, obrigatorio(required=True), chamado nome
@click.option( #cria uma opcao ao executar um comando no terminal. Podeiramos fazer: python programa.py Rui --num_vezes 10
    "--num_vezes",
    type=int,
    default=1, #caso não se use a option, default=1
    help="Número de vezes que a mensagem será impressa",
)
def hello(nome, num_vezes):
    for _ in range(num_vezes):
        click.echo(f"Hello {nome}!")


if __name__ == "__main__": #fazemos isso para que a funcao hello nao seja executada
    hello()
#um decorador funciona assim, nesse exemplo:
# Quando o interpretador encontra:
# def hello():
#ele faz algo equivalente a:
# def hello():
    # ...
# hello = click.command()(hello)