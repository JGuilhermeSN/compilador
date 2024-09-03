# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
class Token:
    def __init__(self, token='', lexema='', linha='', coluna=''):
        self.token = token
        self.lexema = lexema
        self.linha = linha
        self.coluna = coluna
        self.classifyer = None


        self.classifyer = [
            {"lexema": "program", "token":"PROGRAM", "tipo":"palavra_chave"},
            {"lexema": "var",     "token":"VAR",     "tipo":"palavra_chave"},
            {"lexema": "if",      "token":"IF",      "tipo":"palavra_chave"},
            {"lexema": "for",     "token":"FOR",     "tipo":"palavra_chave"},
            {"lexema": "while",   "token":"WHILE",   "tipo":"palavra_chave"},
            {"lexema": "write",   "token":"WRITE",   "tipo":"palavra_chave"},
            {"lexema": "do",      "token":"DO",      "tipo":"palavra_chave"},
            {"lexema": "endif",   "token":"ENDIF",   "tipo":"palavra_chave"},
            {"lexema": "read",    "token":"READ",    "tipo":"palavra_chave"},
            {"lexema": "end",     "token":"END",     "tipo":"palavra_chave"},
            {"lexema": "else",    "token":"ELSE",    "tipo":"palavra_chave"},
            {"lexema": "then",    "token":"THEN",    "tipo":"palavra_chave"},
            {"lexema": "for",     "token":"FOR",    "tipo":"palavra_chave"},
            {"lexema": "<",    "token":"MENOR",    "tipo":"operador_logico"},
            {"lexema": ">",    "token":"MAIOR",    "tipo":"operador_logico"},
            {"lexema": "==",   "token":"IGUAL",   "tipo":"operador_logico"},
            {"lexema": "!=",   "token":"DIFERENTE",   "tipo":"operador_logico"},
            {"lexema": "/",    "token":"DIVISOR",    "tipo":"operador_aritmetico"},
            {"lexema": "*",    "token":"MULTIPLICADOR",    "tipo":"operador_aritmetico"},
            {"lexema": "+",    "token":"ADIÇAO",    "tipo":"operador_aritmetico"},
            {"lexema": "-",    "token":"SUBTRAÇAO",    "tipo":"operador_aritmetico"},
            {"lexema": "{",    "token":"OPEN_BRACE",    "tipo":"abre_chave"},
            {"lexema": "}",    "token":"CLOSE_BRACE",    "tipo":"fecha_chave"},
            {"lexema": "(",    "token":"OPEN_PAR",    "tipo":"abre_parentese"},
            {"lexema": ")",    "token":"CLOSE_PAR",    "tipo":"fecha_parentese"},
            {"lexema": ":",    "token":"ASSIGN",    "tipo":"atribuir"},
            {"lexema": ";",    "token":"SEMICOLON",    "tipo":"ponto_virgula"},
            {"lexema": ",",    "token":"COMMA",    "tipo":"virgula"},
            {"lexema": self.lexema,      "token":"ID",      "tipo":"identificador"},
            {"lexema": self.lexema,      "token":"NUM",      "tipo":"numerador"},
        ]


    def token_list(self):
        lista = []
        if self.lexema.isnumeric():
            print(f'{self.lexema} / NUM / numerador / Ln:{self.linha} / Col:{self.coluna}') # visualizaçao
            lista.append(f'{self.lexema} / NUM / numerador / Ln:{self.linha} / Col:{self.coluna}') # envio para o sintatico
        else:
            for item in self.classifyer:
                # Verifica se o token ou lexema coincide
                if item["token"] == self.token or item["lexema"] == self.lexema:
                    print(f'{item["lexema"]} / {item["token"]} / {item["tipo"]} / Ln:{self.linha} / Col:{self.coluna}') # visualizaçao do que esta sendo enviado para a lista sintatica
                    lista.append(f'{item["lexema"]} / {item["token"]} / {item["tipo"]} / Ln:{self.linha} / Col:{self.coluna}')
                    break
        return lista
