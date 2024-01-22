import os

restaurantes = ["Pizza Hut", "Burger King"]


def exibir_nome_app():
    print(
        """
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮
╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫
┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃
╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
"""
    )


def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")


def finalizar_app():
    os.system("cls")  # no mac e linux 'clear'
    print("Encerrando a aplicação\n")


def opcao_invalida():
    print("OPÇÃO INVÁLIDA \n")
    voltar_menu_principal()


def voltar_menu_principal():
    input("\nDigite uma teclada para retornar ao menu principal ")
    main()

def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)

def cadastrar_restaurante():
    exibir_subtitulo('Cadasto de novos restaurantes')
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_restaurante)
    print(f"Restaurante {nome_restaurante} foi cadastrado com sucesso!")
    voltar_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('Listagem dos restaurantes cadastrados')
    for restaurante in restaurantes:
        print(f"- {restaurante}")
    voltar_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Listar restaurantes")
        elif opcao_escolhida == 4:
            finalizar_app(),
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system("cls")
    exibir_nome_app()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()
