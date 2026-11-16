
estoque = {}
alto_contraste = False


def formatar_texto(texto):
    if alto_contraste:
        return f"\033[97;40;1m{texto}\033[0m"
    return texto


def cadastrar_produto(nome, quantidade, preco):
    if not nome.strip():
        return False

    if nome in estoque or quantidade < 0 or preco < 0:
        return False

    estoque[nome] = {
        "quantidade": quantidade,
        "preco": preco
    }
    return True


def consultar_estoque():
    return estoque


def registrar_entrada(nome, quantidade):
    if nome not in estoque or quantidade <= 0:
        return False

    estoque[nome]["quantidade"] += quantidade
    return True


def registrar_saida(nome, quantidade):
    if nome not in estoque or quantidade <= 0:
        return False

    if quantidade > estoque[nome]["quantidade"]:
        return False

    estoque[nome]["quantidade"] -= quantidade
    return True


def menu():
    global alto_contraste

    while True:
        print(formatar_texto("\n===== SISTEMA DE CONTROLE DE ESTOQUE ====="))
        print(formatar_texto("1 - Cadastrar produto"))
        print(formatar_texto("2 - Consultar estoque"))
        print(formatar_texto("3 - Registrar entrada"))
        print(formatar_texto("4 - Registrar saída"))
        print(formatar_texto("5 - Sair"))
        print(formatar_texto("6 - Ativar/desativar alto contraste"))

        opcao = input(formatar_texto("Escolha uma opção: "))

        if opcao == "1":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: R$ "))

            if cadastrar_produto(nome, quantidade, preco):
                print(formatar_texto("Produto cadastrado com sucesso!"))
            else:
                print(formatar_texto("Não foi possível cadastrar o produto."))

        elif opcao == "2":
            for nome, dados in consultar_estoque().items():
                print(formatar_texto(f"{nome}: {dados}"))

        elif opcao == "3":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade de entrada: "))

            if registrar_entrada(nome, quantidade):
                print(formatar_texto("Entrada registrada!"))
            else:
                print(formatar_texto("Não foi possível registrar a entrada."))

        elif opcao == "4":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade de saída: "))

            if registrar_saida(nome, quantidade):
                print(formatar_texto("Saída registrada!"))
            else:
                print(formatar_texto("Não foi possível registrar a saída."))

        elif opcao == "5":
            print(formatar_texto("Sistema encerrado!"))
            break

        elif opcao == "6":
            alto_contraste = not alto_contraste

            if alto_contraste:
                print(formatar_texto("Modo de alto contraste ativado!"))
            else:
                print("Modo de alto contraste desativado!")

        else:
            print(formatar_texto("Opção inválida!"))


if __name__ == "__main__":
    menu()
