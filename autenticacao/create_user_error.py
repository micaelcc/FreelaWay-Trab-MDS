class CreateUserError(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Erro ao criar usuario"