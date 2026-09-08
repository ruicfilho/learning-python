class Projeto:
    def __init__(self, requisito_programacao, requisito_design):
        self.requisito_programacao = requisito_programacao
        self.requisito_design = requisito_design


class Empregado:
    def __init__(self, valor_por_projeto, valor_recebido):
        self.__valor_por_projeto = valor_por_projeto
        self.__valor_recebido = valor_recebido

    @property
    def valor_recebido(self):
        return self.__valor_recebido

    # Um empregado normal não é capaz de entregar nenhum projeto :(
    def capaz(self, projeto: Projeto) -> bool:
        return False

    def receber_recompensa(self) -> None:
        self.__valor_recebido += self.__valor_por_projeto



class Programador(Empregado):
    # TODO: Complete o código do construtor inicializando os valores corretamente.
    def __init__(self, valor_por_projeto: int, habilidade_programacao: int):
        super().__init__(valor_por_projeto, 0)
        self.__habilidade_programacao = habilidade_programacao
    


    # TODO: Um programador deve ser capaz de entregar um projeto se sua habilidade de programação é maior que o requisito de programação do projeto.
    def capaz(self, projeto: Projeto) -> bool:
        return self.__habilidade_programacao >= projeto.requisito_programacao
    
            


class Designer(Empregado):
    # porque eu nao uso valor_recebido como parametro, mas inicializo ele com super?
    #Porque são duas coisas diferentes:
    #valor_recebido é um estado interno que precisa ser inicializado;
    #não é uma informação que o usuário precisa fornecer para criar um Programador ou Designer.
    #se adicionassemos como parametro, seria necessário definir o parametro quando se criasse o objeto



    # TODO: Complete o código do construtor inicializando os valores corretamente.
    def __init__(self, valor_por_projeto: int, habilidade_design: int):
        super().__init__(valor_por_projeto, 0)
        self.__habilidade_desing = habilidade_design
        

    # TODO: Um designer deve ser capaz de entregar um projeto se sua habilidade de design é maior que o requisito de design do projeto.
    def capaz(self, projeto: Projeto) -> bool:
        return self.__habilidade_desing >= projeto.requisito_design

    


if __name__ == "__main__":

    valor, habilidade = map(int, input().split())
    programador = Programador(valor, habilidade)

    valor, habilidade = map(int, input().split())
    designer = Designer(valor, habilidade)

    N = int(input())
    for _ in range(N):
        requisito_programacao, requisito_design = map(int, input().split())
        projeto = Projeto(requisito_programacao, requisito_design)
        if programador.capaz(projeto) == True and designer.capaz(projeto) == True:
            programador.receber_recompensa()
            designer.receber_recompensa()

        # TODO: Use os métodos das classes acima para calcular quando tanto o programador quanto o designer conseguem desenvolver o projeto P e dê a recompensa a cada um caso eles consigam.

    print(f"Programador: R$ {programador.valor_recebido}")
    print(f"Designer: R$ {designer.valor_recebido}")
