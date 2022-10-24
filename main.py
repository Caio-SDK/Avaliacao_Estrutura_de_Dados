from professor import Professor
from lista_de_prioridades import ListaDePrioridade

lista_prioridade = ListaDePrioridade()

professor_1 = Professor('Gustavo', 12212, 'Técnico', 'Jaguaribe', 'Cedro', 697, 20, 9.0)
professor_2 = Professor('Caio', 12212, 'Técnico', 'Jaguaribe', 'Cedro', 10, 20, 9.0)
professor_3 = Professor('Bruno', 12212, 'Técnico', 'Jaguaribe', 'Cedro', 123, 20, 9.0)
professor_4 = Professor('Arruda', 12212, 'Técnico', 'Jaguaribe', 'Cedro', 1200, 20, 9.0)
professor_5 = Professor('Angeline', 12212, 'Técnico', 'Jaguaribe', 'Cedro', 10, 20, 9.0)
professor_6 = Professor('Alice', 12212, 'Técnico', 'Jaguaribe', 'Cedro', 12, 20, 9.0)
professor_7 = Professor('Nicolas', 12212, 'Técnico', 'Jaguaribe', 'Cedro', 1980, 20, 9.0)
professor_8 = Professor('Robson', 12212, 'Técnico', 'Jaguaribe', 'Cedro', 120, 20, 9.0)

professor_9 = Professor('Herleson', 12212, 'Técnico', 'Jaguaribe', 'Cedro', 122, 20, 9.0)

lista_prioridade.push(professor_1)
lista_prioridade.push(professor_2)
lista_prioridade.push(professor_3)
lista_prioridade.push(professor_4)
lista_prioridade.push(professor_5)
lista_prioridade.push(professor_6)
lista_prioridade.push(professor_7)
lista_prioridade.push(professor_8)
lista_prioridade.push(professor_9)


print(lista_prioridade)
