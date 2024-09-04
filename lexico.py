# pylint: disable=line-too-long
"""
Modulo do analisador lexico do compilador
by: José Guilherme
"""
#pylint: disable=missing-function-docstring
import utils_lexico
from my_exception import EmptyFileException

class Lexico:
    """classe do analisador lexico"""

    def __init__(self, source_file=None):
        """metodo construtor"""
        self.source_file = source_file
        self.i = 0
        self.token = " "
        self.pointer = self.open_file()
        self.lista_tk = []
        self.line = 1
        self.column = 1
        self.counter = 0


    def open_file(self):
        try:
            file = input('arquivo fonte?: ')
            print('='*30)
            self.source_file = open(file,"r", encoding='utf-8').read().lower().replace("\xa0","").replace("    ","\t")
            if not self.source_file:
                raise EmptyFileException()
            return self.source_file[self.i]
        except FileNotFoundError:
            print("O arquivo nao foi encontrado")


    def next(self): # contagem de linhas e colunas
        if self.pointer == ' ':
            self.column += 1
            self.i += 1
            self.counter += 1
        elif self.pointer == '\n':
            self.line += 1
            self.i += 1
            self.column = 1
            self.counter += 1
        elif self.pointer == '\t':
            self.column += 4
            self.i += 1
            self.counter += 1
        else:
            self.column +=1
            self.i += 1
            self.counter += 1

    def insert_token(self,token=None, lexema=None):
        if self.pointer != '\n' or token != 'ID':
            token = utils_lexico.Token(token, lexema, self.line, self.column-self.counter)
            lista = token.token_list()
            self.lista_tk.append(lista)
        self.q0()


    def q0(self):
        if len(self.source_file) == self.i:
            return self.lista_tk
        elif self.pointer == '\n' or self.pointer.isspace():
            self.next()
        self.pointer = self.source_file[self.i]
        self.token = ""
        self.counter = 0
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
            case 'f':
                self.token += self.pointer
                self.next()
                self.q37()
            case '=':
                self.token += self.pointer
                self.next()
                self.q40()
            case '!':
                self.token += self.pointer
                self.next()
                self.q40()
            case '<' | '>' | '/' | '*' | '+' | '-' | '{' | '}' | '(' | ')' | ':' | ';' | ',':
                self.symbol_verifyer()
            case _: # Default
                if self.pointer.isalnum() or self.pointer == '\n':# verificaçao de variavel
                    self.id_verifyer()
                elif self.pointer.isspace():
                    self.next()
                    self.pointer = self.source_file[self.i]
                    self.q0()
                else:
                    self.non_identifyed() # tratamento de caracteres nao identificados
        return self.lista_tk


    def q1(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'r':
            self.token += self.pointer
            self.next()
            self.q2()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q2(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'o':
            self.token += self.pointer
            self.next()
            self.q3()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q3(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'g':
            self.token += self.pointer
            self.next()
            self.q4()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q4(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'r':
            self.token += self.pointer
            self.next()
            self.q5()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q5(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'a':
            self.token += self.pointer
            self.next()
            self.q6()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q6(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'm':
            self.token += self.pointer
            self.next()
            self.q7()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q7(self):
        """reconhece o token 'program' """
        if not len(self.source_file) == self.i:
            self.pointer = self.source_file[self.i]
            if not self.pointer.isalnum() or self.pointer == '\n':
                self.insert_token(token=self.token.upper(), lexema=self.token)
            else:
                self.token += self.pointer
                self.next()
                self.id_verifyer()
        else:
            self.insert_token(token=self.token.upper(), lexema=self.token)

    def q8(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'f':
            self.token += self.pointer
            self.next()
            self.q9()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q9(self):
        """reconhece o token 'if' """
        if not len(self.source_file) == self.i:
            self.pointer = self.source_file[self.i]
            if not self.pointer.isalnum() or self.pointer == '\n':
                self.insert_token(token=self.token.upper(), lexema=self.token)
            else:
                self.token += self.pointer
                self.next()
                self.id_verifyer()
        else:
            self.insert_token(token=self.token.upper(), lexema=self.token)

    def q10(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'h':
            self.token += self.pointer
            self.next()
            self.q11()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q11(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'e':
            self.token += self.pointer
            self.next()
            self.q12()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q12(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'n':
            self.token += self.pointer
            self.next()
            self.q13()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q13(self):
        """reconhece o token 'then' """
        if not len(self.source_file) == self.i:
            self.pointer = self.source_file[self.i]
            if not self.pointer.isalnum() or self.pointer == '\n':
                self.insert_token(token=self.token.upper(), lexema=self.token)
            else:
                self.token += self.pointer
                self.next()
                self.id_verifyer()
        else:
            self.insert_token(token=self.token.upper(), lexema=self.token)


    def q14(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'o':
            self.token += self.pointer
            self.next()
            self.q15()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q15(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == '\n' or self.pointer == ' ':
            self.next()
            self.insert_token(token=self.token.upper(), lexema=self.token)
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q16(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'e':
            self.token += self.pointer
            self.next()
            self.q17()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q17(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'a':
            self.token += self.pointer
            self.next()
            self.q18()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q18(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'd':
            self.token += self.pointer
            self.next()
            self.q19()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q19(self):
        """reconhece o token 'read' """
        if not len(self.source_file) == self.i:
            self.pointer = self.source_file[self.i]
            if not self.pointer.isalnum() or self.pointer == '\n':
                self.insert_token(token=self.token.upper(), lexema=self.token)
            else:
                self.token += self.pointer
                self.next()
                self.id_verifyer()
        else:
            self.insert_token(token=self.token.upper(), lexema=self.token)

    def q20(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'a':
            self.token += self.pointer
            self.next()
            self.q21()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q21(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'r':
            self.token += self.pointer
            self.next()
            self.q22()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q22(self):
        """reconhece o token 'var' """
        if not len(self.source_file) == self.i:
            self.pointer = self.source_file[self.i]
            if not self.pointer.isalnum() or self.pointer == '\n':
                self.insert_token(token=self.token.upper(), lexema=self.token)
            else:
                self.token += self.pointer
                self.next()
                self.id_verifyer()
        else:
            self.insert_token(token=self.token.upper(), lexema=self.token)

    def q23(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'n':
            self.token += self.pointer
            self.next()
            self.q24()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q24(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'd':
            self.token += self.pointer
            self.next()
            self.q25()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q25(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'i':
            self.token += self.pointer
            self.next()
            self.q26()
        elif self.pointer == '\n' or self.pointer == ' ':
            self.next()
            self.insert_token(token=self.token.upper(), lexema=self.token)

    def q26(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'f':
            self.token += self.pointer
            self.next()
            self.q27()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q27(self):
        """reconhece o token 'endif' """
        if not len(self.source_file) == self.i:
            self.pointer = self.source_file[self.i]
            if not self.pointer.isalnum() or self.pointer == '\n':
                self.insert_token(token=self.token.upper(), lexema=self.token)
            else:
                self.token += self.pointer
                self.next()
                self.id_verifyer()
        else:
            self.insert_token(token=self.token.upper(), lexema=self.token)

    def q28(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'h':
            self.token += self.pointer
            self.next()
            self.q29()
        elif self.pointer == 'r':
            self.token += self.pointer
            self.next()
            self.q33()


    def q29(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'i':
            self.token += self.pointer
            self.next()
            self.q30()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q30(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'l':
            self.token += self.pointer
            self.next()
            self.q31()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q31(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'e':
            self.token += self.pointer
            self.next()
            self.q32()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q32(self):
        """reconhece o token 'while' """
        if not len(self.source_file) == self.i:
            self.pointer = self.source_file[self.i]
            if not self.pointer.isalnum() or self.pointer == '\n':
                self.insert_token(token=self.token.upper(), lexema=self.token)
            else:
                self.token += self.pointer
                self.next()
                self.id_verifyer()
        else:
            self.insert_token(token=self.token.upper(), lexema=self.token)


    def q33(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'i':
            self.token += self.pointer
            self.next()
            self.q34()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q34(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 't':
            self.token += self.pointer
            self.next()
            self.q35()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q35(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'e':
            self.token += self.pointer
            self.next()
            self.q36()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q36(self):
        """reconhece o token 'write' """
        if not len(self.source_file) == self.i:
            self.pointer = self.source_file[self.i]
            if not self.pointer.isalnum() or self.pointer == '\n':
                self.insert_token(token=self.token.upper(), lexema=self.token)
            else:
                self.token += self.pointer
                self.next()
                self.id_verifyer()
        else:
            self.insert_token(token=self.token.upper(), lexema=self.token)

    def q37(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'o':
            self.token += self.pointer
            self.next()
            self.q38()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q38(self):
        self.pointer = self.source_file[self.i]
        if self.pointer == 'r':
            self.token += self.pointer
            self.next()
            self.q39()
        else:
            self.token += self.pointer
            self.next()
            self.id_verifyer()

    def q39(self):
        """reconhece o token 'for' """
        self.pointer = self.source_file[self.i]
        if not len(self.source_file) == self.i:
            self.pointer = self.source_file[self.i]
            if not self.pointer.isalnum() or self.pointer == '\n':
                self.insert_token(token=self.token.upper(), lexema=self.token)
            else:
                self.token += self.pointer
                self.next()
                self.id_verifyer()
        else:
            self.insert_token(token=self.token.upper(), lexema=self.token)

    def q40(self):
        """reconhece o token '==' e '!=' """
        self.pointer = self.source_file[self.i]
        if self.pointer == '=':
            self.token += self.pointer
            self.next()
            self.insert_token(token=self.token.upper(), lexema=self.token)
        elif not self.pointer == '=':
            print(f'Erro: token == ou !=, ln {(self.line)}, col {(self.column-self.counter)}')
            #self.q0() # nesta chamada o codigo continuara normalmente apos o aviso
            return 1
        else:
            print('erro simbolos == ou !=')
            self.q0()



    def id_verifyer(self):
        """funçao para reconhecer id """
        if not len(self.source_file) == self.i:
            self.pointer = self.source_file[self.i]
            if self.pointer.isalnum() or self.pointer == '_':
                self.token += self.pointer
                self.next()
                self.id_verifyer()
            elif not self.pointer.isspace or self.pointer == '\n' or not self.pointer.isalnum():
                self.insert_token(token='ID', lexema=self.token)
            else:
                self.q0()
        else:
            self.insert_token(token='ID', lexema=self.token)

    def symbol_verifyer(self):
        """funçao para reconhecer simbolos"""
        if not len(self.source_file) == self.i:
            self.pointer = self.source_file[self.i]
            if not self.pointer == '\n' and not self.pointer.isalnum():
                self.token += self.pointer
                self.next()
                self.insert_token(token=self.token.upper(), lexema=self.token)
            else:
                self.q0()
        else:
            self.insert_token(token='ID', lexema=self.token)

    def non_identifyed(self):
        print(f'Erro: "{self.pointer}" caracter nao identificado, ln {self.line} col {self.column-self.counter}')
        return 1


# usar para testar somente o analisador lexico
lexico = Lexico()
lexico.q0()
