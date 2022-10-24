class Professor:
    def __init__(self, nome:str, matricula:int, subarea:str, campus_atual:str, campus_removido:str, tempo_de_ifce:int, idade:int, nota_concurso:float):
        self.nome_professor = nome
        self.matricula = matricula
        self.subarea = subarea
        self.campus_atual = campus_atual
        self.campus_removido = campus_removido
        self.tempo_de_ifce = tempo_de_ifce
        self.idade = idade
        self.nota_concurso = nota_concurso


    def __repr__(self):
        return repr((self.nome_professor, self.tempo_de_ifce))


    def __str__(self):
        return f'Professor: {self.nome_professor} - TEMPO DE IFCE: {self.tempo_de_ifce}'
