from utils.funcoes_auxiliares import retorna_menu_principal
from utils.menu_cliente import menu_cliente
from utils.menu_analise_carteira import menu_analise_carteira
from utils.menu_ordem import menu_ordem
from utils.menu_relatorio_carteira import menu_relatorio_carteira

def main():
    validador = True
    while(validador):
        print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções abaixo:")
        print("1 - Cliente")
        print("2 - Cadastrar ação")
        print("3 - Realizar análise da carteira")
        print("4 - Imprimir relatório da carteira")
        print("5 - Sair")

        menu = input("Digite a opção desejada: ")

        if menu == "1":
            menu_cliente()

        elif menu == "2":
            menu_ordem()

        elif menu == "3":
            menu_analise_carteira()

        elif menu == "4":
            menu_relatorio_carteira()

        elif menu == "5":
            print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima!")
            validador = False
        else:
            print("Opção inválida. Tente novamente.")

            retorna_menu = retorna_menu_principal()
            if retorna_menu:
                continue
            else:
                validador: False


if __name__ == "__main__":
    main()
