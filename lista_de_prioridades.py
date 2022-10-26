# CRIAÇÃO DE UMA CLASSE PARA A LISTA DE PRIORIDADE
class ListaDePrioridade:

    # Declarando o método construtor dessa classe
    def __init__(self):

        self.lista_de_prioridade = []


    # Declarando o método que adicionará o professor a lista
    def push(self, professor):

        self.lista_de_prioridade.append(professor)

        self.lista_de_prioridade = sorted(self.lista_de_prioridade, key=lambda professor: professor.tempo_de_ifce, reverse=True)

    
    # Declarando o método que verifica se a lista de prioridades está vazia ou não
    def empty(self):

        # Se a lista de prioridades for vazia
        if not self.lista_de_prioridade:

            # Retornar True
            return True
        
        # Caso a lista de prioridades não esteja vazia
        else:

            # Retornar False
            return False

    
    # Declarando o método que deleta o professor com mais tempo de IFCE
    def pop(self):

        del self.lista_de_prioridade[0]


    # Declarando o método que recebe como parametro o nome do campus e retorna a quantidade de professores no campus
    def filter_campus(self, campus):

        quantidade_professor = 0

        for professor in self.lista_de_prioridade:

            if professor.campus_atual == campus:

                quantidade_professor += 1
        
        return quantidade_professor


    # Declarando método dunder __str__ para a utilização em um "print"
    def __str__(self):

        tratamento_string_professor = ''

        for index, professor in enumerate(self.lista_de_prioridade):
            tratamento_string_professor += f'{index + 1} - {professor}\n'

        return tratamento_string_professor



