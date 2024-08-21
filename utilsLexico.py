# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
class Token:
    def __init__(self, token, lexema=None, position=None):
        self.token = token
        self.lexema = lexema
        self.position = position



    def token_list(self):
        print(f'| {self.lexema} | {self.token} | ')
