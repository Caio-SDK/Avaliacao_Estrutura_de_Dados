# CRIAÇÃO DE UMA CLASSE PARA A LISTA DE PRIORIDADES
class ListaDePrioridade:

    # Declarando o método construtor dessa classe
    def __init__(self):
        self.lista_de_prioridade = []

    def push(self, professor):
        self.lista_de_prioridade.append(professor)

    def __str__(self):
        lista_reverse = sorted(self.lista_de_prioridade, key=lambda professor: professor.tempo_de_ifce, reverse=True)
        professores = ''

        for index, professor in enumerate(lista_reverse):
            professores += f'{index + 1} - {professor}\n'

        return professores



