"""Modulo principal do compilador"""
from lexico import Lexico

class Main:
    """Classe main do Compilador"""
    def __init__(self):
        print('Compilador - JGN')



    def analisadores(self):
        """Funçao de chamada do analisador lexico"""
        analyser = input('1- lexico \n2- sintatico \n3- semantico')
        match analyser:
            case '1':
                lexico = Lexico()
                lexico.q0()
            case '2':
                print('sintatico')
            case '3':
                print('semantico')

main = Main()
main.analisadores()
