from validacao import Validacao
from professor import Professor
from lista_de_prioridades import ListaDePrioridade

import sys

lista_prioridade = ListaDePrioridade()

class Menu:

    @staticmethod
    def MenuInterativo():

        while True:

            print("""
[ 1 ] - Cadastrar novo professor
[ 2 ] - Exibir todos os professores
[ 3 ] - Remover professor da lista
[ 4 ] - Verificar quantidade de professores no campus
[ 5 ] - Sair do sistema
""")
            opcao_desejada = Validacao.ValidacaoOpcoes("Digite o número da opção desejada: ", 1, 5)

            if (opcao_desejada == 1):

                professor = Menu.CadastroProfessor()

                lista_prioridade.push(professor)

            elif (opcao_desejada == 2):

                print("\nPROFESSORES")
                print(lista_prioridade)
            
            elif (opcao_desejada == 3):

                if not (lista_prioridade.empty()):
                    
                    lista_prioridade.pop()
                    print("Professor removido!")
                
                else:

                    print("Não existe nenhum professor na lista de prioridades\nTeste novamamente mais tarde...")
            
            elif (opcao_desejada == 4):

                Menu.DashboardCampus()
        
            elif (opcao_desejada == 5):

                sys.exit()


    @staticmethod
    def CadastroProfessor():

        nome_professor = Validacao.ValidacaoNome("Digite o nome do professor: ").title()
        matricula_professor = Validacao.ValidacaoNumeroInteiro("Digite a matricula do professor: ")
        sub_area_professor = Validacao.ValidacaoNome("Digite o sub área do professor: ").capitalize()
        campus_atual_professor = Validacao.ValidacaoNome("Digite o campus atual do professor: ").capitalize()
        campus_removido_professor = Validacao.ValidacaoNome("Digite o campus de remoção do professor: ").capitalize()
        tempo_ifce_professor = Validacao.ValidacaoNumeroInteiro("Digite a o tempo (EM DIAS) de IFCE do professor: ")
        idade_professor = Validacao.ValidacaoNumeroInteiro("Digite a idade do professor: ")
        nota_concurso_professor = Validacao.ValidacaoNumeroDecimal("Digite a nota do concurso do professor: ", 2, True)

        registro = Professor(nome_professor, matricula_professor, sub_area_professor, campus_atual_professor, campus_removido_professor, tempo_ifce_professor, idade_professor, nota_concurso_professor)

        return registro

    
    @staticmethod
    def DashboardCampus():

        campus = Validacao.ValidacaoNome("Digite o nome do campus que deseja pesquisar: ").capitalize()

        print(f'\nExiste um total de: {lista_prioridade.filter_campus(campus)} professores no campus de {campus}')
