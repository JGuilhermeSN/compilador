# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from lexico import Lexico

class Sintatico:
    def __init__(self):
        self.token_list = []
        self.lexico = Lexico()
        self.pilhatopo = []


    def lista_token(self):
        tokens = self.lexico.q0()
        self.token_list.extend(tokens)

    def amostra(self):
        print('listagem de tokens')
        for i in self.token_list:
            print(f'{i}')

    def compara(self):

        if self.token_list[0] == self.pilhatopo:
            pass


sintatico = Sintatico()
sintatico.lista_token()
sintatico.amostra()
