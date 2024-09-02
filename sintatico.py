# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from lexico import Lexico

class Sintatico:
    def __init__(self):
        self.token_list = []
        self.lexico = Lexico()


    def lista_token(self):
        print('chegou aqui')
        self.token_list.append(self.lexico.q0())
        #print(self.token_list)

    def amostra(self):
        print('listagem de tokens')
        for i in self.token_list:
            print(i)

sintatico = Sintatico()
sintatico.lista_token()
sintatico.amostra()
