class Professor:

    def __init__(self, nome, matricula, subarea, campus_atual, campus_removido, tempo_de_ifce, idade, nota_concurso):
        self.nome = nome
        self.matricula = matricula
        self.subarea = subarea
        self.campus_atual = campus_atual
        self.campus_removido = campus_removido
        self.tempo_de_ifce = tempo_de_ifce
        self.idade = idade
        self.nota_concurso = nota_concurso

    
    def __str__(self):
        return f"{self.nome}"


    @staticmethod
    def cadastro():
        

        return Professor("Caio", 3232, "Desenvolvedor", "J", "H", 32, 20, 7.5)





class ListaDePrioridade:

    def __init__(self):

        self.lista_prioridade = []

    
    def push(self, professor):

        self.lista_prioridade.append(professor)

    
    def __str__(self):
        string_lista_prioridade = ""
        for professor in self.lista_prioridade:
            string_lista_prioridade += str(professor) + "\n"

        return string_lista_prioridade



prioridade = ListaDePrioridade()