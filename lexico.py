"""
Modulo do analisador lexico do compilador
by: José Guilherme
"""
#pylint: disable=missing-function-docstring

import utilsLexico

class Lexico:
    """classe do analisador lexico"""

    def __init__(self, source_file=None):
        """metodo construtor"""
        self.source_file = source_file
        self.i = 0
        self.token = " "
        self.counter = 1
        self.pointer = self.open_file()


    def open_file(self):
        """funçao de abertura do arquivo"""
        file = input('arquivo fonte?: ')
        self.source_file = open(file,"r", encoding='utf-8').read().lower()
        return self.source_file[self.i]

    def next(self):
        self.i += 1
        self.counter +=1


    def insert_token(self,token=None, lexema=None):
        token = utilsLexico.Token(token, lexema)
        token.token_list()
        self.q0()

    def q0(self):
        self.pointer = self.source_file[self.i]
        self.token = ""
        self.counter = 1
        match self.pointer:
            case 'p':
                self.token += self.pointer
                self.next()
                self.q1()
            case 'i':
                self.token += self.pointer
                self.next()
                self.q8()
            case 't':
                self.token += self.pointer
                self.next()
                self.q10()
            case 'd':
                self.token += self.pointer
                self.next()
                self.q14()
            case 'r':
                self.token += self.pointer
                self.next()
                self.q16()
            case 'v':
                self.token += self.pointer
                self.next()
                self.q20()
            case 'e':
                self.token += self.pointer
                self.next()
                self.q23()
            case 'w':
                self.token += self.pointer
                self.next()
                self.q28()
            case _: # metodo defaut do match case
                pass

    def q1(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'r':
            self.token += self.pointer
            self.next()
            self.q2()
        else:
            print('errado')

    def q2(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'o':
            self.token += self.pointer
            self.next()
            self.q3()
        else:
            print('errado')

    def q3(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'g':
            self.token += self.pointer
            self.next()
            self.q4()
        else:
            print('errado')

    def q4(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'r':
            self.token += self.pointer
            self.next()
            self.q5()
        else:
            print('errado')

    def q5(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'a':
            self.token += self.pointer
            self.next()
            self.q6()
        else:
            print('errado')

    def q6(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'm':
            self.token += self.pointer
            self.next()
            self.q7()
        else:
            print('errado')

    def q7(self):
        """reconhece o token 'program' """
        self.pointer = self.source_file[self.i]
        if self.pointer == '\n':
            print(self.counter - 1)
            self.next()
            self.insert_token(self.token.upper(), self.token)
        else:
            print('errado')

    def q8(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'f':
            self.token += self.pointer
            self.next()
            self.q9()
        else:
            print('errado')

    def q9(self):
        """reconhece o token 'if' """
        self.pointer = self.source_file[self.i]
        if self.pointer == '\n':
            print(self.counter - 1)
            self.next()
            self.insert_token(self.token.upper(), self.token)
        else:
            print('erro')

    def q10(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'h':
            self.token += self.pointer
            self.next()
            self.q11()
        else:
            print('errado')

    def q11(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'e':
            self.token += self.pointer
            self.next()
            self.q12()
        else:
            print('erro')

    def q12(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'n':
            self.token += self.pointer
            self.next()
            self.q13()
        else:
            print('erro')

    def q13(self):
        """reconhece o token 'then' """
        self.pointer = self.source_file[self.i]
        if self.pointer == '\n':
            print(self.counter - 1)
            self.next()
            self.insert_token(self.token.upper(), self.token)

    def q14(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'o':
            self.token += self.pointer
            self.next()
            self.q15()
        else:
            print('erro')

    def q15(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == '\n':
            print(self.counter - 1)
            self.next()
            self.insert_token(self.token.upper(), self.token)
        else:
            print('erro')

    def q16(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'e':
            self.token += self.pointer
            self.next()
            self.q17()
        else:
            print('erro')

    def q17(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'a':
            self.token += self.pointer
            self.next()
            self.q18()
        else:
            print('erro')

    def q18(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'd':
            self.token += self.pointer
            self.next()
            self.q19()
        else:
            print('erro')

    def q19(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == '\n':
            print(self.counter - 1)
            self.next()
            self.insert_token(self.token.upper(), self.token)

    def q20(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'a':
            self.token += self.pointer
            self.next()
            self.q21()
        else:
            print('erro')

    def q21(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'r':
            self.token += self.pointer
            self.next()
            self.q22()
        else:
            print('erro')

    def q22(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == '\n':
            print(self.counter - 1)
            self.next()
            self.insert_token(self.token.upper(), self.token)
        else:
            print('erro')

    def q23(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'n':
            self.token += self.pointer
            self.next()
            self.q24()
        else:
            print('erro')

    def q24(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'd':
            self.token += self.pointer
            self.next()
            self.q25()
        else:
            print('erro')

    def q25(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'i':
            self.token += self.pointer
            self.next()
            self.q26()
        elif self.pointer == '\n' or self.pointer == ' ':
            print(self.counter - 1)
            self.next()
            self.insert_token(self.token.upper(), self.token)

    def q26(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'f':
            self.token += self.pointer
            self.next()
            self.q27()
        else:
            print('erro')

    def q27(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == '\n':
            print(self.counter - 1)
            self.next()
            self.insert_token(self.token.upper(), self.token)
        else:
            print('erro')

    def q28(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'h':
            self.token += self.pointer
            self.next()
            self.q29()
        elif self.pointer == 'r':
            self.q33()


    def q29(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'i':
            self.token += self.pointer
            self.next()
            self.q30()
        else:
            print('erro')

    def q30(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'l':
            self.token += self.pointer
            self.next()
            self.q31()
        else:
            print('erro')

    def q31(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'e':
            self.token += self.pointer
            self.next()
            self.q32()
        else:
            print('erro')

    def q32(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == '\n':
            print(self.counter - 1)
            self.next()
            self.insert_token(self.token.upper(), self.token)
        else:
            print('erro')

    def q33(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'i':
            self.token += self.pointer
            self.next()
            self.q34()
        else:
            print('erro')

    def q34(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 't':
            self.token += self.pointer
            self.next()
            self.q35()
        else:
            print('erro')

    def q35(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'e':
            self.token += self.pointer
            self.next()
            self.q36()
        else:
            print('erro')

    def q36(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == '\n' or self.pointer == ' ':
            print(self.counter - 1)
            self.next()
            self.insert_token(self.token.upper(), self.token)
        print('erro')


lexico = Lexico()
lexico.q0()
