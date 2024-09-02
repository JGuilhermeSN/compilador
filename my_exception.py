class EmptyFileException(Exception):
    def __init__(self, message= "Erro: O arquivo esta vazio"):
        self.message = message
        super().__init__(self.message)
