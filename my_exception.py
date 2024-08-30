class EmptyFileException(Exception):
    def __init__(self, message= "O arquivo esta vazio"):
        self.message = message
        super().__init__(self.message)
