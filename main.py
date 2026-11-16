
estoque = {}


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
    while True:
        print("\n===== SISTEMA DE CONTROLE DE ESTOQUE =====")
        print("1 - Cadastrar produto")
        print("2 - Consultar estoque")
        print("3 - Registrar entrada")
        print("4 - Registrar saída")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: R$ "))
            if cadastrar_produto(nome, quantidade, preco):
                print("Produto cadastrado com sucesso!")
            else:
                print("Não foi possível cadastrar o produto.")

        elif opcao == "2":
            for nome, dados in consultar_estoque().items():
                print(nome, dados)

        elif opcao == "3":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade de entrada: "))
            if registrar_entrada(nome, quantidade):
                print("Entrada registrada!")
            else:
                print("Não foi possível registrar a entrada.")

        elif opcao == "4":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade de saída: "))
            if registrar_saida(nome, quantidade):
                print("Saída registrada!")
            else:
                print("Não foi possível registrar a saída.")

        elif opcao == "5":
            print("Sistema encerrado!")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
